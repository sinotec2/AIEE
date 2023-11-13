---
layout: default
title: processors/rag.py
nav_order: 99
layout: default
grand_parent: swirl搜尋引擎
parent: swirl
date: 2023-11-09
last_modified_date: 2023-11-09 09:45:06
tags: AI chat report
---


# rag.py

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

- 程式位置：[swirl/processors/rag.py](./rag.py)
- 本程式受到`swirl/consumer.py`的呼叫。輸入參數包括
  - `search_id`、
  - `request_id`，以及
  - 是否為socket邏輯(`is_socket_logic`)和
  - RAG（檢索增強生成）查詢項目的標誌(`rag_query_items`)

## 程式說明

## RAGPostResultProcessor

這段Python代碼定義了一個名為`RAGPostResultProcessor`的類，它是`PostResultProcessor`的一種。該類旨在處理搜索結果的輸出，並進行額外的處理，特別是與OpenAI的ChatGPT集成，用於生成摘要或提取信息。以下是該類中主要組件和功能的說明：

- `__init__`：構造方法用於初始化類所需的參數，如`search_id`、`request_id`，以及是否為socket邏輯和RAG（檢索增強生成）查詢項目的標誌。

- `_log_n_store_warn`：一個輔助方法，用於記錄警告並將它們存儲在緩衝區中。

- `stop_processing`：設置一個標誌，指示應停止後台處理。

- `background_process`：此方法處理搜索結果，以提取與ChatGPT生成響應的相關內容。它根據得分和日期等標準對結果進行篩選和排名，然後使用最相關的內容為ChatGPT創建**提示**。

- `is_valid_url`, `find_substrings`：用於URL驗證和在字符串中查找子串的實用程序函數。

- `clean_string_keep_punct`：在保留標點符號的同時清理字符串的實用程序函數。

- `create_result_dictionary`：創建搜索結果的字典結構的實用程序函數。

- `process`：這個方法是處理的主入口。它設置了ChatGPT API，準備了**提示**，並根據從搜索結果收集的內容([background_process](#background_process))呼叫ChatGPT來生成回應。說明[詳下](#process)。

- `MODEL_3`, `MODEL_4`, `MODEL`：定義使用哪個OpenAI模型的常量。

- `MODEL_TOK_MAX`：模型能夠處理的最大令牌數。

- `MODEL_DEFAULT_SYSTEM_GUIDE`：ChatGPT系統的預設指導消息。

- `FETCH_TO_SECS`, `DO_MESSAGE_MOCK_ON_ERROR`, `MESSAGE_MOCK_ON_ERROR`：與抓取超時和錯誤處理相關的常量。

- `logger`：一個用於記錄消息的日誌實例。

- `RagPrompt`：一個類（在[別處](../rag_prompt.md)定義），它協助根據搜索結果為ChatGPT創建提示。

`RAGPostResultProcessor`旨在通過將搜索結果與語言模型集成來增強搜索結果，這可以潛在地總結信息或基於結果內容回答問題。該類處理頁面抓取、內容處理，並與OpenAI API進行交互，以產生連貫且相關的輸出。後台線程允許異步處理，這樣在等待API響應時不會阻塞主執行流程。

## background_process

這個background_process方法是RAG查詢的具體執行過程:

### 主要邏輯

1. 從已有的查詢結果中過濾出符合rag_query_items的內容

2. 如果沒有結果,返回0

3.呼叫[RagPrompt](../rag_prompt.md)構建RAG prompt,循環調用page_fetcher_task組件來獲取內容

4. 清理內容,新增到prompt中,檢查是否達到最大token數

5. 如果prompt太短,使用預設的fallback內容

6. 調用OpenAI API生成回復內容

7. 封裝結果並保存到資料庫

8. 返回結果對象

### 特殊情況處理

- API調用失敗時,返回預設內容或0

- 內容獲取失敗時,記錄日志並繼續程序

### 限制和需注意

- 依賴外部組件page_fetcher_task

- prompt內容過長會影響效果

- 需要處理內容清理去重等問題

- 返回類型和值需統一

總體上這個方法將RAG查詢的複雜邏輯封裝起來了。

## process

這是[RAGPostResultProcessor](#ragpostresultprocessor)類中的process方法,用於啟動RAG查詢過程。

### 輸入參數

- should_return: 是否直接返回查詢結果，如為否，則使用多線程。

### 邏輯步驟

1. 打印日誌記錄查詢開始
2. 從設定中獲取OpenAI的API key
3. 判斷should_return的值
   3.1 如果為True,直接調用[background_process](#background_process)執行查詢並返回結果
   3.2 如果為False,啟動新的線程執行[background_process](#background_process),主線程返回1
4. [background_process](#background_process)會發起API請求獲取RAG查詢結果

### 限制和注意事項

- 需要先在設定中配置OpenAI的API key
- [background_process](#background_process)方法如前所述，是查詢的具體邏輯
- 多線程情況下需要處理線程同步和競爭問題
- 返回值類型不統一,0和1容易混淆

總體來說,這個process方法实现了异步或同步兩種模式啟動RAG查詢的功能。