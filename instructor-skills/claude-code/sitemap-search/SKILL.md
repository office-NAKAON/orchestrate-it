---
name: sitemap-search
description: "Webサイトのサイトマップページとサイト内検索機能を実装する。サイトマップ、サイト内検索、ページ一覧、ナビゲーション、検索機能を追加したい時に使用。"
user-invocable: true
argument-hint: "[framework: react|next|vanilla] [--tags] [--keyboard]"
---

# サイトマップ & サイト内検索機能スキル

Webサイトにサイトマップページとサイト内検索機能を実装するスキルです。

## 対応タスク

1. サイトマップページの作成
2. サイト内検索機能（モーダル + リアルタイム検索）
3. タグ・カテゴリによるフィルタリング
4. キーボードショートカット（Cmd/Ctrl + K）
5. 検索結果ハイライト表示

## 実装フロー

### Step 1: サイト構造の把握

まず、プロジェクトのページ構造を調査します：

```bash
# Next.js App Router
find src/app -name "page.tsx" | head -50

# Next.js Pages Router
find src/pages -name "*.tsx" | head -50

# 静的サイト
find . -name "*.html" | head -50
```

### Step 2: 検索データの生成

ページ情報を収集してsearchDataを生成：

```typescript
// types/search.ts
interface SearchItem {
  title: string;
  description: string;
  url: string;
  icon?: string;
  category: string;
  keywords: string[];
  tags?: string[];
}

// data/search-data.ts
export const searchData: SearchItem[] = [
  {
    title: "はじめに",
    description: "プロジェクトの概要と使い方",
    url: "/getting-started",
    icon: "rocket",
    category: "ドキュメント",
    keywords: ["開始", "スタート", "入門", "初心者"],
    tags: ["入門", "必読"]
  },
  // ...
];
```

### Step 3: 検索コンポーネントの実装

#### React/Next.js版

```tsx
// components/SearchModal.tsx
'use client';

import { useState, useEffect, useCallback, useRef } from 'react';
import { searchData, SearchItem } from '@/data/search-data';

export function SearchModal() {
  const [isOpen, setIsOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchItem[]>([]);
  const [selectedIndex, setSelectedIndex] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);

  // Cmd/Ctrl + K でモーダルを開く
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setIsOpen(true);
      }
      if (e.key === 'Escape') {
        setIsOpen(false);
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, []);

  // モーダルが開いたらフォーカス
  useEffect(() => {
    if (isOpen && inputRef.current) {
      inputRef.current.focus();
    }
  }, [isOpen]);

  // 検索ロジック
  const search = useCallback((q: string) => {
    if (!q.trim()) {
      setResults([]);
      return;
    }

    const normalized = q.toLowerCase();
    const scored = searchData
      .map(item => {
        let score = 0;
        if (item.title.toLowerCase() === normalized) score += 100;
        else if (item.title.toLowerCase().startsWith(normalized)) score += 80;
        else if (item.title.toLowerCase().includes(normalized)) score += 60;
        if (item.description.toLowerCase().includes(normalized)) score += 40;
        if (item.keywords.some(kw => kw.toLowerCase().includes(normalized))) score += 50;
        return { ...item, score };
      })
      .filter(item => item.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 10);

    setResults(scored);
    setSelectedIndex(0);
  }, []);

  // クエリ変更時に検索
  useEffect(() => {
    search(query);
  }, [query, search]);

  // キーボードナビゲーション
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setSelectedIndex(i => Math.min(i + 1, results.length - 1));
    }
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      setSelectedIndex(i => Math.max(i - 1, 0));
    }
    if (e.key === 'Enter' && results[selectedIndex]) {
      window.location.href = results[selectedIndex].url;
    }
  };

  // ハイライト表示
  const highlight = (text: string, q: string) => {
    if (!q) return text;
    const regex = new RegExp(`(${q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    return text.replace(regex, '<mark class="bg-yellow-200 dark:bg-yellow-800">$1</mark>');
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 bg-black/50" onClick={() => setIsOpen(false)}>
      <div
        className="mx-auto mt-20 max-w-xl bg-white dark:bg-neutral-900 rounded-xl shadow-2xl overflow-hidden"
        onClick={e => e.stopPropagation()}
      >
        <div className="flex items-center gap-3 p-4 border-b dark:border-neutral-700">
          <svg className="w-5 h-5 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={e => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="ページを検索..."
            className="flex-1 bg-transparent outline-none"
          />
          <kbd className="px-2 py-1 text-xs bg-neutral-100 dark:bg-neutral-800 rounded">ESC</kbd>
        </div>

        <div className="max-h-80 overflow-y-auto">
          {results.length === 0 && query && (
            <div className="p-4 text-center text-neutral-500">
              「{query}」に一致するページが見つかりません
            </div>
          )}
          {results.map((item, i) => (
            <a
              key={item.url}
              href={item.url}
              className={`flex items-start gap-3 p-4 hover:bg-neutral-100 dark:hover:bg-neutral-800 ${
                i === selectedIndex ? 'bg-neutral-100 dark:bg-neutral-800' : ''
              }`}
            >
              <span className="text-2xl">{item.icon || '📄'}</span>
              <div className="flex-1">
                <div
                  className="font-medium"
                  dangerouslySetInnerHTML={{ __html: highlight(item.title, query) }}
                />
                <div
                  className="text-sm text-neutral-500"
                  dangerouslySetInnerHTML={{ __html: highlight(item.description, query) }}
                />
                <div className="flex gap-2 mt-1">
                  <span className="text-xs px-2 py-0.5 bg-neutral-200 dark:bg-neutral-700 rounded">
                    {item.category}
                  </span>
                </div>
              </div>
            </a>
          ))}
        </div>
      </div>
    </div>
  );
}
```

### Step 4: サイトマップページの実装

```tsx
// app/sitemap/page.tsx
import { searchData } from '@/data/search-data';

