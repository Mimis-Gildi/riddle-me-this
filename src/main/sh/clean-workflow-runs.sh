#!/usr/bin/env bash
### Modified from Mímis Gildi
# Original shell: zsh

on_branch="${BRANCH:-$(git rev-parse --abbrev-ref HEAD)}"
echo "::notice title=Workflow Runs Pruner::Agent host <$(hostname)>: Running on branch <$on_branch>.";

IFS=$'\n' read -r -d '' -a workflows <<< "$(gh workflow list --json id,name,path,state -q '.[] | [ .id, .name, .path, .state ] | @csv')"
for workflow_row in "${workflows[@]}"; do
  IFS=',' read -r -d '' workflow_id workflow_name workflow_description workflow_state <<< "${workflow_row//$'\n'/}"
  echo "::group::$workflow_name";

  if [[ -z "${workflow_id// }" ]]; then
    echo "::notice title=NOOP::Workflow $workflow_name has no runs to clean up. ($workflow_id,$workflow_state) $workflow_description.";
  else
    IFS=$'\n' read -r -d '' -a run_ids <<< "$(gh run list --workflow="$workflow_id" --json databaseId --limit 500 -q '.[1:] | .[].databaseId')"
    echo "${run_ids[*]}"
    for run_id in "${run_ids[@]}"; do
      if [[ -z "${run_id// }" ]]; then
        echo "::notice title=NOOP(row)::This run is empty/null.";
      else
        gh run delete "$run_id"
        echo "::notice title=$run_id::Requested deletion of run ID: $run_id for workflow: $workflow_name"
      fi
    done
  fi
  echo "::endgroup::"
done
