# 講師提供スキル集

このディレクトリには、講座の講師が作成した参考用スキルが含まれています。
各プラットフォーム（AIコードエディタ）に対応した形式で提供しています。

## ディレクトリ構成

```
instructor-skills/
├── antigravity/       # Google Antigravity用
│   ├── gas-webapp-hig/    # GAS Webアプリ開発（HIG準拠）
│   └── sitemap-search/
├── claude-code/       # Claude Code用
│   ├── gas-webapp-hig/    # GAS Webアプリ開発（HIG準拠）
│   └── sitemap-search/
├── cursor/            # Cursor用
│   ├── gas-webapp-hig/    # GAS Webアプリ開発（HIG準拠）
│   └── sitemap-search/
└── gemini-cli/        # Gemini CLI用
    ├── gas-webapp-hig/    # GAS Webアプリ開発（HIG準拠）
    └── sitemap-search/
```

## プラットフォーム別の違い

| プラットフォーム | ファイル形式 | 配置場所 | 特徴 |
|----------------|-------------|---------|------|
| Antigravity | `SKILL.md` | `.agent/skills/` | YAML frontmatter + Markdown |
| Claude Code | `SKILL.md` | `.claude/skills/` | YAML frontmatter + Markdown |
| Cursor | `.mdc` | `.cursor/rules/` | Frontmatter + Markdown、glob対応 |

## 提供スキル

### GAS Webアプリ HIG準拠 (`gas-webapp-hig`)

Google Apps Script（GAS）で高品質なWebアプリを開発するスキル。

**機能:**
- HIG（Human Interface Guidelines）20原則準拠
- 6種類のテーマ（ライト、ダーク、オーシャン、フォレスト、サンセット、サクラ）
- ロード画面、ツアー機能、設定モーダル
- GAS固有の制約（遅延、中断不可、取り消し不可）への対策
- 日本語UI必須ルール

**出力ファイル:**
- コード.gs（doGet関数 + サーバーサイド処理）
- Index.html（HTML/CSS/JS統合）

**クレジット:**
- Original: [gas-webapp-prompt-hig.md](https://github.com/akari-iku/gas-webapp-prompt/blob/main/prompt/gas-webapp-prompt-hig.md)
- Author: Akari ([akari-iku](https://github.com/akari-iku))
- License: MIT

---

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
https://github.com/School-Agent-Inc/orchestrate-it/tree/main/instructor-skills/antigravity/gas-webapp-hig
```

### Claude Code

`.claude/skills/gas-webapp-hig/` ディレクトリにSKILL.mdとreferences/をコピー

### Gemini CLI

`~/.gemini/skills/gas-webapp-hig/` にSKILL.mdとreferences/をコピー

### Cursor

`.cursor/rules/` ディレクトリに `gas-webapp-hig.mdc` をコピー