export default function SitemapPage() {
  // カテゴリでグループ化
  const grouped = searchData.reduce((acc, item) => {
    if (!acc[item.category]) acc[item.category] = [];
    acc[item.category].push(item);
    return acc;
  }, {} as Record<string, typeof searchData>);

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">サイトマップ</h1>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {Object.entries(grouped).map(([category, items]) => (
          <section
            key={category}
            className="bg-white dark:bg-neutral-900 rounded-xl p-6 shadow-sm"
          >
            <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <span>📁</span>
              {category}
            </h2>
            <ul className="space-y-2">
              {items.map((item, i) => (
                <li key={item.url}>
                  <a
                    href={item.url}
                    className="flex items-start gap-3 p-2 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-800 transition"
                  >
                    <span className="min-w-[28px] h-7 flex items-center justify-center bg-blue-500 text-white text-sm font-medium rounded">
                      {i + 1}
                    </span>
                    <div>
                      <div className="font-medium">{item.title}</div>
                      <div className="text-sm text-neutral-500">{item.description}</div>
                    </div>
                  </a>
                </li>
              ))}
            </ul>
          </section>
        ))}
      </div>
    </div>
  );
}
```

## ファイル構成

```
src/
├── components/
│   ├── SearchModal.tsx      # 検索モーダル
│   ├── SearchButton.tsx     # 検索ボタン（ナビゲーション用）
│   └── TagFilter.tsx        # タグフィルター（オプション）
├── data/
│   └── search-data.ts       # 検索データ
├── types/
│   └── search.ts            # 型定義
└── app/
    └── sitemap/
        └── page.tsx         # サイトマップページ
```

## バニラJS版

静的サイト向けの実装は`references/vanilla-js.md`を参照してください。

## ルール

- 検索データは静的に管理（ビルド時生成も可）
- キーボードショートカットは `Cmd/Ctrl + K` を標準
- アクセシビリティ：モーダルにはfocus trapを実装
- パフォーマンス：検索はクライアントサイドで完結
- SEO：サイトマップページは静的に生成
- 日本語対応：IME入力（compositionstart/end）を考慮

## ヒアリング項目

実装前に確認：

1. フレームワークは？（Next.js / React / バニラJS）
2. スタイリングは？（Tailwind / CSS Modules / vanilla CSS）
3. ページ数は？（検索データの規模）
4. タグ・カテゴリ機能は必要？
5. ダークモード対応は必要？

---

## UXベストプラクティス

### 検索UX

- 検索ボックス幅: 27文字以上（90%のクエリをカバー）
- サジェスト数: 10件以下（スクロールなし）
- Spotlight風: 現在画面上にオーバーレイ表示
- 背景ぼかし: `backdrop-filter: blur(4px)` で集中を促す

### アクセシビリティ（ARIA）

```tsx
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="search-title"
>
  <h2 id="search-title" className="sr-only">サイト内検索</h2>
  {/* ... */}
</div>
```

### フォーカストラップ

```typescript
// react-focus-lockを使用（推奨）
import FocusLock from 'react-focus-lock';

<FocusLock>
  <div className="search-modal">...</div>
</FocusLock>
```

### パフォーマンス

| ページ数 | 推奨アプローチ |
|---------|---------------|
| ~100 | クライアントサイド（このスキル） |
| 100-1000 | Fuse.js + インデックス |
| 1000+ | Algolia / Meilisearch |

### デバウンス

```typescript
import { useDeferredValue } from 'react';

// React 18+: useDeferredValueで自動デバウンス
const deferredQuery = useDeferredValue(query);

useEffect(() => {
  search(deferredQuery);
}, [deferredQuery]);
```
