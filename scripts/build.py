#!/usr/bin/env python3
"""
create-prd 技能构建脚本

将所有参考文件拼接生成：
1. dist/create-prd-universal-prompt.md  — 独立可用的完整 prompt，适用于任意 LLM
2. dist/create-prd.skill               — 编译后的技能包
"""

import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = SKILL_DIR / "dist"
REFS_DIR = SKILL_DIR / "references"
FRAMEWORK_DIR = REFS_DIR / "framework"

FRAMEWORK_FILES = [
    FRAMEWORK_DIR / "README.md",
    FRAMEWORK_DIR / "complexity-assessment.md",
    FRAMEWORK_DIR / "global-checks" / "g1-product-type-fit.md",
    FRAMEWORK_DIR / "global-checks" / "g2-document-structure.md",
    FRAMEWORK_DIR / "global-checks" / "g3-major-risks.md",
    FRAMEWORK_DIR / "chapters" / "ch01-background.md",
    FRAMEWORK_DIR / "chapters" / "ch02-basic.md",
    FRAMEWORK_DIR / "chapters" / "ch03-commercial.md",
    FRAMEWORK_DIR / "chapters" / "ch04-goals.md",
    FRAMEWORK_DIR / "chapters" / "ch05-overview.md",
    FRAMEWORK_DIR / "chapters" / "ch06-scope.md",
    FRAMEWORK_DIR / "chapters" / "ch07-risks.md",
    FRAMEWORK_DIR / "chapters" / "ch08-09-terms.md",
    FRAMEWORK_DIR / "chapters" / "ch10-1-framework.md",
    FRAMEWORK_DIR / "chapters" / "ch10-2-detail.md",
    FRAMEWORK_DIR / "chapters" / "ch10-3-exception.md",
    FRAMEWORK_DIR / "chapters" / "ch11-tracking.md",
    FRAMEWORK_DIR / "chapters" / "ch12-permissions.md",
    FRAMEWORK_DIR / "chapters" / "ch13-operations.md",
    FRAMEWORK_DIR / "chapters" / "ch14-tbd.md",
]

# 文件拼接顺序
ORDERED_FILES = [
    SKILL_DIR / "SKILL.md",
    *FRAMEWORK_FILES,
    REFS_DIR / "appendices" / "create-prd-appendix-typing.md",
    REFS_DIR / "chapters" / "create-prd-ch01-background.md",
    REFS_DIR / "chapters" / "create-prd-ch02-basic.md",
    REFS_DIR / "chapters" / "create-prd-ch03-commercial.md",
    REFS_DIR / "chapters" / "create-prd-ch04-goals.md",
    REFS_DIR / "chapters" / "create-prd-ch05-overview.md",
    REFS_DIR / "chapters" / "create-prd-ch06-scope.md",
    REFS_DIR / "chapters" / "create-prd-ch07-risks.md",
    REFS_DIR / "chapters" / "create-prd-ch08-09-terms.md",
    REFS_DIR / "chapters" / "create-prd-ch10-functions.md",
    REFS_DIR / "chapters" / "create-prd-ch11-tracking.md",
    REFS_DIR / "chapters" / "create-prd-ch12-permissions.md",
    REFS_DIR / "chapters" / "create-prd-ch13-operations.md",
    REFS_DIR / "chapters" / "create-prd-ch14-tbd.md",
    REFS_DIR / "appendices" / "create-prd-appendix-selfcheck.md",
]


def build_universal_prompt():
    """将所有参考文件拼接为独立可用的 universal prompt。"""
    DIST_DIR.mkdir(exist_ok=True)

    parts = []
    parts.append("# Create-PRD 完整独立 Prompt\n")
    parts.append("> 本文件是 create-prd 技能的完整独立版本，可在任何 LLM 中直接使用。\n")
    parts.append("> 将本文件内容粘贴到 ChatGPT / Gemini / DeepSeek / Claude 等 LLM 中，")
    parts.append("> 然后提供你的业务上下文，即可生成结构化 PRD。\n")
    parts.append("> 本版本已内联复杂度分级与章节质量基线，无需额外预装 framework 目录。\n")
    parts.append("---\n")

    for fpath in ORDERED_FILES:
        if not fpath.exists():
            print(f"  WARNING: {fpath.name} 不存在，跳过")
            continue

        content = fpath.read_text(encoding="utf-8")

        # SKILL.md 需要去掉 frontmatter 并将文件引用转为内联
        if fpath.name == "SKILL.md":
            if content.startswith("---"):
                end = content.index("---", 3)
                content = content[end + 3:].strip()
            content = re.sub(
                r'\[([^\]]+)\]\(references/[^)]+\)',
                r'\1',
                content
            )

        parts.append(f"\n{'='*60}\n")
        parts.append(f"## {fpath.stem}\n")
        parts.append(content)
        parts.append("\n")

    universal = "\n".join(parts)

    out_path = DIST_DIR / "create-prd-universal-prompt.md"
    out_path.write_text(universal, encoding="utf-8")
    print(f"  universal prompt: {out_path}")
    print(f"  大小: {len(universal):,} 字符 / 约 {len(universal)//4:,} tokens")

    # 同时生成 .skill 文件
    skill_path = DIST_DIR / "create-prd.skill"
    skill_path.write_text(universal, encoding="utf-8")
    print(f"  技能包: {skill_path}")


def validate():
    """校验所有引用的文件是否存在。"""
    print("校验文件结构...")
    ok = True
    for fpath in ORDERED_FILES:
        status = "OK" if fpath.exists() else "缺失"
        print(f"  [{status}] {fpath.relative_to(SKILL_DIR)}")
        if not fpath.exists():
            ok = False

    if ok:
        print("所有文件就绪。\n")
    else:
        print("部分文件缺失！\n")
    return ok


if __name__ == "__main__":
    print("构建 create-prd 技能...\n")
    validate()
    build_universal_prompt()
    print("\n构建完成！")
