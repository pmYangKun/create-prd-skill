#!/usr/bin/env python3
"""
将 create-prd 安装为 Claude Code 技能。

复制技能文件到 ~/.claude/skills/create-prd/
"""

import os
import shutil
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_NAME = "create-prd"

# 确定目标目录
if os.name == "nt":
    CLAUDE_HOME = Path(os.environ.get("USERPROFILE", "~")) / ".claude"
else:
    CLAUDE_HOME = Path.home() / ".claude"

TARGET_DIR = CLAUDE_HOME / "skills" / SKILL_NAME


def install():
    print(f"安装 {SKILL_NAME} 技能...")
    print(f"  源目录: {SKILL_DIR}")
    print(f"  目标目录: {TARGET_DIR}")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    # 复制 SKILL.md
    shutil.copy2(SKILL_DIR / "SKILL.md", TARGET_DIR / "SKILL.md")
    print(f"  SKILL.md 已复制")

    # 复制 references 目录
    refs_target = TARGET_DIR / "references"
    if refs_target.exists():
        shutil.rmtree(refs_target)
    shutil.copytree(SKILL_DIR / "references", refs_target)
    print(f"  references/ 已复制")

    print(f"\n安装完成: {TARGET_DIR}")
    print(f"使用方式: /create-prd 或直接描述产品需求即可自动触发")


if __name__ == "__main__":
    install()
