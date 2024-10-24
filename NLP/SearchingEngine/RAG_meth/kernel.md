---
layout: default
title: kernel packages
parent: RAG Methodologies
grand_parent: SearchingEngine
nav_order: 99
date: 2024-10-12 
last_modified_date: 2024-10-12 20:32:31
tags: AI chat report
---

# kernel packages

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


## langchain/langGraph

- [知勢2024/06](https://edge.aif.tw/application-langchain-rag-advanced/amp/)
- [medium](https://lazypro.medium.com/%E5%81%9A%E4%B8%80%E5%80%8B%E5%8B%99%E5%AF%A6%E7%9A%84rag-pragmatic-rag-65fc63647c51)
要讓 RAG 務實有以下幾個重點：
必須是要懂繁體中文的 embedding
要有中文語意的分片器
一定要是用繁體中文訓練的 LLM
精準的 prompt 連同 system instruction
沒做 rerank 的效果都差到不行，但 rerank 要懂繁體中文

## llmware

-［Github](https://llmware-ai.github.io/llmware/)
  - [官網](https://llmware.ai/)
  - [中文推薦](https://codelove.tw/@tony/post/gqvJ2q)

LLMWare.ai 是一個專門為 LLM（大型語言模型）構建的開源平台，提供 RAG 服務。該平台專注於將語言模型與各類資料來源整合，支持企業用來構建可擴展且高效的生成應用。它提供向量數據庫整合、API 架構、內建快取等功能，並能夠支援多種部署環境如 Kubernetes。這使其成為 RAG 領域中的一個重要玩家，適合需要大規模語言模型應用的企業。

你可以查看 LLMWare.ai 了解更多。