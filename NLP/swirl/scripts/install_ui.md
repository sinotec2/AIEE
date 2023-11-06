---
layout: default
title: install_ui.sh
grand_parent: swirl搜尋引擎
parent: scripts
nav_order: 99
date: 2023-02-16
last_modified_date: 2023-02-16 19:35:37
tags: AI ChatGPT note_system
---

# install.sh

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

- 這個[ Shell 腳本](../install_ui.sh)是用來設置 Python 項目的依賴和配置的。
- 它檢查 `.env` 和數據庫文件，安裝 Python 依賴，並檢查自然語言處理庫 spaCy 的模型是否最新。

## 前提

- *要先執行swirl.py安裝*：`python swirl.py setup`
- *需有python3之環境(以下準備了py39)*
- *腳本會將軟體安裝到py38環境中*
- *會需要jq*：`sudo yum --disablerepo=c7-media -y install jq`(DEVP的`yum`內設會讀取光碟更新c7-media內容)
- *docker必須先在背景執行*

## 腳本說明

這個 Bash 腳本是用來安裝用戶界面到 Swirl 的靜態目錄中。在運行此腳本之前，必須先運行 Swirl 的安裝和設置。以下是腳本中的一些重要函數及其用途：

### 命令：檢查 jq 命令

- **用途**：確保 jq 命令可用，jq 用於處理 JSON。
- **輸入參數**：無。
- **輸出**：如果 jq 命令不在路徑上，將給出錯誤信息。

### 命令：確定要使用的圖像

- **用途**：基於命令行參數（preview、x-fork）來確定使用哪個 Docker 映像。
- **輸入參數**：`-p`（預覽圖像）、`-x`（實驗分支圖像）。
- **輸出**：設置要從 Docker Hub 拉取的圖像變量。

### 命令：複製 UI 文件

- **用途**：如果提供了源目錄，將直接從該目錄複製文件。
- **輸入參數**：源目錄的路徑。
- **輸出**：將 UI 文件從源目錄複製到目標目錄。

### 命令：從 Docker 容器中提取 UI 文件

- **用途**：如果沒有提供源目錄，則從指定的 Docker 映像中提取 UI 文件。
- **輸入參數**：Docker 映像的名稱。
- **輸出**：將 UI 文件從 Docker 容器複製到工作目錄，然後移動到目標目錄。

### 命令：配置前端應用的默認設置

- **用途**：從提取的文件中提取配置，並用環境變量替換佔位符，以創建前端應用的配置。
- **輸入參數**：包含替換占位符的 jq 命令。
- **輸出**：在目標目錄中創建一個包含配置的 `default` 文件。

### 最後的清理和完成信息

- **用途**：刪除工作目錄並移除 Docker 容器，然後顯示完成信息。
- **輸入參數**：無。
- **輸出**：終端中顯示完成信息。

## 開始swirl

- *背景必須有redis*
- *如果要提供其他人搜尋，需修改.env內的ALOWHOST=200.200.32.195*
- 開始`python swirl.py start`
  - 不會有server的訊息。會自動在背景執行。
  - 登入：admin/password
  - 登出：如未登出，再次登入會無法搜尋。
- 結束：`python swirly.py stop`

