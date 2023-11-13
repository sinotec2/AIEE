---
layout: default
title: swirl_load.py
parent: swirl搜尋引擎
grand_parent: 自然語言處理
nav_order: 99
date: 2023-11-13
last_modified_date: 2023-11-13 19:18:56
has_children: true
tags: AI chat report
---

# swirl_load.py
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

- 用在新增搜尋對象時，會需要將提供者的連結方式、搜尋結果送往AI解讀的傳送設定等等細節，載入系統程式之中。
- 使用方式詳見[Bulk Loading](https://sinotec2.github.io/AIEE/NLP/swirl/docs/User-Guide/#bulk-loading)
1. 先準備好連結設定檔。可以參考模版設定。
   1. 可以直接編輯`SearchProvider/...json`
   2. 也可以使用專用界面` http://localhost:8000/swirl/searchproviders/{id}/`.`id`為`preloaded.json`內的序號。
2. `preloaded.json`是裝置時載入系統的內容。
3. 如不重新安裝，就只能新增功能、以新的檔案內容覆蓋舊的設定（關閉或開啟）。
4. 需要`admin`身分與密碼才能改變設定。

![wirl_sp_instance](https://sinotec2.github.io/AIEE/NLP/swirl/docs/images/swirl_sp_instance.png)

```bash
python swirl_load.py SearchProviders/provider-name.json -u admin -p your-admin-password
```

## 程式說明

這個 Python 腳本（[swirl_load.py](./swirl_load.py)）是一個命令行工具，用於將 JSON 格式的資料批量加載到 Swirl 應用程式中。以下是對這段代碼的逐行解釋：

1. 導入必要的模塊：包括 `argparse` 用於解析命令行參數，`sys` 和 `os` 用於系統操作，`glob` 用於文件路徑模式匹配，`json` 用於處理 JSON 資料，以及 `requests` 用於 HTTP 請求。

2. `module_name = 'swirl_load.py'`: 定義一個變量來儲存腳本名稱。

3. 從 `swirl.banner` 導入 `SWIRL_BANNER` 和 `bcolors`，這些可能是用於顯示標誌和顏色的自定義工具。

4. 定義 `main` 函數，它是腳本的入口點。

5. 使用 `argparse.ArgumentParser` 創建一個解析器對象，並添加命令行參數。

6. 解析命令行參數並儲存在 `args` 變量中。

7. 使用 `glob.glob` 獲取匹配的文件列表。

8. 對每個文件執行以下操作：
   - 檢查是否為目錄，如果是，則遞迴搜索。
   - 嘗試打開並讀取文件內容，將其解析為 JSON。
   - 根據 JSON 物件的鍵來判斷它的類型（如 searchprovider、search、result）。
   - 構建目標 URL 並使用 `requests.post` 向 Swirl 服務器發送 POST 請求，將 JSON 資料傳輸過去。

9. 處理請求的響應，記錄成功和錯誤的數量。

10. 最後打印載入過程中成功和失敗的記錄數量。

此腳本的主要功能是將指定路徑下的 JSON 文件批量加載到 Swirl 應用程式中。這對於需要快速將大量資料導入 Swirl 的場景非常有用。它支持通過命令行參數定制行為，包括指定 Swirl 服務器的 URL、開啟調試模式、以及提供用於身份驗證的用戶名和密碼。
