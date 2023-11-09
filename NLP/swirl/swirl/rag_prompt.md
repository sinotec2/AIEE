---
layout: default
title: swirl/rag_prompt.py
nav_order: 99
layout: default
grand_parent: swirl搜尋引擎
parent: swirl
date: 2023-11-09
last_modified_date: 2023-11-09 09:45:06
tags: AI chat report
---

# rag_prompt.py

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

- 程式位置：[swirl/rag_prompt.py](./rag_prompt.py)
- 本程式受到[rag.py](./processors/rag.md)的呼叫，傳入變數
  - 查詢(`user_query`)、
  - 最大令牌數(`max_tokens=max_tokens`)、
  - 模型(`model=MODEL`)

## 程式說明

這段代碼定義了一個名為 `RagPrompt` 的類，它用於處理和準備提交給 OpenAI 聊天模型的提示文字（prompt text）。 `RagPrompt` 類別提供了一種方式來組織和格式化輸入資料，以便更有效地利用語言模型來產生回應。

以下是該類的主要方法和屬性：

- `__init__`: 初始化方法，設定查詢、最大令牌數、模型和提示文字的基本結構。

- `get_num_tokens`: 傳回目前提示文字中的令牌數。

- `is_full`: 判斷是否已達到或超過最大令牌數限制。

- `_all_tokens_exist` 和 `_no_tokens_exist`: 這些方法用於檢查字串中是否存在或完全不存在與另一個字串相關的令牌。

- `_is_good_chunk`: 決定一段文字（chunk）是否適合加入到提示中。 這涉及檢查其長度以及是否含有查詢的相關術語。

- `_count_model_tokens_in_string`: 計算字串中的令牌數量。

- `_trim_punctuation`: 清理字串開頭和結尾的標點符號。

- `_sprint_chunk`: 根據給定的文字區塊、網域和內容類型格式化一段新的提示文字。

- `is_last_chunk_added`: 檢查最後一段新增的文字是否符合標準。

- `get_last_chunk_status`: 取得最後一段文字的狀態。

- `put_chunk`: 新增一段文字到提示中，如果新增成功，則更新令牌計數和提示文字。

- `get_promp_text`: 取得目前的完整提示文字。

- `get_role_system_guide_text`: 取得預設的系統指引文本，用於向模型提供背景資訊。

整個類別是為了確保產生給定查詢的最佳提示，同時考慮到模型的令牌限制和文字的相關性。 這對於與GPT-3.5或GPT-4等先進的聊天模型進行互動非常關鍵，因為模型的性能很大程度上取決於它收到的提示的品質。

## 修改內設提示

### MODEL_DEFAULT_SYSTEM_GUIDE

- 原來內容

```python
MODEL_DEFAULT_SYSTEM_GUIDE="You are a helpful assistant who considers recent information when responding. You are positive and do not report negative or upsetting things, like poor ratings."
```

- 修改版本

```python
MODEL_DEFAULT_SYSTEM_GUIDE = "You are a helpful assistant who considers recent information when responding. You are positive and do not report negative or upsetting things, like poor ratings. Be concise, accurate and thorough. Provide details."
```

### self._prompt_text

```python
        self._prompt_text = f"Answer this query '{query}' given the following recent search results as background information. Do not mention that you are using the provided background information. Please cite the sources at the end of your response. Ignore information that is off-topic or obviously conflicting, without warning about it."
```

- 修改版本

```python
        self._prompt_text = f"Answer this query '{query}' given the following recent search results as background information. \
Do not mention that you are using the provided background information. Please cite the sources at the end of your response. \
Ignore information that is off-topic or obviously conflicting, without warning about it. \
Please answer in Tradition Chinese."
```