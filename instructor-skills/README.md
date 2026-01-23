# 講師提供スキル集

このディレクトリには、講座の講師が作成した参考用スキルが含まれています。
各プラットフォーム（AIコードエディタ）に対応した形式で提供しています。

## ディレクトリ構成

```
instructor-skills/
├── antigravity/       # Google Antigravity用
│   └── sitemap-search/
├── claude-code/       # Claude Code用
│   └── sitemap-search/
└── cursor/            # Cursor用
    └── sitemap-search/
```

## プラットフォーム別の違い

| プラットフォーム | ファイル形式 | 配置場所 | 特徴 |
|----------------|-------------|---------|------|
| Antigravity | `SKILL.md` | `.agent/skills/` | YAML frontmatter + Markdown |
| Claude Code | `SKILL.md` | `.claude/skills/` | YAML frontmatter + Markdown |
| Cursor | `.mdc` | `.cursor/rules/` | Frontmatter + Markdown、glob対応 |

## 提供スキル

### サイトマップ & サイト内検索 (`sitemap-search`)

Webサイトにサイトマップページとサイト内検索機能を実装するスキル。

**機能:**
- サイトマップページの作成
- サイト内検索機能（リアルタイム検索）
- キーボードショートカット（Cmd/Ctrl + K）
- タグ・カテゴリによるフィルタリング
- 検索結果のハイライト表示

**対応フレームワーク:**
- Next.js / React
- バニラHTML/CSS/JavaScript

---

## 導入方法

### Google Antigravity

```
このスキルを導入して
https://github.com/School-Agent-Inc/orchestrate-it/tree/main/instructor-skills/antigravity/sitemap-search
```

### Claude Code

`.claude/skills/sitemap-search/` ディレクトリにSKILL.mdをコピー

### Cursor

`.cursor/rules/` ディレクトリに `.mdc` ファイルをコピー
