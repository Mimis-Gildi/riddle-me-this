#!/usr/bin/env bash

set -euo pipefail

# Determine repo root
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

# Create test directory structure
mkdir -p src/test/helper
mkdir -p .saga-notes/letters

# Create placeholder index.text for Saga Notes
if [[ ! -f ".saga-notes/letters/index.text" ]]; then
  echo "(Saga Letters Capsule Initialized)" > .saga-notes/letters/index.text
fi

# Install ShellSpec locally if not yet installed
INSTALL_DIR="$REPO_ROOT/.local"

if [[ ! -x "$INSTALL_DIR/bin/shellspec" ]]; then
  echo "🛠 Installing ShellSpec locally..."
  curl -fsSL https://git.io/shellspec | sh -s -- --yes --prefix "$INSTALL_DIR"
else
  echo "✅ ShellSpec already installed at $INSTALL_DIR/bin/shellspec"
fi

# Create .shellspec config if missing
if [[ ! -f ".shellspec" ]]; then
  cat > .shellspec <<EOF
--require spec_helper
--default-path src/test/sh
--shell bash
--kcov-options "--include-pattern=.sh"
EOF
  echo "✅ .shellspec initialized."
fi

# Create spec_helper if missing
if [[ ! -f "src/test/helper/spec_helper.sh" ]]; then
  cat > src/test/helper/spec_helper.sh <<EOF
#!/usr/bin/env bash
# shellcheck shell=bash

spec_helper_precheck() {
  : minimum_version "0.28.1"
}

spec_helper_loaded() {
  :
}

spec_helper_configure() {
  :
}
EOF
  chmod +x src/test/helper/spec_helper.sh
  echo "✅ spec_helper initialized."
fi

echo "🎯 Saga Ops Bootstrap Packager Complete."
