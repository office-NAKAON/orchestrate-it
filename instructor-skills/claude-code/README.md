# Claude Code用スキル

Claude Codeで使用できるスキル集です。

## ディレクトリ構成

```
claude-code/
└── sitemap-search/
    └── SKILL.md
```

## スキル形式

Claude Codeスキルは以下の形式で記述します：

```yaml
---
name: skill-name
description: "スキルの説明。トリガーとなる状況を記述"
user-invocable: true
argument-hint: "[optional arguments]"
---

# スキル名

## 対応タスク
...
```

### 重要ポイント

1. **description**が簡潔で具体的であること
2. `user-invocable: true` でスラッシュコマンドとして呼び出し可能
3. `argument-hint` で引数のヒントを表示

## 導入方法

### 方法1: 手動コピー

1. `.claude/skills/sitemap-search/` ディレクトリを作成
2. `SKILL.md` をコピー

### 方法2: gitサブモジュール

```bash
# プロジェクトルートで実行
git submodule add https://github.com/School-Agent-Inc/orchestrate-it.git .external/orchestrate-it
# スキルをシンボリックリンク
ln -s .external/orchestrate-it/instructor-skills/claude-code/sitemap-search .claude/skills/sitemap-search
```

## スキル一覧

| スキル名 | 説明 |
|---------|------|
| sitemap-search | サイトマップ&サイト内検索機能を実装 |

## 参考

- [Claude Code Skills公式ドキュメント](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
