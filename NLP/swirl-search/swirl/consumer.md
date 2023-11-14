---
layout: default
title: consumers.py
nav_order: 99
layout: default
grand_parent: swirl搜尋引擎
parent: swirl
date: 2023-11-04
last_modified_date: 2023-11-04 20:37:49
tags: AI chat report
---


# consumers.py

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

- 這支程式會在`swirl_server/routing.py`([source](../swirl_server/routing.py))中被`django`的`path`函式呼叫，以展開asgi通道服務(ASGI, Asynchronous Server Gateway Interface)。
- 有關`AsyncWebsocketConsumer`的說明，可以參考`django`的[官網](https://channels.readthedocs.io/en/latest/topics/consumers.html)。

## 程式說明

這段Python代碼([consumer.py](./consumers.py))實現了一個基於Django Channels的異步[WebSocket](../static/api_config_default.md#websocket)消費者，名為`Consumer`。WebSocket消費者用於管理前端與後端之間的WebSocket連接，這裡是為了實現即時的數據通信。以下是代碼的主要功能和元件：

1. `connect`: 當客戶端嘗試與WebSocket建立連接時，這個異步方法被調用。它檢查用戶是否通過身份驗證和搜索ID是否存在。如果不符合條件，它將關閉連接。

2. `get_rag_result`: 這是一個裝飾為異步的同步數據庫查詢方法。它嘗試從數據庫中獲取特定的`Result`對象，該對象與提供的`search_id`相關聯，並檢查是否需要更新結果。

3. `process_rag`: 這個異步方法處理接收到的查詢，通過調用`get_rag_result`方法獲取結果並將其發送回客戶端。

4. `stop_rag_processor`: 此方法用於停止正在執行的查詢處理，如果有任何背景任務正在運行，它將撤銷它們。

5. `receive`: 當從客戶端接收到消息時，這個異步方法被調用。它解析接收到的數據，根據消息的內容處理請求。

6. `instances`: 這是一個字典，用於存儲正在處理查詢的實例。

這段代碼顯示了如何在Django應用中使用Channels和Celery來處理非同步任務，特別是在需要即時通信時。它結合了WebSocket技術來推送實時數據和數據庫異步查詢，這對於構建動態和響應式Web應用非常有用。

## get_rag_result

這個程式的主要功能是獲取 RAG(Retrieve and Gather) 查詢的結果。

### 輸入參數

- search_id: 查詢的ID
- rag_query_items: RAG查詢中的關鍵詞項目

### 輸出

- RAG查詢的結果內容,儲存在json格式中

### 主要邏輯

1. 嘗試從資料庫的Result表中獲取search_id對應的RAG查詢結果
2. 判斷rag_query_items是否更新了,如果更新就需要重新查詢
3. 如果資料庫中沒有結果,或者查詢條件更新了,就創建`RAGPostResultProcessor`實例進行查詢
4. 調用`RAGPostResultProcessor`的`process`方法發起查詢
5. 從返回的結果中解析出body字段作為最終輸出
6. 刪除no longer需要的實例對象
7. 如果任何异常,返回False

### 特殊情況處理

- 捕獲各種異常,防止程式中斷

### 限制和注意事項

- 依賴外部`RAGPostResultProcessor`組件處理查詢(在[rag.py](../swirl/processors/rag.md)中)
- 需要確保search_id不重複衝突
- rag_query_items的數據類型要一致,才能比較是否更新