#!/usr/bin/env bash
#
# build-bundles.sh
#
# Packages each skill into a single-click installable `.skill` bundle for
# Claude Cowork. A `.skill` file is just a zip of the skill folder. Cowork's
# "Save skill" button installs one in a click.
#
# Usage, from the repo root:
#   ./scripts/build-bundles.sh
#
# Output: dist/<skill-name>.skill, one per skill.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SRC="$REPO_ROOT/skills"
DIST="$REPO_ROOT/dist"

if ! command -v zip >/dev/null 2>&1; then
  echo "This script needs the 'zip' command, which is not installed." >&2
  exit 1
fi

mkdir -p "$DIST"
rm -f "$DIST"/*.skill 2>/dev/null || true

count=0
for skill in "$SRC"/*/; do
  name="$(basename "$skill")"
  if [ ! -f "$skill/SKILL.md" ]; then
    echo "Skipping $name (no SKILL.md)."
    continue
  fi
  # Zip from inside skills/ so the archive contains <name>/SKILL.md at its root.
  (cd "$SRC" && zip -r -q "$DIST/$name.skill" "$name" -x '*.DS_Store')
  echo "Built dist/$name.skill"
  count=$((count + 1))
done

echo ""
echo "Done. Built $count bundles into $DIST"
echo "In Cowork: Customize > Settings > Capabilities > Skills > + > Save skill, then pick a .skill file."
