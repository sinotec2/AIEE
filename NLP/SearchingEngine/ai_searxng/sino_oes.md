---
layout: default
title: sino_oes
parent: 地端智慧搜尋引擎
grand_parent: SearchingEngine
nav_order: 4
date: 2025-11-12
last_modified_date: 2025-11-12T13:08:00
tags:
  - AI
  - OES
---

# sino_oes

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



## 🛠️ `sino_oes.py` – SearXNG 搜尋引擎介面說明

> **檔案位置**  
> `/<project_root>/searxng/searx/engines/sino_oes.py`  
> （如果你是使用 *searx-ng* 版小說化，也可以改寫為 `searx-ng/searx/engines/oes/search.py`，但內容完全相同）

> 這份檔案是一個 **==SearXNG==** 搜尋引擎（engine）模組，用來把 *http://172.20.31.7/cgi-bin/search/query.cgi* / *http://172.20.32.158:7651/cgi-bin/search/query.cgi* 內的搜尋服務，包裝成 ==SearXNG== 可識別、可顯示並可排序的結果集。

> 本文件為資料說明與操作手冊，包含：  
> * [1️⃣] 程式結構、全域資訊  
> * [2️⃣] `request` 與 `response` 的實作細節  
> * [3️⃣] 如何在 ==SearXNG== 中註冊與測試此引擎  
> * [4️⃣] 參數說明、可自動化修改建議  
> * [5️⃣] 常見問題與除錯技巧

---

## 1️⃣ 程式結構與全局變數

| 變數                              | 型別                 | 說明                                |
| ------------------------------- | ------------------ | --------------------------------- |
| `about`                         | `dict`             | 對外顯示的資訊：官方網站、是否需要 API key、回傳格式等。  |
| `categories`                    | `list[str]`        | 引擎可搜尋的類別（==SearXNG== 會用來分類）。      |
| `paging`                        | `bool`             | 是否支援「分頁」功能。                       |
| `BASE_URL`                      | `str`              | 目標搜尋 API 的基礎位址（後面會覆寫，請自行指向正確的服務）。 |
| `print(f"BASE_URL={BASE_URL}")` | 僅在加載時印出，方便開發時確認網址。 |                                   |

> **提醒**  
> 如果你部署在多個環境（測試、正式）時，請把 `BASE_URL` 放進環境變數或檔案 `settings.py`，避免在程式內直接硬編。

---

## 2️⃣ `request(**query, params)`：組裝搜尋網址

```python
def request(query: str, params: dict) -> dict:
    ...
```

### 參數

| 參數       | 型別     | 說明                                                  |
| -------- | ------ | --------------------------------------------------- |
| `query`  | `str`  | 使用者在搜尋框輸入的文字。                                       |
| `params` | `dict` | 由 ==SearXNG== 自己傳進來的額外參數，例如 `size`、`pageno`、`lang`。 |

### 回傳

`params` 的副本（實際上是同一參考）必須新增 **`url`** 鍵，包含完整的 GET URL。  
==SearXNG== 會用這個 URL 送出實際的 HTTP 請求。

### 實作流程

1. **基本參數**：固定 `dbs`、`type`。  
2. **塞入查詢字**：`search_params["q"] = query`。  
3. **符合 UI 需求**：  
   * 若 `params` 有 `size`，就轉成 `limit`；  
   * 若想支援分頁，可加 `page` 或 `p`（此程式已注註拒絕、示例）。  
4. **組裝 URL**：`url = f"{BASE_URL}?{urlencode(search_params)}"`。  
5. **寫回**：`params["url"] = url`。  
6. **回傳**：`params`。

> **自訂範例**  
> ```python
> # 若 API 需要 page 參數
> search_params["page"] = params.get("pageno", 1)
> ```
> 若你想把 `size` 轉成 `offset`，只需要改成 `search_params["offset"] = params["size"] * (params.get('pageno',1)-1)`。

---

## 3️⃣ `response(resp)`：解析轉換回應

```python
def response(resp: requests.Response) -> list[dict]:
    ...
```

### 步驟說明

1. `resp.json()` 讀取 API 回傳的 JSON。  
2. 若解析失敗，直接回傳空列表，避免程式崩潰。  
3. 對 `data["results"]` 逐筆轉為 **==SearXNG== 需要的欄位**：  
   * `title`  → `r.get("title", "")`  
   * `url`  → `r.get("url", "")`  
   * `content` → 優先取 `snippet`，若沒得就取 `content`。  
1. 可自行加入額外欄位（`tags`、`publishedDate` 等），==SearXNG== 只會使用 `title`、`url`、`content`（或 `snippet`），但其他欄位可在 UI 自訂欄位使用。

> **小技巧**  
> 你可以利用 `response` 裡面加入 `debug`，例如 `print("解析", data)`，或把除錯訊息寫入日誌檔。

---

## 4️⃣ 如何把此引擎加入 ==SearXNG==

1. **確定檔案位置**  
   把 `sino_oes.py` 放在 `searx-ng/searx/engines` 目錄下（確保可被 `import`）。

2. **在 `settings.yml` 加入**  

   ```yaml
   engines:
     - name: sino_oes   # 與檔名一致
   ```

   或者使用 `available_engine` 方式：

   ```yaml
   engines:
     - name: sino_oes
       inherit: search   # 必須有父層 'search' 的設定
   ```

3. **重新啟動 ==SearXNG==**

   ```bash
   # 若你用 Docker
   docker compose up -d searx

   # 或者直接 python
   python manage.py run
   ```

