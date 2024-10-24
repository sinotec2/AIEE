---
layout: default
title: K8s 的應用
parent: RAG Methodologies
grand_parent: SearchingEngine
nav_order: 99
date: 2024-10-12 
last_modified_date: 2024-10-12 20:32:31
tags: AI chat report
---

# K8s 的應用
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

## 訓練階段7500個節點

- [openAI,2021](https://juejin.cn/post/7255230505409429559)

本文討論了 OpenAI 如何擴展其 Kubernetes 基礎設施以支援 7,500 個節點，重點是優化資源調度、網路管理和 API 伺服器。解決的主要挑戰包括 GPU 資源分配、並行作業的群組調度、高效檢查點、網路效能和 API 伺服器負載管理。他們使用 Azure 的 VMSS 等工具進行擴展，使用 Kubernetes 1.16 的 EndpointSlices 來提高效能，並解決了 Prometheus 監控問題。總的來說，Kubernetes 被證明是一個可擴展且靈活的平台，用於管理 GPT-3 和 DALL·E 等大型 AI 模型。

![](https://openai.com/index/scaling-kubernetes-to-7500-nodes/#unsolvedproblems%E3%80%82)
## 推論階段可服務人數

在 Kubernetes (K8S) 中部署 GPU 推理服務時，每個節點能夠服務的使用者數量取決於多個因素，包括 GPU 的規格、模型的複雜性、推理的時間要求以及使用者的並發需求。以下是影響 GPU 推理服務能力的幾個關鍵因素：

	1.	GPU 性能：高性能的 GPU（如 NVIDIA A100 或 V100）能夠處理更多的推理請求。相較於入門級 GPU（如 T4 或 GTX 系列），這些高端 GPU 擁有更多 CUDA 核心、內存和加速能力，能夠更好地支持大規模並發請求。
	2.	模型大小與複雜性：較大的模型（如 GPT-3、BERT 這類生成式模型）需要更多的計算資源。相比之下，較小的模型（如 ResNet）對 GPU 資源的要求較低。因此，複雜的模型會降低單一 GPU 能夠同時處理的請求數量。
	3.	推理延遲與吞吐量要求：如果應用需要實時回應（如聊天機器人或即時推薦系統），那麼每個使用者的推理請求需要佔用更多的資源。如果允許較高的延遲或批處理推理，則可以增加服務的使用者數量。
	4.	並發用戶量：對於需要低延遲響應的場景，可能每個 GPU 同時僅能支持 5 到 10 個並發請求；而對於批次推理的應用場景，這個數量可能會增加。
	5.	K8S 節點配置：Kubernetes 節點上的資源分配方式（如 GPU 資源分片）也會影響每個 GPU 能夠同時服務的請求數量。K8S 允許將 GPU 資源分配給不同的 Pod，因此你可以將 GPU 資源共享給多個容器，這樣能夠有效提升服務多個用戶的能力。

大約服務人數範圍：
在典型的商業應用中，使用高端 GPU（如 NVIDIA A100），每個 GPU 在低延遲要求下可同時處理 5-10 個使用者的推理請求。如果應用允許較高延遲或批量處理，這一數字可以提升到數十甚至上百個使用者。

