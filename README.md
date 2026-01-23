# Orchestrate-It: AI Skills共有リポジトリ

「AIオーケストレーションの極意」講座の参加者が作成したSkillsを共有するリポジトリです。

## このリポジトリでできること

1. **サンプルを試す** - 講師が用意したSkills/Rules/Workflowsを自分の環境に導入
2. **講師提供スキルを使う** - 実践的なスキル（サイトマップ&検索など）を導入
3. **自分のSkillを作る** - テンプレートを使ってオリジナルSkillを作成
4. **共有する** - Pull Requestで他の参加者と共有
5. **他の人のSkillを使う** - 参加者が作ったSkillを自分の環境に導入

---

## 講師提供スキル（実践的なスキル集）

講師が作成した、すぐに使える実践的なスキルです。
**複数のAIコードエディタに対応**しています。

| スキル名 | 説明 |
|---------|------|
| **sitemap-search** | サイトマップページ&サイト内検索機能を実装 |

### 対応プラットフォーム

| プラットフォーム | 導入方法 |
|----------------|---------|
| **Google Antigravity** | チャットでURL指定 |
| **Claude Code** | `.claude/skills/` にコピー |
| **Cursor** | `.cursor/rules/` にコピー |

詳細は [instructor-skills/README.md](instructor-skills/README.md) を参照。

---

## 概念の違い：Skills / Rules / Workflows

| 概念 | 役割 | 発動タイミング | 例 |
|------|------|---------------|-----|
| **Skills** | 特定タスクの専門知識 | AIが自動判断 | 「指導案を作って」→ 自動起動 |
| **Rules** | 常に守るべきルール | 常時適用 | 「日本語で回答」「絵文字禁止」 |
| **Workflows** | 複数ステップの自動化 | 明示的に呼び出し | `/deploy` でテスト→ビルド→公開 |

### フォルダ構成（Google Antigravity）

```
プロジェクト/
├── .agent/
│   ├── skills/          # Skills（自動起動する専門知識）
│   │   └── lesson-plan/
│   │       └── SKILL.md
│   ├── rules/           # Rules（常時適用ルール）
│   │   └── coding-style.md
│   └── workflows/       # Workflows（手動で呼び出す自動化）
│       └── deploy.md
└── GEMINI.md            # プロジェクト全体の設定
```

---

## Skillsの導入方法

### Step 1: Antigravityで導入

Antigravityのチャットで以下のように伝えるだけ：

```
このリポジトリのskillを導入して
https://github.com/School-Agent-Inc/orchestrate-it/tree/main/.agent/skills/lesson-plan
```

### Step 2: 動作確認

導入後、以下のように話しかけてSkillが動作するか確認：

```
指導案を作って
```

---

## スキル作成ガイド（Skill Creator）

Anthropicが公開している[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)をベースにした、スキル作成のベストプラクティスを提供しています。

**詳細:** [docs/SKILL-CREATOR.md](docs/SKILL-CREATOR.md)

### 核心原則

1. **コンテキストは公共財** - 必要最小限の情報のみを含める
2. **500行以下のSKILL.md** - 長すぎるスキルは分割
3. **明確なdescription** - `Use when:` でトリガー条件を明記

### グローバルスキルとして導入

どのフォルダを開いても使えるようにするには：

| プラットフォーム | 配置先 |
|----------------|--------|
| Claude Code | `~/.claude/skills/` |
| Antigravity | `~/.gemini/antigravity/skills/` |
| Cursor | `~/.cursor/rules/` |

---

## 自分のSkillを作って共有する

### Step 1: リポジトリをフォーク

1. このページ右上の「Fork」ボタンをクリック
2. 自分のアカウントにリポジトリがコピーされる

### Step 2: Skillを作成

1. `submissions/あなたのGitHub名/` フォルダを作成
2. その中に `スキル名/SKILL.md` を作成
3. [テンプレート](templates/SKILL-TEMPLATE.md) を参考に記述

```
submissions/
└── your-github-id/
    └── my-awesome-skill/
        └── SKILL.md
```

### Step 3: Pull Requestを作成

1. 変更をコミット・プッシュ
2. GitHub上で「Pull Request」を作成
3. レビュー後、マージされます！

---

## リポジトリ構成

```
orchestrate-it/
├── README.md                    # このファイル
├── .agent/                      # サンプル（Antigravity形式）
│   ├── skills/                  # サンプルSkills
│   │   ├── lesson-plan/         # 指導案作成Skill
│   │   ├── report-comment/      # 通知表コメントSkill
│   │   └── parent-letter/       # 保護者向けお便りSkill
│   ├── rules/                   # サンプルRules
│   │   ├── teaching-style.md    # 教育者向けルール
│   │   └── output-format.md     # 出力フォーマットルール
│   └── workflows/               # サンプルWorkflows
│       ├── material-create.md   # 教材作成ワークフロー
│       └── weekly-report.md     # 週報作成ワークフロー
├── instructor-skills/           # 講師提供スキル（プラットフォーム別）
│   ├── antigravity/             # Google Antigravity用
│   │   └── sitemap-search/
│   ├── claude-code/             # Claude Code用
│   │   └── sitemap-search/
│   └── cursor/                  # Cursor用
│       └── sitemap-search/
├── submissions/                 # 参加者の提出場所
│   └── examples/                # 提出例
│       └── sample-user/
│           └── greeting-skill/
│               └── SKILL.md
└── templates/                   # テンプレート
    ├── SKILL-TEMPLATE.md        # Skill作成用テンプレート
    ├── RULES-TEMPLATE.md        # Rules作成用テンプレート
    └── WORKFLOW-TEMPLATE.md     # Workflow作成用テンプレート
```

---

## よくある質問

### Q: Skillが動かない
**A:** `description` に `Use when:` を含めていますか？AIはこの記述を見て、いつSkillを使うか判断します。

### Q: 複数のSkillを導入したい
**A:** 1つずつ導入してください。または、フォルダごと導入することも可能です：
```
このリポジトリの.agent/skillsフォルダを全て導入して
https://github.com/School-Agent-Inc/orchestrate-it/tree/main/.agent/skills
```

### Q: Rulesも導入したい
**A:** 同様にURLを指定して導入できます：
```
このリポジトリのrulesを導入して
https://github.com/School-Agent-Inc/orchestrate-it/tree/main/.agent/rules
```

---

## ライセンス

MIT License - 自由に使用・改変・再配布できます。

---

## 講座情報

**AIオーケストレーションの極意** - 先生のための新しい仕事術

- 主催: スクールエージェント株式会社
