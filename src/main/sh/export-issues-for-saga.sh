#!/usr/bin/env bash
# Dump issue data into Saga capsule format by list or range.
# Fully self-contained, simple, reproducible.
set -euo pipefail

# These folders are expected -- otherwise fail.
repository_root="$(git rev-parse --show-toplevel)"
notes_for_saga="${repository_root}/.saga-notes"
letters_for_saga="$notes_for_saga/letters"

# Reserved files: index expected, and issues ignored.
about_saga_letters="$letters_for_saga/index.text"
issues_for_saga="$letters_for_saga/issues-for-saga.json"
[[ -f "$about_saga_letters" ]] || { echo "Error: Saga's index file does not exist ($about_saga_letters)."; exit 11; }

# Use all issues from commandline; otherwise just find open issues in sorted order.
function acquire_issue_ids() {
  declare -a the_issues_numbers_local=()

  if [[ $# -eq 0 ]]; then
    while IFS= read -r issue_number; do
      echo "... found issue: $issue_number"
      the_issues_numbers_local+=("$issue_number")
    done <<< "$( gh issue list --limit 100 --state all --json number -q '.[] | .number' | sort -n )"
  else
    the_issues_numbers_local=("$@")
  fi

  if (( ${#the_issues_numbers_local[@]} == 0 )); then
    echo "... nothing to do."
    exit 13
  else
    echo "... acquired ${#the_issues_numbers_local[@]} issues."
  fi

  the_issues_numbers=("${the_issues_numbers_local[@]}")
}

# Read issue data for each issue number.
function read_issues_data(){
  declare -a the_issues_data_local=()

  for issue_number in "$@"; do
    echo -e "🔍 Exporting issue #$issue_number."

    if ! issue_text=$(gh issue view "$issue_number" --json number,title,body,url,state,author,createdAt,updatedAt 2>/dev/null); then
      echo -e "⚠️  Issue #$issue_number not found, skipping."
      continue
    fi

    issue_body_tasks=$(echo "$issue_text" | jq -r '.body' | grep -E '^- \[.\]' || true)

    issue_structured=$(jq -n -c       --argjson issue "$issue_text"       --arg tasks "$issue_body_tasks"       '{
        number: $issue.number,
        title: $issue.title,
        body: $issue.body,
        url: $issue.url,
        state: $issue.state,
        author: $issue.author.login,
        createdAt: $issue.createdAt,
        updatedAt: $issue.updatedAt,
        taskList: ($tasks | split("\n") | map(select(length > 0)))
      }')

    the_issues_data_local+=("$issue_structured")
  done

  the_issues_data=("${the_issues_data_local[@]}")
}

function write_issues_data() {
  printf '%s\n' "$@" | jq -s '.' > "$issues_for_saga"
}

function main() {
  acquire_issue_ids "$@"
  read_issues_data "${the_issues_numbers[@]}"
  write_issues_data "${the_issues_data[@]}"
  echo -e "\n✅ Export complete: $issues_for_saga"
}

main "$@"
