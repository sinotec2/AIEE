---
layout: default
title: chatgpt_query.py
nav_order: 99
layout: default
grand_parent: swirl搜尋引擎
parent: swirl
date: 2023-11-09
last_modified_date: 2023-11-09 09:45:06
tags: AI chat report
---


# chatgpt_query.py


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

- 程式位置：[swirl/processors/chatgpt_query.py](./chatgpt_query.py)

## 程式說明

這段Python程式碼定義了一個名為`ChatGPTQueryProcessor`的類別，這個類別繼承自`QueryProcessor`，用於改善查詢字符串，以便在搜索引擎中獲得更精確的結果。這個類別主要利用OpenAI的GPT-3模型來實現查詢優化的過程。

以下是主要功能和步驟的概述：

1. **初始化（`__init__`）**：
   - 接收查詢字符串(`query_string`)、映射和標籤，並調用父類別的初始化方法。

2. **設置提示（`set_prompt`、`get_prompt`、`set_prompt_from_tags`）**：
   - 設置和獲取用於向模型發送的提示信息。
   - 如果標籤中沒有提供提示，則使用預設提示。

3. **設置指導信息（`set_guide_from_tags`）**：
   - 從標籤中獲取指導信息，如果沒有提供，則使用預設指導信息。

4. **設置是否應用過濾（`set_do_filter_from_tags`）**：
   - 從標籤中決定是否對ChatGPT的回覆應用過濾規則。

5. **處理函數（`process`）**：
   - 設置必要的提示、指導信息和過濾標志。
   - 使用OpenAI的API和GPT-3模型生成查詢優化建議。
   - 處理來自模型的回應，並應用一系列檢查和過濾規則來確保回應的相關性。

6. **清理回應（`clean_reply`）**：
   - 移除回應中的換行符和雙引號等不需要的字符。

這段代碼主要通過與OpenAI的GPT-3模型的互動來優化用戶的搜索查詢。它首先確定是否需要對模型的回應進行過濾。然後，它根據提示和系統指導信息向模型發送查詢字符串，並處理模型的回應。如果選擇應用過濾，它還會執行一系列規則來決定是否接受模型的建議，或者直接返回原始查詢字符串。

這個程式是為了自動化查詢優化過程，以改善搜索引擎的查詢結果，提供更精確、更相關的搜索結果。

## 

是的，"接收查詢字符串"在這段程式碼中指的就是`query_string`。在`ChatGPTQueryProcessor`類別中，`query_string`是傳遞給`__init__`方法的一個參數，代表用戶輸入的原始查詢內容。這個字符串會被用於生成提示（prompt）並傳送給GPT模型，以獲取優化後的查詢建議。程序中涉及到的變數`self.query_string`就是用來存儲這個查詢字符串的。