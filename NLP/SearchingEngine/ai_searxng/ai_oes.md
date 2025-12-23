---
layout: default
title: AI‑OES 搜尋插件設計與使用說明
parent: 地端智慧搜尋引擎
grand_parent: SearchingEngine
nav_order: 3
date: 2025-11-12
last_modified_date: 2025-11-12T13:08:00
tags:
  - AI
  - searching
  - OES
---

# AI‑OES 搜尋插件設計與使用說明  

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

**檔案路徑**：`/nas2/kuang/MyPrograms/OES/ai_oes.py`  
**作者**：kuang@l40  
**授權**：AGPL‑3.0-or‑later  (可自行修改成其他 BSD / MIT 等，請自行調整 `SPDX` 識別)

> 本文件對 `ai_oes.py` 補充 **設計架構**、**依賴、配置**和**使用流程**，方便你在`searx`（或自訂的搜尋平台）中嵌入 AI 摘要功能。  
> 若你想把此插件放到 Docker 容器內，亦可參考下方的 **部署指引**。  

---

## 1️⃣ 目錄

| 章節         | 簡述                                         |
| ---------- | ------------------------------------------ |
| 1. 所有者與版本  | 作者、日期、授權                                   |
| 2. 依賴      | 必要的 Python 套件                              |
| 3. 目錄結構    | 插件所在路徑、設定檔                                 |
| 4. 設計概觀    | 主要類別、流程                                    |
| 5. 重要屬性與方法 | 每個成員變數、關鍵函式說明                              |
| 6. 如何啟用    | 在 `searx` 的設定檔 ( `searx/settings.yml`) 裡加載 |
| 7. 配置項     | 修改 API URL、token、摘要長度等                     |
| 8. 使用範例    | 單筆搜尋、批量測試                                  |
| 9. 故障排除    | 常見問題 & 解決方案                                |
| 10. 擴充     | 如何改寫 prompt、切換模型、快速重試                      |
| 11. 部署     | Docker／K8s、CI 時的執行方式                       |
| 12. 參考資料   | 官方 API、OpenAI、Markdown-it 等                |


---

## 2️⃣ 依賴

| 套件 | 版本 | 安裝方式 | 作用 |
|------|------|----------|------|
| `requests` | `>=2.25` | `pip install requests` | HTTP client，向 vLLM 伺服器發送請求 |
| `searx` |  | 內建 | 提供 `Plugin`, `PluginInfo`, `EngineResults` 這些基礎類別 |
| `markdown-it-py` | `>=2.2` | `pip install markdown-it-py` | 把 vLLM 回傳的 Markdown 轉成純文字 |
| `flask-babel` |  | 內建 | 本地化字符串 (gettext) |
| `python-telnet` |  | | 用於內部 `searx` |
| `pylint` (optional) |  | | 以 PC 檢查 |

::: note

 > 如果是在 Docker 內部執行 `searx`, 請確認 `requirements.txt` 中包含 `markdown-it-py` 及 `requests`。  
> 其它依賴直接由 `searx` 安裝。  

:::

---

## 3️⃣ 專案目錄

```
/nas2/kuang/MyPrograms/searxng/
├─ searx/plugins/ai_oes.py            ← 本插件 (主入口)
├─ searx/settings.yml   ← searx 主設定檔 (須加載該插件)
├─ config/settings.yml   ← searx 外部設定檔 (Docker執行時會加載此檔)
└─ requirements.txt     ← 若使用 Docker 或 pip 安裝

```

> `searx/settings.yml` 中加入

```yaml
plugins:
 - ai_oes
```

- 若編譯 `searx` 的 Docker 版，則
	- 修改 `searx/settings.yml` 之後，重新建構容器，
	- 還要注意外部`config/settings.yml`需同步更新。


---

## 4️⃣ 設計概觀

| 類別 / 函式           | 作用            | 簡述                                                                |
| ----------------- | ------------- | ----------------------------------------------------------------- |
| `SXNGPlugin`      | 入口點           | 由 `searx` 提供 `Plugin` 基礎類別，實作 `pre_search`, `post_search`         |
| `call_vllm`       | 請求本機 vLLM     | 發送 POST 給 `api_url` (OpenAI 介面)                                   |
| `delayed_collect` | 當前搜尋執行完成時自動執行 | 讓插件在搜尋結果到位後，取 `main_results_sorted` 或 `main_results_map` 進行 AI 摘要 |
| `Answer`          | 資料結構          | 用於回傳 AI 結果（以及 loading 佔位文字）                                       |

插件整體流程：

1. 用戶輸入 `ai <關鍵字>` → `pre_search` 會偵測到前綴 `ai`  
2. `search_query.query` 被截掉 `ai`，並在 `search` 物件上寫 `_ai_mode = True`  
3. 搜尋器完成後，`post_search` 在 `container` 內執行 `delayed_collect()`  
4. 收到搜尋結果（最多 30 筆摘要），組成 prompt → `call_vllm`  
5. vLLM 回傳 Markdown → 轉成純文字 → 形成 `Answer` 回傳  
6. 前端得到 AI 摘要，並在搜尋結果頁面顯示。

