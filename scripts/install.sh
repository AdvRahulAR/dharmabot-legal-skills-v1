#!/usr/bin/env bash
# Install Dharmabot Legal Skills into Claude Code, Codex or Antigravity.
# This is a thin wrapper around scripts/install.py, which takes the same options
# (run it with --help). On Windows without Git Bash, run install.py directly:
#   py -3 scripts\install.py --antigravity
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
for py in python3 python "py -3"; do
  # Skip the Windows Store alias, which exists but does not run Python.
  if $py -c "import sys" >/dev/null 2>&1; then
    exec $py "$HERE/install.py" "$@"
  fi
done
echo "Python 3 is needed to install the skills (https://www.python.org/downloads/)." >&2
exit 1
