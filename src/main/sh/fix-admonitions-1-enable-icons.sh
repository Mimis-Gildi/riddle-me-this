#!/usr/bin/env zsh
# Add `icons: font` to _config.yml -> asciidoctor.attributes (idempotent).
pushd "$(git rev-parse --show-toplevel)"
f=site/_config.yml
if grep -qE '^[[:space:]]+icons[[:space:]]*:[[:space:]]*font' "$f"; then
  echo "icons: font already present — no change"
else
  perl -0pi -e 's/^(  attributes:\n)/${1}    icons                   : font\n/m' "$f"
  echo "added icons: font"
fi
grep -nE '^[[:space:]]+(icons|cb-hacker)[[:space:]]*:' "$f"
popd
