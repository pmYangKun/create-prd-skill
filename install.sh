#!/bin/bash
# create-prd skill 安装脚本（Mac / Linux）

set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="$HOME/.claude/skills/create-prd"

echo "正在安装 create-prd skill..."
echo "源目录：$ROOT"
echo "目标目录：$TARGET"

python3 "$ROOT/scripts/install_skill.py" --source "$ROOT" --target "$TARGET"

echo ""
echo "安装完成！"
echo "使用方式："
echo "  1. 打开 Claude Code"
echo "  2. 输入 /create-prd"
echo "     或直接描述你的需求，Claude 会自动触发该 skill"
