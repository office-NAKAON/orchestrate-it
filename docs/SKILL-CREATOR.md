# Skill Creator: スキル作成ガイド

Anthropicが公開している[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)をベースにした、効果的なスキル作成のためのガイドです。

## Skill Creatorとは？

AIコードエディタ（Claude Code、Google Antigravity、Cursor）で使用できるスキル/ルールを作成するためのベストプラクティス集です。

## 核心原則

### 1. コンテキストは公共財

> "コンテキストウィンドウは公共財である"

スキルはAIが必要とする他の全てのものとコンテキストを共有します。**必要最小限の情報のみ**を含めてください。

### 2. 適切な具体性レベル

| 自由度 | 形式 | 使用場面 |
|--------|------|----------|
| 高 | テキスト説明 | 柔軟なアプローチが適切な場合 |
| 中 | 疑似コード | パターンに多少のバリエーションがある場合 |
| 低 | 具体的スクリプト | 精密さが必要な脆弱な操作 |

### 3. プログレッシブ・ディスクロージャー

スキルは3段階でコンテキストを管理：

1. **メタデータ** (~100語) - 常時利用可能
2. **SKILL.md本文** (起動時) - 5000語以下推奨
3. **バンドルリソース** (必要時) - 要求に応じて読み込み

---

## 導入方法

### Claude Code

skill-creatorは `~/.claude/skills/` にグローバルスキルとして導入済み。
どのフォルダを開いても利用可能です。

```
~/.claude/skills/skill-creator/
├── SKILL.md
├── scripts/
│   ├── init_skill.py
│   ├── quick_validate.py
│   └── package_skill.py
└── references/
    ├── output-patterns.md
    └── workflows.md
```

### Google Antigravity

`~/.gemini/antigravity/skills/` にグローバルスキルとして導入済み。

```
~/.gemini/antigravity/skills/skill-creator/
├── SKILL.md
├── scripts/
└── references/
```

### Cursor

`~/.cursor/rules/` にグローバルルールとして導入済み。

```
~/.cursor/rules/skill-creator.mdc
```

---

## 使い方

### 新しいスキルを作成

1. チャットで「新しいスキルを作りたい」と伝える
2. skill-creatorが自動的に起動
3. ガイドに従ってスキルを設計

### スクリプトを直接使用

```bash
# スキルの初期化
python ~/.claude/skills/skill-creator/scripts/init_skill.py my-skill --path .claude/skills

# スキルの検証
python ~/.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill

# スキルのパッケージ化
python ~/.claude/skills/skill-creator/scripts/package_skill.py .claude/skills/my-skill
```

---

## スキル構造

### 必須ファイル

```
skill-name/
└── SKILL.md          # YAML frontmatter + Markdown指示
```

### オプションリソース

```
skill-name/
├── SKILL.md
├── scripts/          # 実行可能コード（Python, Bash等）
├── references/       # 必要時に読み込むドキュメント
└── assets/           # テンプレート、出力用ファイル
```

### YAML Frontmatter形式

**Claude Code:**
```yaml
---
name: skill-name
description: "スキルの説明。トリガーとなる状況を記述"
---
```

**Google Antigravity:**
```yaml
---
name: skill-name
description: |
  スキルの説明。
  Use when: トリガーキーワード1, キーワード2
  Do not use when: 除外条件
---
```

**Cursor:**
```yaml
---
description: "ルールの説明"
globs: ["**/*.tsx"]
---
```

---

## ベストプラクティス

### 良いスキル

- ✅ 500行以下のSKILL.md
- ✅ 明確な`description`（いつ使うかが分かる）
- ✅ 必要時のみリソースを読み込む
- ✅ 具体例を含む

### 避けるべきこと

- ❌ README.md, CHANGELOG.mdなど不要なファイル
- ❌ 500行を超えるSKILL.md
- ❌ 曖昧な`description`
- ❌ AIが既に知っている情報の重複

---

## 参考リンク

- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Claude Code Skills Documentation](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Antigravity Skills Documentation](https://antigravity.google/docs/skills)
- [Cursor Rules Documentation](https://cursor.com/docs/context/rules)
