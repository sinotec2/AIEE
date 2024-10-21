---
layout: default
title: Network Inference Modules
parent: RAG Methodologies
grand_parent: SearchingEngine
nav_order: 99
date: 2024-10-12 
last_modified_date: 2024-10-12 20:32:31
tags: AI chat report
---

# NIM 的應用
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

- [Haystack  AI Eco](https://haystack.deepset.ai/blog/haystack-nvidia-nim-rag-guide)
  - Haystack AI 是一個開源的問答和檢索增強生成 (RAG) 框架，專注於構建以語言模型為基礎的應用。它支援文檔搜尋、問答系統和對話 AI 的構建，並與向量數據庫（如 Elasticsearch 和 FAISS）整合，以進行高效的相似性搜索。Haystack 支援多種後端模型（如 Hugging Face、OpenAI），以及部署在 Kubernetes 和 Docker 上，適合建立靈活且可擴展的檢索生成系統。
  - 該網址介紹了如何使用 Haystack 和 NVIDIA NGC 設置 RAG（Retrieval-Augmented Generation）服務。步驟包括在 Kubernetes 上運行 Haystack，並整合 NVIDIA NGC 的模型和資源來進行高效的推理與檢索。
  - 重點涵蓋了如何將向量資料庫（如 FAISS 或 Elasticsearch）與語言模型整合，實現實時數據檢索和生成。
  - 該指南還展示了如何優化 GPU 資源和配置 Kubernetes 節點來支持大規模的 RAG 應用。

## 費用

- [IThome](https://www.ithome.com.tw/news/164187)
- 
[ngc]: "NGC 是 NVIDIA GPU Cloud 的縮寫，它是 NVIDIA 提供的一個專門針對 AI、機器學習、數據分析和高性能計算的雲端平台。NGC 提供了一個容器化的環境，內含各種經過優化的深度學習框架、預訓練模型、應用程式和工具，能夠快速部署在各種環境中，如本地伺服器、雲端或超級計算機。"
使用者可以透過 NGC 來訪問 NVIDIA 認證的軟體堆疊，並在其雲端平台上進行訓練、推理及分析工作，提升開發效率並確保軟體的穩定性和性能。"