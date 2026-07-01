#!/usr/bin/env bash
#
# install.sh
#
# Copies every skill in this repo into your personal Claude skills directory
# (~/.claude/skills/), where Claude loads them automatically by name.
#
# Usage, from the repo root:
#   ./scripts/install.sh
#
# Re-run any time after a `git pull` to update.

set -euo pipefail

# Find the repo root (the parent of this scripts/ folder), so the script works
# no matter where you run it from.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SRC="$REPO_ROOT/skills"
DEST="$HOME/.claude/skills"

if [ ! -d "$SRC" ]; then
  echo "Could not find a skills/ folder at $SRC. Run this from the repo root." >&2
  exit 1
fi

mkdir -p "$DEST"

count=0
for skill in "$SRC"/*/; do
  name="$(basename "$skill")"
  if [ ! -f "$skill/SKILL.md" ]; then
    echo "Skipping $name (no SKILL.md)."
    continue
  fi
  rm -rf "$DEST/$name"
  cp -R "$skill" "$DEST/$name"
  echo "Installed $name"
  count=$((count + 1))
done

echo ""
echo "Done. Installed $count skills into $DEST"
echo "Start a new Claude session and say \"help me get started\" to begin."
