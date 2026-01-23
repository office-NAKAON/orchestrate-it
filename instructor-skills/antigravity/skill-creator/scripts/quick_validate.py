#!/usr/bin/env python3
"""
スキル検証スクリプト - SKILL.mdの構造をチェック

使い方:
    python quick_validate.py <skill-directory>

例:
    python quick_validate.py .agent/skills/my-skill
"""

import sys
import re
from pathlib import Path


def validate_skill(skill_path):
    """スキルの基本検証"""
    skill_path = Path(skill_path)

    # SKILL.mdの存在確認
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.mdが見つかりません"

    content = skill_md.read_text(encoding='utf-8')

    # Frontmatterの確認
    if not content.startswith('---'):
        return False, "YAML frontmatterがありません（---で始まる必要があります）"

    # Frontmatter抽出
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "frontmatterの形式が不正です"

    frontmatter = match.group(1)

    # nameの確認
    if 'name:' not in frontmatter:
        return False, "'name'がfrontmatterにありません"

    # descriptionの確認
    if 'description:' not in frontmatter:
        return False, "'description'がfrontmatterにありません"

    # Use whenの確認（推奨）
    if 'Use when:' not in frontmatter and 'Use when:' not in content:
        print("警告: 'Use when:'がありません（推奨）")

    # 行数チェック
    lines = content.count('\n') + 1
    if lines > 500:
        return False, f"SKILL.mdが500行を超えています（{lines}行）"

    # TODOの残存チェック
    if '[TODO:' in content:
        todo_count = content.count('[TODO:')
        print(f"警告: {todo_count}個のTODOが残っています")

    return True, f"スキルは有効です（{lines}行）"


def main():
    if len(sys.argv) != 2:
        print("使い方: python quick_validate.py <skill-directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)


if __name__ == "__main__":
    main()
