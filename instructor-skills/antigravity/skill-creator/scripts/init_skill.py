#!/usr/bin/env python3
"""
スキル初期化スクリプト - 新しいスキルをテンプレートから作成

使い方:
    python init_skill.py <skill-name> --path <path>

例:
    python init_skill.py my-skill --path .agent/skills
    python init_skill.py report-generator --path ~/.gemini/antigravity/skills
"""

import sys
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: |
  [TODO: スキルの説明を1-2文で記述]
  Use when: [TODO: トリガーキーワードをカンマ区切りで記述]
  Do not use when: [TODO: 除外条件を記述]
---

# {skill_title}

[TODO: このスキルが何をするか1-2文で説明]

## このスキルを使用する時

- [TODO: 条件1]
- [TODO: 条件2]

## このスキルを使用しない時

- [TODO: 除外条件1]
- [TODO: 除外条件2]

## 対応タスク

1. [TODO: タスク1]
2. [TODO: タスク2]
3. [TODO: タスク3]

## 実行方法

[TODO: 具体的な手順を記述]

## ヒアリング項目

実装前に以下を確認：

- [TODO: 確認事項1]
- [TODO: 確認事項2]

## 出力形式

[TODO: どのような形式で出力するか記述]

---

## Tips

- SKILL.mdは500行以下に保つ
- 具体例を含める
- 不要なセクションは削除してOK
"""


def title_case(name):
    """ハイフン区切りの名前をタイトルケースに変換"""
    return ' '.join(word.capitalize() for word in name.split('-'))


def init_skill(skill_name, path):
    """新しいスキルディレクトリを作成"""
    skill_dir = Path(path).resolve() / skill_name

    if skill_dir.exists():
        print(f"エラー: ディレクトリが既に存在します: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True)
        print(f"✓ ディレクトリ作成: {skill_dir}")
    except Exception as e:
        print(f"エラー: {e}")
        return None

    # SKILL.md作成
    skill_md = skill_dir / 'SKILL.md'
    content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=title_case(skill_name)
    )
    skill_md.write_text(content, encoding='utf-8')
    print(f"✓ SKILL.md作成")

    print(f"\n✓ スキル '{skill_name}' を作成しました: {skill_dir}")
    print("\n次のステップ:")
    print("1. SKILL.mdの[TODO]を編集")
    print("2. 必要に応じてscripts/, references/を追加")
    print("3. 実際に使ってテスト")

    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("使い方: python init_skill.py <skill-name> --path <path>")
        print("\n例:")
        print("  python init_skill.py my-skill --path .agent/skills")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    print(f"スキル初期化: {skill_name}")
    print(f"配置先: {path}\n")

    result = init_skill(skill_name, path)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
