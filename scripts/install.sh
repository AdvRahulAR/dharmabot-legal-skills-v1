#!/usr/bin/env bash
# Install Dharmabot Legal Skills into Claude Code, Codex or Antigravity by
# copying the skill folders. (Claude Code users can also use the plugin
# marketplace; see README.)
#
#   ./scripts/install.sh --claude        ~/.claude/skills/
#   ./scripts/install.sh --codex         ~/.agents/skills/
#   ./scripts/install.sh --antigravity   ~/.gemini/config/skills/
#   ./scripts/install.sh --project DIR   DIR/.claude/skills and DIR/.agents/skills
#   ./scripts/install.sh --all           all three user locations
#
# Add --pack NAME (repeatable) to install only some packs:
#   see the pack ids in README.md or docs/CATALOGUE.md
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/plugins/dharmabot-legal-skills/skills"
REGISTRY="$ROOT/plugins/dharmabot-legal-skills/skill-registry.yaml"

targets=()
packs=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --claude) targets+=("$HOME/.claude/skills") ;;
    --codex) targets+=("$HOME/.agents/skills") ;;
    --antigravity) targets+=("$HOME/.gemini/config/skills") ;;
    --all) targets+=("$HOME/.claude/skills" "$HOME/.agents/skills" "$HOME/.gemini/config/skills") ;;
    --project) shift; targets+=("$1/.claude/skills" "$1/.agents/skills") ;;
    --pack) shift; packs+=("$1") ;;
    -h|--help) sed -n '2,15p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

if [[ ${#targets[@]} -eq 0 ]]; then
  sed -n '2,15p' "$0"; exit 2
fi

# Pick skills: all, or those whose pack matches (read from the registry
# without needing PyYAML: each "- id:" line is followed by a "pack:" line).
skills=()
current=""
while IFS= read -r line; do
  if [[ "$line" =~ ^[[:space:]]*-[[:space:]]id:[[:space:]]*(.+)$ ]]; then
    current="${BASH_REMATCH[1]}"
  elif [[ -n "$current" && "$line" =~ ^[[:space:]]*pack:[[:space:]]*(.+)$ ]]; then
    pack="${BASH_REMATCH[1]}"
    if [[ ${#packs[@]} -eq 0 ]]; then
      skills+=("$current")
    else
      for p in "${packs[@]}"; do [[ "$p" == "$pack" ]] && skills+=("$current"); done
    fi
    current=""
  fi
done < "$REGISTRY"

for dest in "${targets[@]}"; do
  mkdir -p "$dest"
  for s in "${skills[@]}"; do
    rm -rf "${dest:?}/$s"
    cp -R "$SRC/$s" "$dest/$s"
  done
  echo "Installed ${#skills[@]} skill(s) into $dest"
done
echo "Restart your agent (or reload skills) to pick them up."
