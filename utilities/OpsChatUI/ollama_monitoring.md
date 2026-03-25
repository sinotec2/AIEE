---
title: ollama容器運轉監測
tags: AI
layout: default
parent: OpsChatUI
grand_parent: Utilities
date: 2025-10-15
modify_date: 2025-10-21T08:37:00
---

## 背景

ollama的容器似乎很容易發生記憶體失控(out of memory)，容器雖然沒有失敗，但是附載全由CPU負擔，GPU記憶體失敗。需要人工重啟。

為改善這個情況，雖然有swarm的系統規劃，但單一容器仍然有崩壞的可能，最終還是需要重啟服務。這方面並不存在開源程式，需要另外按語言模型的特性特別撰寫監視器、與自動重啟程序。

[**monitor.py** ](monitory.py)不是簡單目標的腳本，而是一個「Ollama‑Stack 監視器與自動重啟裝置」。  

它存在於一個已有 **Docker Compose / Stack**（通常放在 `/nas2/kuang/MyPrograms/ollama`）目錄下，並透過 **systemd** （或 **Docker**、你可以自行選擇）啟動。下面是它所承擔的角色、工作流程以及設計背後的動機。

---

### 1️⃣ 為什麼要寫這個監視器？

| 需求              | 產生的痛點                                                        | 監視器的解決方式                                                              |
| --------------- | ------------------------------------------------------------ | --------------------------------------------------------------------- |
| **GPU 簡易無回應**   | Ollama 進程偶爾被系統主動 kill 或掛起，GPU 變得空閒（但 stack 仍在跑）              | 監測 `nvidia-smi` 的 `memory.used` 或 `utilization.memory`，若持續為 0 → 嘗試重啟  |
| **服務失衡或長時間無回應** | Docker Compose 堆疊有多個 service（haproxy、ollama、…），其中一個失效但系統會繼續跑 | 用 `docker services` / `docker stack deploy` 重新建構整個 stack              |
| **預防重複進程**      | 已有在 GPU 的進程被壞掉或崩潰，留下殘留 PID 佔用記憶體                             | 取得 GPU 進程 PID 清單，若無任何進程或占用 0 → 重新部署                                   |
| **自動化、無人介入**    | 本地機器是伺服器，需要長時跑且不想人工倒車                                        | systemd 的 `Restart=on-failure` 或 Docker 的 `restart=always` 讓容器/服務自動重啟 |

> **核心目標**：讓「Ollama 服務 + GPU」永遠處於「熱」狀態；若長時間無回應或失效，立刻喚醒並重啟，避免人員手動操作。

---

### 2️⃣ 主要組成

| 模組 | 主要職責 |
|------|----------|
| **config / env** | 讀取 `CHECK_INTERVAL`、`MAX_UNHEALTHY` 等設定；同時決定 target URL、model 名稱、GPU index、compose 檔路徑等 |
| **GPU 工具** (`gpu_usage_check`, `check_pids`, `kill_pids`) | 透過 `nvidia-smi` / `subprocess` 監測 GPU 使用情況，判斷是否需要 kill / 重新部署 |
| **Docker 工具** (`remove_service`, `deploy_stack`) | 直接對 docker‑py 或容器 host 之 Docker socket 進行 `service` 刪除 / `stack deploy` |
| **舉動 / 事件** (`run_dummy`, `dummy_inference`) | 在偵測到 GPU 空閒時，先送 *dummy* 推論請求，讓 Ollama 重新載入並使用 GPU |
| **主循環** (`main`) | 以 `CHECK_INTERVAL` 週期檢查 GPU / 進程；若發現問題則執行 `run_dummy`、`reset_services` 以恢復服務 |

---

### 3️⃣ 工作流程（概念流程圖）

1. **啟動腳本** → `systemd` 或 `Docker` 以 `--restart` 或 `Restart=on-failure` 監護
2. **等待** `CHECK_INTERVAL`（預設 60 秒）
3. **檢查 GPU**  
   * `check_pids` → 取得 GPU 當前佔用的進程 PID  
   * `gpu_usage_check` → 讀取 memory 使用量
4. **判斷狀態**  
   * **無進程或 memory 0**  
     * 執行 `run_dummy`（送 dummy 推論）  
     * 檢查是否成功載入  
     * 若失敗 → `reset_services()`（刪除舊服務，重新 deploy stack）
   * **已佔用** → 檢查是否為舊進程（殘留） → `kill_pids()` 清除