4. **測試**  
   在瀏覽器輸入搜尋框 `sino_oes:<文字>`（或直接設定搜尋器）  
   你會看到搜尋結果已經載入並顯示 `title`、`url`、`content`。

---

## 5️⃣ 可調整參數

| 參數 | 位置 | 調整方式 | 參考說明 |
|------|------|----------|----------|
| `BASE_URL` | `sino_oes.py` | 直接修改字串 | 選擇正式 / 測試環境 |
| `search_params`（`dbs`,`type`） | `request()` | 直接改寫 | 需要對應後端 API 的必要參數 |
| `size → limit` | `request()` | 在 `params` 裡寫 `limit` | 重新命名可自行調整 |
| 分頁 `pageno` | `request()` | 加 `search_params["page"] = params.get('pageno', 1)` | 若 API 支援則可啟用 |
| 回傳列的欄位 | `response()` | 直接改 `out.append({...})` | 若要顯示更多資訊可自行擴充 |

> **開發建議**  
> - 若你打算把此引擎放到生產環境，建議把 `BASE_URL` 放在環境變數 (`export SINO_OES_URL=...`) 或 `settings.py`，而非硬編。  
> - 若 API 支援 `Authorization`，可以在 `request()` 裡加入 `headers` 把 `token` 或 `api_key` 傳給 `requests.get()`。

---

## 6️⃣ 測試流程 (不經 ==SearXNG==)

如果你想快速驗證程式正否，直接執行：

```bash
python - <<'PY'
import requests, json
from urllib.parse import urlencode
BASE_URL="https://172.20.31.7/cgi-bin/search/query.cgi"

q="test"
params={"size":5}
search_params={"dbs":"default-index","type":"1","q":q}
search_params["limit"]=params["size"]
url=f"{BASE_URL}?{urlencode(search_params)}"
print("URL:",url)

resp=requests.get(url)
print(resp.json()[:2])   # 預覽前兩筆
PY
```

> 確認回傳結構與 `response()` 的處理方式一致。

---

## 7️⃣ 常見問題 (FAQ)

| 問題                             | 可能原因                                     | 建議解決方案                                                                                                                                       |
| ------------------------------ | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **搜尋結果顯示空白**                   | `BASE_URL` 指向錯誤、API 回傳空結果                | 檢查 `BASE_URL`、確認 API 真的有資料。                                                                                                                  |
| **發生 `UnicodeDecodeError`**    | 文字編碼問題                                   | 在 `requests.get(..., timeout=..., verify=False)` 前加 `response.encoding="utf-8"` 或使用 `requests.get(..., headers={"Accept-Charset":"utf-8"})`。 |
| **==SearXNG== 設定 reload 後無變化** | 聯繫不到引擎文件，或 `settings.yml` 中 `engines` 名稱錯誤 | 確認文件名 `sino_oes.py` 與 `settings.yml` 的 `name` 一致，並重啟 SearXNG。                                                                                  |
| **分頁無效**                       | API 需要 `page` 參數但程式未加入                   | 參考 3️⃣ 中「分頁」範例，將 `page=` 參數寫回 `search_params`。                                                                                               |
| **結果無翻譯**                      | `content` 欄位沒有 `snippet`                 | 查看回傳 JSON 中確實有 `snippet`；若使用其他鍵名，請修改 `response()` 的欄位選取。                                                                                     |

---

## 8️⃣ 擴充方向

| 需求 | 解決方案                                                             | 參考範例 |
|------|-----------|----------|
| **多語言回覆** | 在 `request()` 加 `lang=` 參數，並在 `response()` 取 `language`          | `search_params["lang"] = params.get("lang", "zh")` |
| **自訂欄位顯示** | 把 `tags`、`published` 裝進 `out.append({...})`，在前端設定 `label_fields` | `tags": r.get("tags", [])` |
| **多個來源合併** | 把多組引擎結果合併成一個列表，再傳給 ==SearXNG==                                   | 直接在 `response()` 內合併多重 JSON |
| **改用 HTTPX 或異步请求** | 把 `requests.get` 換成 `httpx.AsyncClient`，並在 `request()` 裡改寫為同步函式  | 需把 `request()` 改成 `async def request` 三 |

---

## 9️⃣ 部署範例（Docker）

```js
# Dockerfile (searx-ng 版)
FROM searxng/searx-ng:latest

# 安裝 requests (已內建)
# 安裝 markdown 或其他建立本機插件時所需的套件
RUN pip install requests

# 複製自訂引擎
COPY sino_oes.py /app/searx-ng/searx/engines/sino_oes.py

# 設定 settings.yml
COPY settings.yml /settings.yml

CMD ["searx", "--conf", "/settings.yml"]
```

> 只要把 `settings.yml` 裡加入：

```yaml
engines:
  - name: sino_oes
```

就能在容器內自動註冊。

---

## 📚 總結

- `sino_oes.py` 是一個 **==SearXNG== 引擎**，把 OES 搜尋 API 包裝成「==SearXNG== 可用」的 `request/response` 模式。  
- 只要改 `BASE_URL`、`search_params`、`response()` 就能對接任何兼容的搜尋後端。  
- 把它放到 `searx/engines/` 目錄，並在 `settings.yml` 裡註冊，即可在 SearXNG 前端於搜尋欄輸入 `sino_oes: <關鍵字>` 或直接選擇此引擎。  
- 設定 `paging = True` 時，可在 `request()` 裡把 `pageno` 加入 API 的「page」參數，讓 SearXNG 支援分頁。  

這樣你就可以在自己的 ==SearXNG== 實例上，快速把 OES 內的搜尋服務整合進來，並隨時偵錯、擴充。祝你順利整合、快速啟用！ 🚀