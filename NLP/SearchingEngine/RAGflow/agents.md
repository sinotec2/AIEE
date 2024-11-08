---
layout: default
title: 代理與流程編輯器
parent: RAGflow
grand_parent: SearchingEngine
nav_order: 99
date: 2024-10-30 
last_modified_date: 2024-10-30 20:32:31
tags: AI chat report
---

# 代理與流程
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

- RAGFlow 的代理機制將 RAG 技術與無代碼工作流程編輯器結合，適合複雜商業應用場景。透過代理，使用者可利用查詢分類、對話導向等功能，從知識庫中進行檢索並生成回應。可選擇現有模板或自行設定代理，並透過元件如檢索、生成、分類等來自訂工作流程。每個元件有特定的配置要求，確保流程運行順暢，且支持基礎操作如添加、複製和刪除元件。
- 更多詳情請參閱：[RAGFlow 官方文件](https://ragflow.io/docs/dev/agent_introduction)

### 元件

| 元件         | 說明                                                                                                                             |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| 檢索 (Retrieval) | 從指定的知識庫檢索資訊，若無資訊則返回「空回應」。確保已選擇正確的知識庫。                                       |
| 生成 (Generate) | 讓 LLM 生成回應的元件，必須確保提示設置正確。                                            |
| 互動 (Interact) | 作為人類與機器人之間的介面，接收用戶輸入並顯示代理的回應。                                  |
| 分類 (Categorize) | 使用 LLM 將用戶輸入分類到預定的類別中，需設定每個類別的名稱、描述和示例，以及相應的下一步元件。 |
| 訊息 (Message) | 發送靜態訊息，若提供多條訊息則隨機選擇一條發送。確保下游為介面元件 Interact。               |
| 關聯 (Relevant) | 使用 LLM 判斷上游輸出與用戶查詢的相關性，並根據判斷結果指定下一步元件。                       |
| 重寫 (Rewrite) | 若查詢未檢索到相關資訊，則重新修訂查詢，直到達到預定次數上限。上游需為 Relevant，下游為 Retrieval。|
| 關鍵字 (Keyword) | 從 Wikipedia 檢索前 N 筆結果，使用前需正確設置 TopN 值。                                  |