5. **循環** → 繼續下一個檢查週期

---

### 4️⃣ 為「兩種部署方式」留的設計空間

| 方式 | 主要需求 | 選擇關鍵點 |
|------|----------|------------|
| **systemd 在宿主機執行** | 需要直接操作 Docker socket 及 GPU；已安裝 python / conda 環境 | `User=` 需 root / 並確實存在；把 `/opt/anaconda3/.../python` 路徑寫進 `ExecStart` |
| **Docker 容器內執行** | 想要隔離、可跨境部署；部署需要掛載 `docker.sock`、`nvidia` 以及相同的 python 環境 | 需 `--privileged` 或 `--cap-add=SYS_ADMIN`；必須把 `docker.sock` 及 GPU 硬體掛進容器 |

---

### 5️⃣ 小結

[**monitor.py** ](monitory.py)是 **一個完整的自動化監視腳本**，負責確保 Ollama 服務永遠保持「熱」且可用。  
- 透過 GPU 監測 + docker‑py 何時需要重啟。  
- 支援 **systemd** 或 **Docker** 兩種部署方式。  
- 設計上保留了可擴充性（可加入更多檢測指標、更多服務名稱、更多 GPU 等）。

這個背景說明可以幫你快速理解為何要這樣寫、它是如何運作，以及在實際部署時該怎麼調整。
## `monitor.py` (Python 監控腳本)

檔案路徑：`/nas2/kuang/MyPrograms/ollama/ollama_restart/monitor.py`

### 1️⃣總體說明

此 Python 腳本用於監控 Ollama Docker 服務的 GPU 使用情況，並在 GPU 無使用或出現長期卡頓時自動重新部署 Docker stack。

- **功能說明**
    - 定期檢查 GPU 是否被 Ollama 服務佔用。
    - 若 GPU 無使用或出現長期卡頓，則自動重新部署指定的 Docker stack。
- **使用方式**
    1. 在宿主機安裝 Docker、`nvidia-smi`、Python 3 以及 `pip`。
    2. 本機執行 `bash -c "python monitor.py"`。
    3. 若欲在容器內執行，請參考下方提供的 Dockerfile 及執行指令。
- **環境變數**
    - `CHECK_INTERVAL`: 監測間隔（秒），預設 120 秒。
    - `MAX_UNHEALTHY`: 未回應次數斷線門檻，預設 3 次。
    - `MAX_CPU_PERCENT`: CPU utilization 上限（%），預設 80.0%。
    - `MAX_MEMORY_PERCENT`: Memory utilization 上限（%），預設 80.0%。
    - `MAX_IO_BYTES`: IO throughput 上限（B/s），預設 100000000。
### 2️⃣基本設定

- **主要模組導入**
    - 導入所需的 Python 模組，包括 `datetime`、`logging`、`os`、`sys`、`subprocess`、`time`、`threading`、`docker`、`requests` 等。
- **日誌設定**
    - 設定日誌記錄，包括日誌檔案路徑、檔案大小、備份數量等。
    - 日誌訊息會同時輸出到檔案和控制台。
- **程式組態**
    - 透過環境變數設定程式的各項參數，若未設定則使用預設值。

### 3️⃣**內部工具函式**

- `dummy_inference`: 送出一個[dummy]推論請求，藉此觸發 Ollama 服務的 GPU 負載。
- `run_dummy`: 在獨立執行緒中啟動 dummy 推論，避免阻塞主監控迴圈。
- `_run_cmd`: 執行 shell 命令，並回傳標準輸出。
- `gpu_usage_check`: 讀取指定 GPU 的 memory 利用率（%）。
- `get_compute_pids`: 取得目前在特定 GPU 上運行的 PCIe 油執行 PID。
- `kill_pids`: 給定欲殺掉的 PID 清單，逐一呼叫 `kill`。
###  4️⃣ **Docker 相關工具**

- `remove_service`: 通過 docker‑py 移除指定服務。
- `remove_services`: 移除多個服務。
- `deploy_stack`: 以容器宿主機的 docker CLI 方式部署 stack。
- `reset_services`: 先刪除舊服務，再重新部署 stack。

### 5️⃣**主邏輯**

