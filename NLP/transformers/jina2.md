---
layout: default
title: jina2
parent: 轉換器transformers
grand_parent: 自然語言處理
nav_order: 99
date: 2023-09-05
last_modified_date: 2023-09-05 13:44:37
tags: AI chat
---


# jina-embeddings-v2
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

- [](https://www.marktechpost.com/2023/11/01/jina-ai-introduces-jina-embeddings-v2-the-worlds-first-8k-open-source-text-embedding-models/)
  - 這篇文章是關於Jina AI推出其第二代文本嵌入模型jina-embeddings-v2的最新進展。
  - 該模型支持8K（8192個標記）的上下文長度，與OpenAI的專有模型text-embedding-ada-002在功能和在Massive Text Embedding Benchmark（MTEB）排行榜上的表現相當。
  - 該模型在各種應用領域中展示了卓越的性能，包括法律文件分析、醫學研究、文學分析、金融預測和對話式人工智能等。此外，Jina AI還計劃發布一篇學術論文，詳細介紹jina-embeddings-v2的技術細節和基準測試結果，並正在開發類似於OpenAI的嵌入API平台。
  - 目前Jina AI正在擴展其語言能力，計劃推出德語-英語模型。
- [jinaai/jina-embeddings-v2-base-en](https://huggingface.co/jinaai/jina-embeddings-v2-base-en)
  - 本網頁介紹了 jina-embeddings-v2-base-en，這是由 Jina AI 訓練的文本嵌入集，用於序列長度不超過 8192 的英語單語文檔。
  - 該模型基於 Bert 架構 （JinaBert），該架構支援 ALiBi 的對稱雙向變體，以允許更長的序列長度。該模型在 C4 數據集上進行了預訓練，並在 Jina AI 收集的 4 億多個句子對和硬否定詞上進行了進一步訓練。
  - 該模型可實現 1.37 億 p 的快速推理
  - 該模型能夠使用1.37 億個參數進行快速推理，並在各種用例中提供比小型模型更好的性能，例如長文檔檢索、語義文本相似性、文本重排序、推薦、RAG 和基於LLM 的生成搜索等等。
  - 該網頁還提供較短序列長度（最多 2048）的嵌入模型和用於對 Jina Embeddings 模型進行完全託管訪問的嵌入平台。 此外，該網頁還宣布開發了德語和西班牙語的新雙語模型，並引用了描述該模型及其評估的論文。