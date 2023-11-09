---
layout: default
title: chatgpt.py
nav_order: 99
layout: default
grand_parent: swirl搜尋引擎
parent: swirl
date: 2023-11-09
last_modified_date: 2023-11-09 09:45:06
tags: AI chat report
---


# chatgpt.py


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

- 程式位置：[swirl/connectors/chatgpt.py](./chatgpt.py)

## 程式說明

這段程式碼是一個名為 `ChatGPT` 的 Python 類別，負責與 OpenAI 的 GPT-3 或 GPT-4 模型進行交互來處理查詢。以下是重點函數及其用途、參數和輸出的概述：

### 類別 ChatGPT

- **__init__(self, provider_id, search_id, update, request_id=''):**
  - **用途：** 初始化 ChatGPT 類別的一個實例。
  - **參數：**
    - `provider_id`：提供者的ID。
    - `search_id`：搜索的ID。
    - `update`：更新標誌，可能用於指定是否需要更新搜索結果。
    - `request_id`：（可選）請求的ID。
  - **輸出：** 無直接輸出，但會設置實例變量。

- **execute_search(self, session=None):**
  - **用途：** 執行對 GPT 模型的查詢和獲取結果。
  - **參數：**
    - `session`：（可選）用於執行搜索的會話，默認為None。
  - **輸出：** 無返回值，但會更新類別實例的多個屬性，如`self.found`, `self.retrieved`和`self.response`。

- **normalize_response(self):**
  - **用途：** 正規化從 GPT 模型獲得的回應。
  - **參數：** 無。
  - **輸出：** 無返回值，但會更新`self.results`，這是一個包含處理後的搜索結果的列表。

這個類別還包含了一些用於配置和日誌記錄的變量，例如`MODEL_3`, `MODEL_4`, `MODEL`以及`MODEL_DEFAULT_SYSTEM_GUIDE`。這些配置變量允許定制 GPT 模型的使用以及定義系統對話指南。

類別的方法使用 OpenAI 提供的 API 進行交互，並處理來自搜索系統或其他來源的查詢。這個處理包括組裝適當的提示（prompted query），發送給 GPT 模型，並將模型的回應轉換為標準格式的搜索結果。這些結果隨後可以被搜索系統顯示或進一步處理。