- 程式入口：逐一監控設定好的 swarm stack。
- 監控 GPU 記憶體占用比例。
- 若沒有user相應的進程、系統處於閒置狀態，等候`CHECK_INTERVAL`: 監測間隔之後，隨即觸發 dummy 推論以產生 GPU 測試負載。
- 長期無 GPU 使用、或GPU呈現卡頓，隨即重啟該stack的服務。

## 使用方式

1. 確保已安裝 Docker、`nvidia-smi`、Python 3 以及 `pip`。
    
2. 安裝所需的 Python 模組：
    
    ```bash
    pip install docker requests  
    ```
    
3. 設定環境變數（可選）。
    
4. 執行腳本：

```bash
    python monitor.py  
```
    
::: warning

因為會刪除docker 內的ollama程序，需要`root`的權限

:::

## 監控效果

### 短期監測

- 觀察`vhtop`的線形對程式開發測試，有其必要與充分性。觀察重點：
	- 啟動條件、終止與清空記憶是否確實
	- 訂定系統記憶體重載所需的秒數閥值
	- 制定重啟邏輯：時間還是記憶體使用率、還是二者同時考量

![](pngs/Pasted%20image%2020251024184105.png)

### 中長期

- 一段時間(10~20分鐘)之後，ollama似乎會進入休眠，`gpt-oss:20b`重啟的時間超過15秒，以致容器服務系統進入重啟的邏輯。
- 相對而言，`llama3.1`似乎還可以在15秒內重新載入記憶體，重啟的機會較小。

```bash
kuang@eng06 /nas2/kuang/MyPrograms/ollama/ollama_restart
$ lst
total 28K
-rw-r--r-- 1 kuang SESAir  323  十  21 15:34 Dockerfile
-rw-r--r-- 1 kuang SESAir  13K  十  24 17:27 monitor.py
-rw-r--r-- 1 kuang SESAir  487  十  24 17:29 ollama-monitor.service
-rw-r--r-- 1 root  root   3.3K  十  24 18:10 ollama_monitor_20251024_172817.log

kuang@eng06 /nas2/kuang/MyPrograms/ollama/ollama_restart
$ grep 重啟 ollama_monitor_20251024_172817.log
2025-10-24 17:34:47,599 |     INFO | Ollama PID gpt-oss:20b GPU 未占用，將重啟服務
2025-10-24 17:43:28,534 |     INFO | Ollama PID gpt-oss:20b GPU 未占用，將重啟服務
2025-10-24 18:08:53,306 |     INFO | Ollama PID gpt-oss:20b GPU 未占用，將重啟服務
2025-10-24 18:17:29,066 |     INFO | Ollama PID gpt-oss:20b GPU 未占用，將重啟服務
```

![](pngs/Pasted%20image%2020251024182110.png)

## TODOs

[] 夜間或假日方案
	- `systemd`似乎沒有辦法像 `crontab` 一樣做到更細粒度的監控，這點還需要改進，也許用 `crontab`做`systemctl stop/start `控制
[] 沒有user的使用pids，該不該、該如何清空記憶體?


## 學習心得

這個 “ollama‑monitor” 專案可以學到哪些實用且具體的技術／概念？

