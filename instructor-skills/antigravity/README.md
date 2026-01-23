# Google Antigravity用スキル

Google Antigravityで使用できるスキル集です。

## ディレクトリ構成

```
antigravity/
├── skill-creator/       # スキル作成ガイド（まずこれを導入！）
│   ├── SKILL.md
│   ├── scripts/
│   └── references/
└── sitemap-search/      # サイトマップ&検索機能
    └── SKILL.md
```

## スキル形式

Antigravityスキルは以下の形式で記述します：

```yaml
---
name: skill-name
description: |
  スキルの説明。
  Use when: トリガーキーワード1、キーワード2
---

# スキル名

## 役割
...
```

### 重要ポイント

1. **`Use when:`** を必ず含める（AIが自動判断する際の手がかり）
2. descriptionは複数行でOK
3. 日本語対応

## 導入方法

Antigravityのチャットで以下のように入力：

```
このスキルを導入して
https://github.com/School-Agent-Inc/orchestrate-it/tree/main/instructor-skills/antigravity/sitemap-search
```

## スキル一覧

| スキル名 | 説明 | 優先度 |
|---------|------|-------|
| **skill-creator** | スキル作成ガイド（まずこれを導入！） | ★★★ |
| sitemap-search | サイトマップ&サイト内検索機能を実装 | ★★ |

## 参考

- [Antigravity公式ドキュメント](https://antigravity.google/docs/skills)
