# Gemini CLI 用スキル

Gemini CLI（`gemini` コマンド）で使用するスキル集です。

## フォルダ構成

```
~/.gemini/
├── GEMINI.md              # グローバル設定
└── skills/                # グローバルスキル
    ├── skill-creator/
    │   └── SKILL.md
    └── sitemap-search/
        └── SKILL.md
```

## 導入方法

### グローバルインストール（推奨）

```bash
# スキルフォルダを作成
mkdir -p ~/.gemini/skills

# スキルをコピー
cp -r skill-creator ~/.gemini/skills/
cp -r sitemap-search ~/.gemini/skills/
```

### プロジェクト単位

```bash
# プロジェクトルートで実行
mkdir -p .gemini/skills
cp -r skill-creator .gemini/skills/
```

## 利用可能なスキル

| スキル | 説明 |
|-------|------|
| skill-creator | スキル作成ガイド |
| sitemap-search | サイトマップ＆検索機能実装 |

## Gemini CLI vs Antigravity

| 項目 | Gemini CLI | Antigravity |
|------|-----------|-------------|
| スキルパス | `.gemini/skills/` | `.agent/skills/` |
| ルールパス | `.gemini/rules/` | `.agent/rules/` |
| グローバル | `~/.gemini/` | `~/.gemini/antigravity/` |
| 用途 | ターミナルでのAI支援 | IDEでのコード生成 |

## 注意

- Gemini CLIとAntigravityはフォルダ構成が異なります
- 両方使う場合は、それぞれのフォルダにスキルを配置してください
