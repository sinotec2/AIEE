---
layout: default
title: install.sh
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

- 這個[ Shell 腳本](../install.sh)是用來設置 Python 項目的依賴和配置的。
- 它檢查 `.env` 和數據庫文件，安裝 Python 依賴，並檢查自然語言處理庫 spaCy 的模型是否最新。

## 前提

- *需有python3之環境(以下準備了py39)*
- *腳本會將軟體安裝到py38環境中*

## 腳本說明

以下是腳本中一些重要命令的用途、參數和輸出：

### 命令：檢查 `.env` 文件

- **用途**：確保 `.env` 配置文件存在。
- **輸入參數**：無。
- **輸出**：如果 `.env` 文件不存在，則從 `.env.dist` 拷貝一份。

### 命令：檢查 `db.sqlite3` 文件

- **用途**：確保 SQLite 數據庫文件存在。
- **輸入參數**：無。
- **輸出**：如果 `db.sqlite3` 文件不存在，則從 `db.sqlite3.dist` 拷貝一份。

### 命令：安裝 Python 依賴

- **用途**：安裝 `requirements.txt` 文件中列出的 Python 依賴。
- **輸入參數**：無。
- **輸出**：安裝所有必需的 Python 包。

### 命令：檢查 spaCy 語言模型

- **用途**：檢查指定的 spaCy 語言模型是否已安裝並且是最新的。
- **輸入參數**：spaCy 語言模型的名稱。
- **輸出**：如果模型過時或不存在，則從 spaCy 下載新的語言模型。

### 命令：下載 NLTK 模塊

- **用途**：下載 NLTK（自然語言處理工具包）所需的模塊。
- **輸入參數**：無。
- **輸出**：下載 `stopwords` 和 `punkt` 模塊。

### 最後一行

- **用途**：通知用戶如果之前的步驟沒有出現錯誤，可以運行 `python swirl.py setup` 以完成安裝。
- **輸入參數**：無。
- **輸出**：在終端機顯示指示信息。

