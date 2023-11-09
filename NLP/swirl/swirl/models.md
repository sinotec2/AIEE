---
layout: default
title: models.py
nav_order: 99
layout: default
grand_parent: swirl搜尋引擎
parent: swirl
date: 2023-11-09
last_modified_date: 2023-11-09 09:45:06
tags: AI chat report
---


# models.py


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

- 程式位置：[swirl/models.py](./models.py)

## 主程式說明

這段代碼是 Django 模型的一系列定義，這些模型用於 Swirl 搜尋平台的資料庫架構。 每個類代表數據庫中的一個表，並定義了數據庫表中將存儲的字段和數據類型。 以下是代碼中每個模型的簡要說明及其重要欄位：

### FlexibleChoiceField
- **用途：** 一個自訂欄位類，允許使用預先定義的選項或自由文字。

### Authenticator
- **用途：** 定義了一個用於身份驗證的模型，包含驗證方法的名稱。

### OauthToken
- **用途：** 儲存使用者的 OAuth 令牌訊息，與特定的身分提供者（如 Microsoft）相關聯。

### SearchProvider
- **用途：** 定義了一個搜尋提供者，它包含了搜尋配置，如搜尋的 URL、查詢範本、查詢處理器等。

### Search
- **用途：** 定義了一個搜尋實例，它包含了查詢字串、排序方式、查詢處理器等。

### Result
- **用途：** 定義了搜尋結果的模型，包括查詢字串、狀態、檢索到的結果數量等。

### QueryTransform

- **用途：** 定義了查詢變換規則，可以是重寫、同義詞替換或同義詞包。

每個模型都包含一些通用的 Django 字段，如
- `CharField`、`IntegerField`、`DateTimeField` 和 `JSONField`。 `JSONField` 通常用來儲存可設定的選項，例如查詢處理器的清單。
- 這些模型還包含特定於業務邏輯的字段，如 `searchprovider_list` 或 `query_to_provider`。

這些模型的實例將被用於建立和管理搜尋相關的數據，並在整個應用程式中進行存取和處理。 透過定義模型，Django 可以根據這些定義建立和維護資料庫表結構。

## SearchProvider

`SearchProvider` 是一個 Django 模型，代表了搜索提供者的配置信息。這些信息用於定義和配置搜索查詢的來源和方式。以下是 `SearchProvider` 模型的各個字段的說明：

- `id`: 數據庫中的主鍵，自動增長的大型整數。
- `name`: 搜索提供者的名稱。
- `owner`: 這個字段是一個外鍵，關聯到 Django 的內置 `User` 模型，表示創建此搜索提供者的用戶。
- `shared`: 一個布爾字段，指示此搜索提供者是否對其他用戶開放。
- `date_created` 和 `date_updated`: 分別記錄了搜索提供者的創建時間和最後更新時間。
- `active` 和 `default`: 布爾字段，分別表示搜索提供者是否活躍和是否為默認提供者。
- `authenticator`: 這個字段允許從預定義的認證方式中選擇一種，例如 Microsoft 認證。
- `connector`: 定義了用於執行搜索查詢的連接器類型，如 HTTP GET、HTTP POST、Elasticsearch 等。
- `url`: 用於搜索查詢的基礎 URL。
- `query_template`: 定義了如何構造搜索查詢的模板。
- `post_query_template`: 一個 JSON 字段，定義了 POST 請求的模板。
- `query_processors`: 定義了處理查詢的處理器列表。
- `query_mappings`: 提供了將查詢字符串映射到特定格式的模板。
- `response_mappings`: 提供了將搜索結果映射到特定格式的模板。
- `result_grouping_field`: 如果設置，並且結果集中存在這個字段，相同值的記錄將被分組，並且只有一個結果將返回給調用者。
- `result_processors`: 定義了處理搜索結果的處理器列表。
- `result_mappings`: 提供了將搜索結果映射到特定格式的模板。
- `results_per_query`: 每次查詢返回的結果數量。
- `eval_credentials` 和 `credentials`: 用於存儲搜索提供者的認證信息。
- `tags`: 一個 JSON 字段，存儲與此搜索提供者相關的標籤。
- `http_request_headers`: 存儲 HTTP 請求頭的 JSON 字段。
- `page_fetch_config_json`: 存儲頁面獲取配置的 JSON 字段。

`class Meta` 中的 `ordering` 定義了默認的排序方式，此處按 `id` 排序。

`get_absolute_url` 方法用於獲取訪問該搜索提供者詳情頁面的 URL。

`__str__` 方法返回搜索提供者的名稱，當將對象轉換為字符串時使用，例如在 Django 管理後台顯示。

整體上，這個模型在 Swirl 平台中扮演著核心角色，允許用戶配置和管理他們的搜索提供者，並根據這些配置執行搜索查詢。