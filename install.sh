#!/bin/bash
# create-prd skill installer for Mac / Linux

set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="$HOME/.claude/skills/create-prd"

echo "Installing create-prd skill..."
echo "Source: $ROOT"
echo "Target: $TARGET"

python3 "$ROOT/scripts/install_skill.py" --source "$ROOT" --target "$TARGET"

echo ""
echo "Done!"
echo "Usage:"
echo "  1. Open Claude Code"
echo "  2. Run: /create-prd"
echo "     or describe your requirement and Claude will trigger it automatically"
