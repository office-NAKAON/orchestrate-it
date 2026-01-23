# Cursor用ルール

Cursorで使用できるルール（Rules）集です。

## ディレクトリ構成

```
cursor/
└── sitemap-search/
    └── sitemap-search.mdc
```

## ルール形式

Cursorルールは `.mdc` または `.md` 形式で記述します：

```yaml
---
description: "ルールの説明。AIが適用判断に使用"
globs: ["**/対象パターン/**"]
---

# ルール名

## ガイドライン
...
```

### 適用モード

| フィールド | 説明 |
|-----------|------|
| `alwaysApply: true` | 常に適用 |
| `globs: [...]` | 特定ファイルパターンに適用 |
| （description のみ） | AIが自動判断 |

### 重要ポイント

1. **description**がルール適用の判断基準
2. `globs` で対象ファイルを限定できる
3. `.mdc` 形式を推奨（最新形式）

## 導入方法

1. `.cursor/rules/` ディレクトリを作成（なければ）
2. `.mdc` ファイルをコピー

```bash
mkdir -p .cursor/rules
cp sitemap-search/sitemap-search.mdc .cursor/rules/
```

## ルール一覧

| ルール名 | 対象glob | 説明 |
|---------|---------|------|
| sitemap-search | `**/sitemap/**`, `**/search/**` | サイトマップ&検索機能の実装パターン |

## 参考

- [Cursor Rules公式ドキュメント](https://cursor.com/docs/context/rules)
- [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)
