#!/usr/bin/env zsh
# Baseline (read-only): how the admonition currently renders on the live site.
pushd "$(git rev-parse --show-toplevel)"
port=$(grep -E '^port' site/_config.yml | grep -oE '[0-9]+')
curl -s "http://127.0.0.1:${port}/riddle-me-this/reflections/2023/05/08/chatGPT-will-replace.html" \
  | grep -nE 'admonitionblock|td class="icon"|icon-tip' | head
popd