| 類別 | 具體學習項目 | 為什麼重要 | 典型實作／操作範例 |
|------|--------------|------------|-------------------|
| **Python 程式設計** | *型別註解 (typing) / docstring*<br>*異步／threading 造`run_dummy`*<br>*Robust error handling (requests, subprocess, docker.errors)* | 讓程式碼在群組開發、持續整合時更易閱讀、維護。 | `def dummy_inference(url: str, model: str) -> bool: …` |
| **日誌管理** | *logging.FileHandler + RotatingFileHandler*<br>*把 timestamp 加到 log 檔名* | 日誌可追溯、分檔、避免磁碟溢位。 | `logging.handlers.RotatingFileHandler(..., maxBytes=2*1024*1024)` |
| **GPU 監控** | *nvidia‑smi 直接取得記憶體佔用與 utilisation*<br>*解析輸出、判斷空閒* | 在 AI 服務中 GPU 維持『熱』對延遲/可靠性至關重要。 | `subprocess.check_output(cmd).decode()` |
| **Docker API** | *docker‑py 輕量級刪除/部署 stack*<br>*升級 `docker stack deploy -c …` 呼叫子命令* | 從 Python 直接操縱容器，省去 shell & 失誤。 | `client.services.get(name).remove()` |
| **Systemd 服務化** | *編寫 unit 檔、設定 `User=`、`Restart=`*<br>*確定 `WorkingDirectory=` 與 `ExecStart=` 路徑* | 讓腳本在作業系統級別自動啟動、重啟、並簡化管理。 | `ExecStart=/opt/anaconda3/envs/ollama/bin/python monitor.py` |
| **權限與安全** | *PID namespace / host PID*<br>*`cap-add=SYS_ADMIN` 或 `--privileged` 需要確認*<br>*`docker.sock` 掛載與權限設定* | 評估何時必須用 `root`、何時用 `privileged` 以避免安全風險。 | `docker run --privileged -v /var/run/docker.sock:/var/run/docker.sock …` |
| **錯誤診斷** | *systemd `journalctl`, `systemctl status`, `systemctl show` 等命令*<br>*理解 217/USER 等錯誤碼* | 快速定位「\*失敗在 User／Group 設定」與「找不到可執行文件」。 | `sudo journalctl -u ollama-monitor -f` |
| **持續健康檢查** | *健康檢查 `apt` 內置 healthcheck 與容器重啟策略*<br>*自建的「dummy 推論」保持輪詢* | 讓整個 stack 在 GPU 離線時自動修復。 | `logging.info("resetting OLlama stack …")` |
| **配置管理** | *環境變數、`docker-compose.yml` 路徑、GPU 參數*<br>*簡易 CLI / Argparse 功能* | 版本控制、不同環境（dev/stage/production）共用同一程式碼。 | `CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "60"))` |
| **容器化最佳實踐** | *最小化 Docker image*<br>*使用 `python:slim`, 安裝必須套件*<br>*保持 entrypoint 擴展可測試* | 碼量最小、重啟腳本置於容器入口、易於 CI/CD。 | `HEALTHCHECK --interval=30s --timeout=5s --retries=5 CMD curl -f http://localhost:12000/health` |

---

### 從這個專案開始學到哪三件事？

1. **如何把「感知 GPU 與 Docker** 轉成「**自動化腳本** 」 
   先寫一個普通腳本嘗試監控 GPU，再將其逐步移植到 `systemd` 及 Docker 裡面，體驗「環境隔離 + 監控 + 自動修復」的完整流程。

2. **在調試與部署時避免「107/USER、No such process」類錯誤**  
   了解 `systemd unit` 的執行階段 (USER、PREREQUISITE、READP、EXEC)、如何使用 `Journalctl`、`systemctl reveal` 等命令快速定位權限/路徑問題。

3. **設計一個既可運行又易閱讀的監控腳本**  
   認識日誌寫往檔案、旋轉、截斷的最佳實踐；如何用 `logging.handlers.RotatingFileHandler` 限制檔案 2 MB 占用；如何在主程式裡以 `threading.Thread` 不阻塞。

---

### 進一步上手的小路徑

| 目標       | 下一步                                                                                                                                                 |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **本地實驗** | 1️⃣ 在宿主機直接執行 `python monitor.py` 看是否能正常監測 GPU。<br>2️⃣ 再跑一次 `systemd` 單元檔測試。                                                                         |
| **容器化**  | 1️⃣ 建立簡易 `Dockerfile` 只安裝 `python`、`pip install docker requests`。<br>2️⃣ 將 `docker.sock` 掛載進容器並執行 `systemctl` (需要 `systemd` 內部) 或直接使用 `docker run`。 |
| **測試重啟** | 1️⃣ 在監控腳本內注入 `time.sleep(180)` 套組讓 GPU 立即空閒。<br>2️⃣ 驗證重啟流程成功。                                                                                       |
| **安全測試** | 1️⃣ 避免使用 `--privileged`；嘗試 `--cap-add=SYS_ADMIN` 只開啟必要權限。<br>2️⃣ 授權正確的 `User=` 、`Group=` 以檢測最小化權限。                                                  |

---

## 結語

- 這個「ollama‑monitor」不僅能讓你運行 Ollama 並自動重啟，更提供了一整套 **Python** + **Docker** + **systemd** 的實作範例。  
- 你可以把它當成一個 **完整的觀測‑自動修復** 案例，從代碼、配置、容器、安全、排錯全方位練習。  
- 接下來，挑選你最感興趣的方向（例如調優 GPU 監控、探究 systemd `User=` 的安全性，或者把監控腳本打包成 CI/CD 流程），即可深入學習並把知識應用到實際專案。