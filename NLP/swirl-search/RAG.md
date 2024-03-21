---
layout: default
title: 檢索強化生成RAG
parent: swirl搜尋引擎
grand_parent: 自然語言處理
nav_order: 99
date: 2023-11-13
last_modified_date: 2023-11-13 19:18:56
has_children: true
tags: AI chat report
---

# RAG檢索強化生成
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>
---

## 背景

**Retrieved Augmented Generation (RAG)** 是一種結合檢索和生成的自然語言處理方法。讓我們來深入了解一下：

1. **檢索（Retrieval）**：
    - 在檢索階段，系統從大量的文本數據中選擇相關的文本片段或段落。這些文本片段通常是與用戶的查詢相關的。
    - 檢索可以使用不同的技術，例如基於關鍵詞的檢索、向量空間模型、BM25 等。這些方法有助於從文本庫中快速找到相關的內容。

2. **生成（Generation）**：
    - 在生成階段，系統使用檢索到的文本片段作為上下文，並生成一個完整的回答或文本。
    - 生成可以使用不同的技術，例如循環神經網絡（RNN）、Transformer 模型等。這些模型可以根據上下文生成自然語言文本。

3. **增強（Augmentation）**：
    - RAG 方法的增強部分在於它允許生成的文本與檢索到的文本進行交互。
    - 生成的文本可以通過添加、修改或擴展檢索到的文本來進行增強。這有助於生成更具信息量和多樣性的回答。

總之，RAG 方法通常用於搜索引擎、問答系統和其他需要生成自然語言文本的應用中。它結合了檢索的速度和生成的靈活性，以提供更好的用戶體驗。

[一文搞懂大模型RAG应用（附实践案例）](https://zhuanlan.zhihu.com/p/668082024?ssp=1&setlang=zh-hant&cc=TW&safesearch=moderate&utm_id=0)
