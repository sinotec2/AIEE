---
layout: default
title: swirl.py
parent: swirl搜尋引擎
grand_parent: 自然語言處理
nav_order: 99
date: 2023-11-13
last_modified_date: 2023-11-13 19:18:56
has_children: true
tags: AI chat report
---

# swirl.py
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

- 系統之啟動、關閉、再啟動、狀態：`python swirl.py start/stop/restart/status`
- celery 部分啟動
  - celery-beats：`python swirl.py start celery-beats`
  - elery-worker：`python swirl.py restart celery-worker consumer`
- help：`python swirl.py help`
- debug mode：
  - `python swirl.py --debug start`
  - 畫面會從`Daphne`切換到一個內設的Django webserver (`runserver`)
- 程式的使用詳見[using swirl.py](https://sinotec2.github.io/AIEE/NLP/swirl/docs/Admin-Guide/#using-swirlpy)

## 程式說明

這個 Python 腳本([swirl.py](./swirl.py))是 Swirl 伺服器*執行*管理的工具。以下是對代碼的簡要說明：

1. **導入模組**：包括處理正則表達式、命令行參數、系統操作、子進程、時間等功能的模組。

2. **全局變數定義**：設定模組名稱、Swirl 核心服務、版本檢查 URL、命令列表等。

3. **功能函數**：
   - `get_swirl_version`：獲取 Swirl 的當前版本信息。
   - `service_is_retired`：檢查服務是否已被棄用。
   - `check_pid` 和 `show_pids`：檢查和顯示進程 ID。
   - `load_swirl_file` 和 `write_swirl_file`：加載和寫入 Swirl 的設定文件。
   - `launch`：啟動指定的服務。
   - `start`, `stop`, `restart` 等：控制 Swirl 服務的開始、停止和重啟。
   - `migrate`：處理數據遷移。
   - `status`, `logs` 等：顯示系統狀態和日誌。
   - `setup`：設置 Swirl 環境。

4. **主函數 `main`**：
   - 使用 `argparse` 解析命令行參數。
   - 根據指令執行相對應的操作，如 `start`、`stop`、`restart` 等。
   - 提供調試模式的支持。
   - 使用 `COMMAND_DISPATCH` 字典將命令映射到相應的函數。

5. **腳本功能**：這個腳本使得用戶能夠通過命令行管理 Swirl 伺服器，包括啟動、停止、重啟服務，查看狀態和日誌，執行數據庫遷移等。

總的來說，這是一個為管理 Swirl 伺服器提供方便的命令列工具，適用於*運作*伺服器的部署和維護。
