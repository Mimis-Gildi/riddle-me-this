#!/usr/bin/env zsh

# Delete the dead blog-url / blog-title / blog-link attribute trio.
#
#     :blog-url: link:{site-baseurl}/
#     :blog-title: Creative Engineering at Scale
#     :blog-link: {blog-url}[{blog-title}]
#
# These are DEFINED in 25 files but REFERENCED only inside
# _fragments/publication-bridging.adoc -- a template that nothing includes and
# that isn't a rendered collection. Everywhere else the trio is dead weight.
#
# SAFETY RULE: a file is a target ONLY if it defines :blog-link: AND never
# references {blog-url}/{blog-title}/{blog-link} outside the definition lines.
# publication-bridging.adoc references them, so it is auto-excluded and left
# untouched -- this script cannot break the one place they're live.
#
# Default is DRY-RUN (prints TARGET/SKIP, changes nothing).
# Pass --apply to delete the three attribute lines in place.
#
#     src/main/sh/delete-dead-blog-attrs.sh            # preview
#     src/main/sh/delete-dead-blog-attrs.sh --apply    # delete

set -euo pipefail

PROJECT_ROOT=$(git rev-parse --show-toplevel)
cd "$PROJECT_ROOT"

apply=0
[[ "${1:-}" == "--apply" ]] && apply=1

targets=0
skips=0

# Candidates: every file that defines :blog-link:
grep -rl '^:blog-link:' site/ | while IFS= read -r f; do
  # References to the trio, EXCLUDING the ":blog-*:" definition lines themselves.
  uses=$(grep -nE '\{blog-(url|title|link)\}' "$f" \
           | grep -vE '^[0-9]+::blog-(url|title|link):' || true)

  if [[ -n "$uses" ]]; then
    print "SKIP (referenced): $f"
    skips=$((skips + 1))
    continue
  fi

  print "TARGET: $f"
  targets=$((targets + 1))

  if [[ $apply -eq 1 ]]; then
    # Delete the three attribute definition lines by key (handles them whether
    # or not they are contiguous; matches the keys, not specific values).
    sed -i '' -E \
      -e '/^:blog-url:[[:space:]]/d' \
      -e '/^:blog-title:[[:space:]]/d' \
      -e '/^:blog-link:[[:space:]]/d' \
      "$f"
  fi
done

print ""
if [[ $apply -eq 1 ]]; then
  print "APPLIED. Deleted the trio from each TARGET above."
else
  print "DRY RUN -- nothing changed. Re-run with --apply to delete."
fi