#!/usr/bin/env bash
set -uo pipefail
declare -i MAX_PARALLEL=${MAX_PARALLEL:-100}

readonly repository="${REPO:-$(basename "$(git rev-parse --show-toplevel)")}"
readonly branch="${BRANCH:-$(git rev-parse --abbrev-ref HEAD)}"
echo "::notice title=Workflow Runs Pruner::Starting GH CLI pruning run for <$repository>"
echo "::notice title=Active Branch Detected::<$branch>"

declare -a workflows
declare -a runs_to_prune

function acquire_workflows_to_process() {
  local -i workflow_count=0
  local -r debug="${1:-off}"

  echo "::group::Acquire workflows to inspect."
  # Note: CSV is fine as there will not be commas in the workflow names; otherwise we'll use @base64 when the first one breaks.
  local -r workflows_as_text="$(gh workflow list --json id,name,path,state -q '.[] | [ .id, .name, .path, .state ] | @csv')"
  while IFS= read -r workflow_row; do
    IFS=',' read -r workflow_id workflow_name workflow_path workflow_state <<< "${workflow_row//}"
    [[ "$debug" == "on" ]] && echo "::debug title=Reading a Workflow row::Workflow $workflow_name with ID $workflow_id in sate $workflow_state and at path  $workflow_path."
    if [[ -z "${workflow_id// }" ]]; then
      echo "::notice title=NOOP::Workflow $workflow_name has an empty ID that makes no sense. Skipping it!"
    else
      [[ "$debug" == "on" ]] && echo "::debug title=Workflow Found::$workflow_id|$workflow_name|$workflow_path|$workflow_state"
      workflows+=("$workflow_id|$workflow_name|$workflow_path|$workflow_state")
      workflow_count=$((workflow_count + 1))
    fi
  done <<< "$workflows_as_text"
  echo "::notice title=Acquired Workflows::There are $workflow_count workflows to process."
  echo "::endgroup::"
}

function prepare_workflows_to_process() {
  local executed_runs_text=''
  local -i runs_count=0 workflow_runs_count=0
  local -r debug="${1:-off}"

  echo "::group::Prepare workflows to inspect."
  for workflow_row in "${workflows[@]}"; do
    IFS='|' read -r workflow_id workflow_name workflow_path workflow_state <<< "${workflow_row//\"/}"
    echo "::notice title=Reading runs for $workflow_name::Extracting all but one runs for $workflow_state workflow with id $workflow_id and declaration path $workflow_path."

    # Important, we're skipping one to leave behind; it does not need to be the last one but usually is.
    executed_runs_text="$(gh run list --workflow="$workflow_id" --json databaseId --limit 1000 | jq -r '.[1:][]?.databaseId')"
    [[ "$debug" == "on" ]] && echo -e "::debug title=Processing textual run information as: |\n$executed_runs_text\n| a query response."

    while IFS= read -r run_row; do
      (( runs_count++ ))
      if [[ -z "${run_row//}" ]]; then
        [[ "$debug" == "on" ]] && echo "::debug title=INVALID Run ID:: Skipping an empty run id ($run_row) in workflow $workflow_name."
      else
        run_entry="$run_row|$workflow_name"
        runs_to_prune+=("$run_entry")
        (( workflow_runs_count++ ))
        echo "::notice title=Queued a run::$run_entry."
      fi
    done <<< "${executed_runs_text}"
  done

  echo "::notice title=Prepared workflow runs to prune::Total $runs_count run rows processed and $workflow_runs_count queued to prune."
  echo "::endgroup::"
}

function process_workflows_to_process(){
  local -r debug="${1:-off}"
  local -i requests_count=0
  echo "::group::Process sending off deletion requests."
  for run_delete_request in "${runs_to_prune[@]}"; do
    IFS='|' read -r run_id run_workflow_name <<< "$run_delete_request"
    if [[ -n "${run_id// }" ]]; then
      (( requests_count++ ))
      (
        gh run delete "$run_id"
        echo "::notice title=Deleted::$run_id of $run_workflow_name"
      ) &

      if (( requests_count % MAX_PARALLEL == 0 )); then
        wait
      fi
    fi

  done
  wait
  echo "::endgroup::"
}

function main() {
  local debug_acquire="${1:-off}"
  local debug_prepare="${2:-on}"
  local debug_process="${3:-off}"

  acquire_workflows_to_process "$debug_acquire"
  prepare_workflows_to_process "$debug_prepare"
  process_workflows_to_process "$debug_process"

}

main "$@"