> **注意**：為了減少等待時間， `delayed_collect` 只等待最大 3 秒（30 次 0.1 秒）。如果搜尋還沒完成，插件會先回傳「正在處理」的 placeholder；若 5 秒內仍無結果，則直接返回 placeholder 內文字。  

---

## 5️⃣ 重要屬性與方法說明

```python
class SXNGPlugin(Plugin):
    # --- 基本屬性 ---------------------------------------------------------------
    id         : str          # 唯一標識，必須與檔名相同
    name       : str          # 顯示名稱
    description: str          # 描述文字（可在 UI 內直接顯示）
    keywords   : List[str]    # 搜索關鍵字，預留組件
```

### 5.1 `__init__(self, plg_cfg: PluginCfg)`

- 初始化 `api_url`, `api_key` (若為 OpenAI service)  
- 建立 `self.info`，供 `searx` 讀取插件資訊；也讓你在 `searx.conf` 的 `preference_section` 調整 UI。

### 5.2 `pre_search(self, request, search)`

- **功能**：偵測前綴 `ai` → 清除之並設 `_ai_mode`  
- **參數**  
  * `request` – searx 的 HTTP Request  
  * `search` – search manager 对象（含 `search_query`、`result_container` 等）  
- **返回**：`True` 以讓搜尋繼續（必須）

### 5.3 `post_search(self, request, search)`

1. **判斷**：若 `_ai_mode` 為 `False` → 直接回傳空列表  
2. **建立佔位**：`Answer(answer="AI Output, ...")`，告知前端「AI 正在產生」  
3. **背景執行** `delayed_collect()`：  
   - 等待搜尋結果容器 (`container`)關閉  
   - 取 `main_results_sorted` 或 `main_results_map`  
   - 若有結果，將前 30 筆作 prompt → `call_vllm`  
   - 生成 Markdown 摘要後加入 `container.answers`。  

### 5.4 `call_vllm(text: str)`

- HTTP POST 內容示例：

  ```python
  payload = {
      "model": "openai/gpt-oss-20b",
      "messages": [{"role": "user", "content": text}],
      "temperature": 0.1,
      "max_tokens": 100000,
  }
  ```

- 可自行改成 `gpt-4`、`gpt-4o-mini` 或其他任何兼容 OpenAI 的 **vLLM** endpoint。

### 5.5 `delayed_collect` 內部實作

```python
for i in range(30):  # 3s max wait
    if getattr(container, "closed", None) or getattr(container, "_closed", False):
        break
    time.sleep(0.1)
```

- 減少多執行緒之間競爭，確保搜尋結果已完全寫入。

---

## 6️⃣ 如何啟用

1. **放置檔案**  
   把 `ai_oes.py` 放在你自己的 `searx` 插件目錄下，或直接複製到  
   `/searx/searx/engine/plugins/ai_oes.py`（如果是 local build）。

2. **修改 `searx.conf`**  
   ```yaml
   plugins:
     - ai_oes
   ```
   若 `searx` 已經存在 `preference_section`，請將 `preference_section` 加到 `PluginInfo`。

3. **重新啟動 searx**  
   ```bash
   # 若你使用 docker-compose
   docker-compose restart searx

   # 若你使用 local python
   python searx/bin/searx.py
   ```

4. **使用**  
   在搜尋欄直接輸入 `ai 會計師合約" 隨便寫個關鍵字，提示 leading AI`。

---

## 7️⃣ 配置項

如果你想覆寫預設值，可在 `searx/settings.yml` 的 `[plugins]` 區塊中, 或在 `searx` 內部自行載入 config。

**示範：**  

```yaml
plugins:
  - id: ai_oes
    api_url: http://172.20.31.7:8001/v1/chat/completions   # 你自己 vLLM endpoint
    api_key: <YOUR_OPENAI_KEY>  # 若使用外部 OpenAI，需要填寫 token
    response_timeout: 20   # 送往 vLLM 的超時秒數
```

> **說明**  
> 1. `api_url`：默認為本機 `vLLM` endpoint，亦可改成 `https://api.openai.com/v1/chat/completions`  
> 2. `api_key`：若使用 OpenAI 正式 API，必填；若使用 `vLLM` 本地部署可以留空  
> 3. `response_timeout`：5～30 秒之間均可，根據模型預測時間調整

> 若你想要修改生成摘要長度、溫度、prompt 範本，請直接調整以下片段：

```python
prompt = (
    f"以下是查詢「{query_text}」的前 3 頁搜尋結果，"
    f"請用中文撰寫重點摘要與整合結論(不要列表)：\n\n"
    + "\n".join(text_block)
)
```

---

## 8️⃣ 使用範例

| 步驟 | 範例命令或前端行為 | 期望結果 |
|------|-------------------|----------|
| 1 | `Navigator: <input value="ai 環境法 第十條"></input>` | 會在搜尋結果頁面最上方顯示「AI Output…」文字 |
| 2 | 等待 1~3 秒 | 顯示 AI 摘要，像：`AI 摘要: ...` |
| 3 | 若 5 秒內還沒推出摘要 | 仍顯示「AI is processing, please wait...」 |

