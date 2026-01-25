# GAS Webアプリ HIG準拠開発スキル

Google Apps Script（GAS）で高品質なWebアプリを開発するためのスキル。
Apple Human Interface Guidelines（HIG）の20原則を組み込み、業界標準のUI/UXを保証します。

## 対象ツール

このスキルは以下のAIツールで使用できます：

| ツール | 導入方法 |
|--------|----------|
| Claude Code | `.agent/skills/` に配置済み |
| Gemini CLI | `.gemini/` にコピー |
| Google Antigravity | `.antigravity/` にコピー |
| Cursor | `.cursor/rules/` にコピー |

## クイックスタート

### Claude Code / Gemini CLI / Antigravity

チャットで以下のように依頼：

```
GASでタスク管理Webアプリを作って
```

スキルが自動的に適用され、HIG準拠の高品質なアプリが生成されます。

### Cursor

`.cursor/rules/` にコピー後、チャットで同様に依頼。

## ファイル構成

```
gas-webapp-hig/
├── SKILL.md              # メインスキル定義
├── README.md             # このファイル
└── references/
    ├── hig-principles.md # HIG 20原則の詳細
    ├── design-system.md  # CSS変数、テーマ、テンプレート
    ├── gas-constraints.md # GAS制約と対策
    └── checklist.md      # 出力前チェックリスト
```

## 特徴

### HIG 20原則

- **Phase 1**: 全アプリ必須の基本原則（7項目）
- **Phase 2**: フォーム・入力UIの原則（8項目）
- **Phase 3**: UX向上の原則（5項目）

### 6種類のテーマ

ライト、ダーク、オーシャン、フォレスト、サンセット、サクラ

### GAS制約対応

- 非同期処理の遅延対策
- 処理中断不可への対応
- 取り消し不可操作の論理削除実装

## 出力ファイル

- **コード.gs**: doGet関数 + サーバーサイド処理
- **Index.html**: HTML/CSS/JS統合ファイル

## クレジット

### Original

- **プロンプト**: [gas-webapp-prompt-hig.md](https://github.com/akari-iku/gas-webapp-prompt/blob/main/prompt/gas-webapp-prompt-hig.md)
- **著者**: Akari ([akari-iku](https://github.com/akari-iku))

### License

MIT License

このスキルは上記プロンプトをベースに、AIツール向けに最適化（500行ルール適用、references分離）したものです。
