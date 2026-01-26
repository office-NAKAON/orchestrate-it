# Web Builder Skill

高品質なNext.js/React Webサイトを構築するためのスキルです。

## 概要

awwwards.comに掲載されるレベルの、エレガントで洗練されたWebサイト・Webアプリを構築します。

## 特徴

- **Next.js App Router対応**: 最新のNext.js構成
- **レスポンシブデザイン**: モバイル・タブレット・デスクトップ完全対応
- **ダークモード対応**: ライト/ダーク切り替え機能
- **ページ遷移アニメーション**: Reveal/Cover の滑らかな遷移
- **プロンプトUI**: クリックコピー機能付きカード
- **ドロワーメニュー**: モバイル対応ナビゲーション

## 使い方

### Claude Code
```bash
# .claude/skills/ にコピー
cp -r web-builder ~/.claude/skills/
```

### トリガーワード

以下のようなプロンプトでスキルが起動します：

- 「Webサイトを作って」
- 「Next.jsでポートフォリオを作成」
- 「ランディングページを構築して」
- 「Reactでダッシュボードを作って」

## ファイル構成

```
web-builder/
├── SKILL.md              # スキル定義（メイン）
├── README.md             # このファイル
└── references/
    ├── design-system.md  # デザインシステム詳細
    ├── animations.md     # アニメーション実装パターン
    └── components.md     # 共通コンポーネント
```

## 作者

講師作成のサンプルスキルです。

## ライセンス

MIT
