#!/usr/bin/env bash
set -euo pipefail

# --------------------------------------------------------------------
# Mímis-Gildi ShellSpec Bootstrapper — Portable, Reproducible, Friend-Proof
# --------------------------------------------------------------------

# Detect repo root even if invoked from subfolders
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

# Always install to project-local .local folder
INSTALL_PREFIX="$REPO_ROOT/.local"

# Install ShellSpec if not yet present
if [[ ! -x "$INSTALL_PREFIX/bin/shellspec" ]]; then
  echo "🛠 Installing ShellSpec into project-local .local ..."
  curl -fsSL https://git.io/shellspec | sh -s -- --yes --prefix "$INSTALL_PREFIX"
else
  echo "✅ ShellSpec already installed at $INSTALL_PREFIX/bin/shellspec"
fi

# Manage submodule: add if not present
if [[ ! -d ".local/lib/shellspec/.git" ]]; then
  echo "🔗 Initializing ShellSpec as version-anchored submodule ..."
  git submodule add https://github.com/shellspec/shellspec.git .local/lib/shellspec
else
  echo "✅ ShellSpec submodule already linked."
fi

# Update submodules if needed (good practice for CI/colleagues)
echo "🔄 Syncing submodules..."
git submodule update --init --recursive

# Ensure ShellSpec config is initialized
if [[ ! -f "$REPO_ROOT/.shellspec" ]]; then
  echo "📝 Initializing ShellSpec default config..."
  "$INSTALL_PREFIX/bin/shellspec" --init
else
  echo "✅ Existing ShellSpec config detected."
fi

echo -e "\n🎯 ShellSpec is fully installed and ready."
echo -e "👉 Use: .local/bin/shellspec"
