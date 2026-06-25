#!/usr/bin/env zsh
# Link asciidoc.css into _includes/head/custom.html (idempotent).
pushd "$(git rev-parse --show-toplevel)"
f=site/_includes/head/custom.html
if grep -q 'assets/css/asciidoc.css' "$f"; then
  echo "already linked — no change"
else
  cat >> "$f" <<'HTML'
<!-- Asciidoctor admonition styling; see assets/css/asciidoc.css for source + rationale. -->
<link rel="stylesheet" href="{{ '/assets/css/asciidoc.css' | relative_url }}">
HTML
  echo "linked asciidoc.css"
fi
grep -n 'asciidoc.css' "$f"
popd