**測試腳本**（可放到 `tests/ai_test.py`）：

```python
import requests, json, time

SEARCH_URL = "http://127.0.0.1:5000/search?search_query=ai%20環境法%20第十條"

resp = requests.get(SEARCH_URL)
print(json.dumps(resp.json(), indent=2, ensure_ascii=False))
```

> 你可以在這個腳本中驗證 `Answer` 是否出現在 `results` 之列表中。

---

## 9️⃣ 常見問題（FAQ）

| 問題 | 原因 | 解決方案 |
|------|------|----------|
| `AI mode is disabled` | `pre_search` 沒偵測到 `ai ` 前綴（多餘空白、大小寫不符） | 確認前綴正確、`.lower().startswith("ai ")` |
| `vLLM fail` | 無法連線至 `api_url` 或模型未啟動 | 檢查網路、防火牆、model_name 是否正確，以及 vLLM 伺服器是否在同一網路 |
| `badtoken` | token 無效或過期 | 重啟 vLLM，或確認 `api_key` 是否正確 |
| 沒有 `Answer` 或 `container.answers` 內無資料 | `delayed_collect` 等待時間不足，搜尋結果仍忙 | 延長 `max_elapsed` 或直接改為同步呼叫（將 30 次 0.1 秒改為 60 次）。 |
| `search not found` | 前端發送的 `search_query` 中含有 `?` 需要 URL encode | 使用瀏覽器自動 encode 或在程式中 `urllib.parse.quote` |

---

## 1️⃣0️⃣ Docker / Kubernetes 部署

### 重新編譯

- 此處用到了`requests`模組，需要在Docker裡面也安裝這個模組

```bash
cd /nas2/kuang/MyPrograms/searxng
echo 'requests==2.32.5' >> requirements.txt
make clean
make container.build
```
### Dockerfile 範例

```js
# Docker for searx with ai_oes plugin
FROM searx/searx:latest

RUN pip install --no-cache-dir markdown-it-py requests

# Copy plugin & enable
COPY ai_oes.py /searx/searx/engine/plugins/ai_oes.py
COPY my_searx.conf /etc/searx/settings.yml

CMD ["searx", "--ip=0.0.0.0", "--port=5000", "--debug"]
```

### Kubernetes Service

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: searx-ai
spec:
  replicas: 1
  selector:
    matchLabels:
      app: searx-ai
  template:
    metadata:
      labels:
        app: searx-ai
    spec:
      containers:
      - name: searx
        image: your-repo/searx-ai:latest
        env:
        - name: SEARX_DEBUG
          value: "true"
        - name: SEARX_API_URL
          value: "http://172.20.31.7:8001/v1/chat/completions"
        ports:
        - containerPort: 5000
```

> 將 `SEARX_API_URL` 或其他環境變數傳入 `searx/settings.yml`（可利用 `jinja2` 版 searx.conf 加載環境變數）

---

## 1️⃣1️⃣ 參考資料

| 主題 | 連結 |
|------|------|
| searx plugin API | https://github.com/searx/searx/wiki/Extending-searx |
| OpenAI chat API | https://platform.openai.com/docs/api-reference/chat |
| vLLM (OpenAI compatible) | https://github.com/vllm-project/vllm |
| Markdown‑IT‑Py | https://github.com/ckreuter/markdown-it-py |
| Python Requests | https://docs.python-requests.org/en/latest/ |

---

## 🔧 拓展方式

| 需求       | 方法                                                            |
| -------- | ------------------------------------------------------------- |
| 改成 GPT-4 | 將 `payload["model"] = "openai/gpt-4o-mini"` 或自行改寫 `call_vllm` |
| 多語言支持    | 在 `call_vllm()` 的 prompt 中動態加入 `lang` 參數                      |
| 加速摘要     | 只取 5 筆結果（將 `top_items[:30]` 改成 `[:5]`）或自訂查询條件                 |
| 語音回應     | 讀取 `answer`，呼叫 TTS 服務                                         |
| 監控       | 在每次成功/失敗時將統計寫進自訂中介層（如 `prometheus`）                           |
| 擴展AI讀取   | 將 `top_items[:30]` 改成 `[:100]`，新增`prompt:""`作為前綴，啟動完整的AI功能。   |

---

## 小結

- **AI‑OES** plugin 為 `searx` 提供「人類可讀摘要」的功能，透過 **vLLM** 模型簡單實現。  
- 只要在 `searx/settings.yml` 加載插件、設定 `api_url`，即可在搜尋框前加 `ai ` 來啟動 AI 摘要。  
- 它使用多執行緒等待搜尋結果，最大等待 3 秒，最後將 AI 摘要 `Answer` 儲存至 `container.answers`。  
- 若需調整 prompt、token 或模型，只需改寫 `call_vllm` 或 `post_search` 內的文字。  
- 若遇大數據、低延遲，請將 `delayed_collect` 改為同步或增大等待時間。  

祝你玩得開心，順利把 AI 進一步整合進搜尋平台！ 🚀