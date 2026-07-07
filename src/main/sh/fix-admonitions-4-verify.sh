#!/usr/bin/env zsh
# Verify the fix on the live rendered site (read-only). Restart Jekyll first.
pushd "$(git rev-parse --show-toplevel)"
port=$(grep -E '^port' site/_config.yml | grep -oE '[0-9]+')
url="http://127.0.0.1:${port}/riddle-me-this/reflections/2023/05/08/chatGPT-will-replace.html"
echo "1) stylesheet linked in <head>?"
curl -s "$url" | grep -o 'assets/css/asciidoc.css' | head -1 || echo "  MISSING"
echo "2) admonition now emits the font glyph (icon-tip)?"
curl -s "$url" | grep -oE '<i class="fa icon-tip[^"]*"' | head -1 || echo "  MISSING — did you restart the server?"
popd
