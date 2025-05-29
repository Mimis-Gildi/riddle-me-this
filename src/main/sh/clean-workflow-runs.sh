#!/usr/bin/env bash
### Modified from Mímis Gildi
# Original shell: zsh

echo "::notice title=Workflow Runs Pruner::Starting GH CLI pruning run for <$GITHUB_REPOSITORY>"

on_branch="${BRANCH:-$(git rev-parse --abbrev-ref HEAD)}"
echo "::notice title=Active Branch Detected::<$on_branch>"

mapfile -t workflows < <(gh workflow list --json id,name,path,state -q '.[] | @base64')
echo "::notice title=Workflow Count::Found ${#workflows[@]} workflows to inspect."

for encoded in "${workflows[@]}"; do
  decoded="$(echo "$encoded" | base64 --decode)"
  workflow_id="$(jq -r '.id' <<< "$decoded")"
  workflow_name="$(jq -r '.name' <<< "$decoded")"
  workflow_state="$(jq -r '.state' <<< "$decoded")"

  echo "::group::🌀 $workflow_name ($workflow_state)"

  if [[ -z "$workflow_id" ]]; then
    echo "::notice title=NOOP::Workflow $workflow_name has no ID or is invalid."
    echo "::endgroup::"
    continue
  fi

  mapfile -t run_ids < <(gh run list --workflow="$workflow_id" --json databaseId --limit 500 -q '.[1:] | .[].databaseId')
  run_count="${#run_ids[@]}"

  echo "::notice title=Prunable Runs::Found $run_count old runs for $workflow_name"

  for run_id in "${run_ids[@]}"; do
    if [[ -z "$run_id" ]]; then
      echo "::notice title=NOOP::Empty or invalid run ID detected."
      continue
    fi
    gh run delete "$run_id" --yes
    echo "::notice title=Deleted::$run_id for $workflow_name"
  done

  echo "::endgroup::"
done
