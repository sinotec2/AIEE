---
layout: default
title: mediawiki.py
parent: 地端智慧搜尋引擎
grand_parent: SearchingEngine
nav_order: 5
date: 2025-11-12
last_modified_date: 2025-11-12T16:08:00
tags:
  - AI
  - searching
  - wiki
---
a
# `mediawiki.py` 

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



> 這份檔案是 **==SearXNG== ** 的一個 “引擎”（engine）模組，負責把 MediaWiki（擴充套件可在任何可使用 MediaWiki Action API 的 wiki 上執行搜尋）封裝成 ==SearXNG==  能直接呼叫的介面。  
> 你只需將這個檔案放到 **`searxng/searx/engines/`** 目錄下，並在 `settings.yml` 裡啟用即可。  
> 下方的說明（繁體中文）詳盡說明了檔案的結構、可設定參數、常見問題，以及範例使用方式。

---

## 1. 程式結構

| 位置 | 說明 |
|------|------|
| **about** | 引擎基本訊息（支援的語言、官方 API、是否需要 key 等）。 |
| **categories，paging，number_of_results** | ==SearXNG==  用來決定搜尋類別、是否顯示分頁以及每頁顯示數量。 |
| **搜索參數** |
| &nbsp;&nbsp;*search_type* | 近似匹配(`nearmatch`)、全文(`text`) 或標題(`title`)。 |
| &nbsp;&nbsp;*srenablerewrites* | 是否在 Sigma 內部重新寫入 query。 |
| &nbsp;&nbsp;*srsort* | 排序方式。 |
| &nbsp;&nbsp;*srprop* | 要回傳的欄位（預設會包含摘要、標題、時間、分類）。 |
| **基礎 API** – *base_url*, *api_path*, *timestamp_format* | 這裡已預設為 `https://{language}.wikipedia.org/`，如果你要使用其他 MediaWiki wiki，只需更改這兩個參數即可。 |
| **request(query, params)** | 把 ==SearXNG==  的參數（query、頁碼、語言等）轉成真正的 GET URL。 |
| **response(resp)** | 把 API 回傳的 JSON 解析成 ==SearXNG==  渲染需要的 dict。 |

> **備註**  
> 只要 **不要** 改動 `request()` 與 `response()` 內的 base_url / api_path 之外的資料，程式即可在任何 MediaWiki 站點運作。  

---

## 2. 參數說明

| 參數 | 值型別 | 備註 |
|------|--------|------|
| **base_url** | `str` | 基本 URL，包含瀏覽器會面向的參數 `https://{language}.wikipedia.org/`。若你想搜尋自己的 wiki，改成 `https://wiki.com/`。 |
| **api_path** | `str` | API 框架的路徑，預設為 `w/api.php`。 |
| **timestamp_format** | `str` | `datetime.strptime()` 所使用的時間格式。 |
| **search_type** | `str` | `nearmatch`（近似）/`text`（全文）/`title`（單字標題）。 |
| **srenablerewrites** | `bool` | 是否使用 MediaWiki 自動寫法。 |
| **srsort** | `str` | 排序方式，預設 `relevance`。 |
| **srprop** | `str` | 回傳哪些欄位，預設 `sectiontitle|snippet|timestamp|categorysnippet`。 |
| **number_of_results** | `int` | 每頁回傳幾筆（預設 5）。 |

> **進階**  
> 你可以在 `settings.yml` 裡給引擎寫一份「專屬設定」，如下：

```yaml
engines:
  - name: mediawiki
    base_url: https://wiki.example.com/
    api_path: /custom_api.php
    search_type: text
    srsort: last_edit_desc
    number_of_results: 10
```

==SearXNG== 在載入時會把這些設定覆寫模組內的 GLOBAL 變數。

---

## 3. 如何在 ==SearXNG==  內使用

1. 把 `mediawiki.py` 複製到 **`searxng/searx/engines/`**。  
   ```bash
   cp mediawiki.py searxng/searx/engines/
   ```

2. 編輯 **`settings.yml`**（或你自己的 config 檔）：

   ```yaml
   engines:
     - name: mediawiki      # 必須和檔案名稱配對
     #   base_url: https://wiki.example.com/
   categories:
     - general
   ```

3. 重啟 ==SearXNG== ，確認此引擎已被載入：

   ```bash
   docker compose restart searx      # 若是 Docker
   # OR
   python manage.py run              # 若是 local
   ```

4. 打開瀏覽器，搜尋框輸入 `mediawiki: 搜尋關鍵字`（或直接把「mediawiki」設為預設搜尋器），即可看到 Wikipedia（或其他 MediaWiki）頁面的結果。  
   ![UI 渲染範例](https://user-images.githubusercontent.com/xxxxxx/example.png)

---

## 4. `request()` & `response()` 內部流程

### request(query, params)

1. **語言處理**  
   - 為了避免未設定語言，此處把 `language='all'` 轉成 `en`。  
   - `params['language']` 會被寫回，後續在 `response()` 中使用。  

2. **URL 組裝**  
   - `api_url = f"{base_url.rstrip('/')}/{api_path}?".format(language=params['language'])`  
   - `args` 包含整個 MediaWiki API 的參數。  
   - 如需要分頁，`sroffset = offset` 會自動設定。  

3. **結合參數**  
   - `params['url'] = api_url + urlencode(args)`  
   - `url` 完整包括 query string，==SearXNG==  直接用它呼叫。  

> **說明**  
> *如果你想支援前端「結果數量」或「排序」等功能，只要把相應參數寫進 `args` 或在 `request()` 接收 `params` 並改寫即可。*

### response(resp)

1. `search_results = resp.json()`  
2. 防止沒有結果：`if not search_results.get('query', {}).get('search'): return []`  
3. 逐筆處理  
   - 省略以 `#REDIRECT` 開頭的結果  
   - 解析 `title`, `sectiontitle`, `snippet`, `categorysnippet`, `timestamp`  
   - `url` 直接組合成: `base_url.format(language=resp.search_params['language']) + 'wiki/' + quote(title)` → 如果包含 section, 加上 `#section`  
4. 轉成 `date` 或保持字符串

結果必須返回一個 `list[dict]`，每個 dict 至少有 `title`, `url`, `content`, `metadata`。若需要在前端顯示分頁、作者或時間，別忘加 `publishedDate`。

---

## 5. 常見問題

| 問題 | 圖片 | 原因 | 解決 |
|------|------|-----|------|
| 搜尋結果**空白** |  | 1️⃣ API 失敗  2️⃣ `base_url`/`api_path` 不對  3️⃣ “language” 未設定 | 檢查 `base_url` 是否正確；執行 `curl <url>` 看回傳；在 config 設 `language=zh` 或其他可用語言。 |
| **類似錯誤**： `#REDIRECT` 暴露在結果 |  |  MediaWiki 會為 redirect 頁面增添標題 `#REDIRECT` | `response()` 已過濾。若你還想保留請刪除 `continue` 這一行。 |
| **分頁不工作** |  |  ==SearXNG==  內 `pageno` 參數未送給 MediaWiki | 在 `request()` 裡加入 `args['sroffset'] = offset`（已包含）並確保 `number_of_results` 小於等於 `srlimit`。 |
| **時間格式錯誤** |  |  目前解析 `timestamp` 只支援 `timestamp_format` 的長度 | 根據自己的 wiki 調整 `timestamp_format` 例如 `'%Y-%m-%dT%H:%M:%SZ'` 或其他。 |

---

## 6. 擴充 & 自訂範例

### 6.1 歸檔異常處理

如果你想直接在 Debug 模式下給使用者看原始 API 回應：

```python
def response(resp):
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
```

> 但這會把整個 HTTP 異常拋到 ==SearXNG== ，請確保你的錯誤處理符合需求。

### 6.2 其它 MediaWiki 站點

假設你有一個本地自建的 wiki `https://wiki.local/`，只需把 `base_url` 改成 `https://wiki.local/`，並把 `api_path` 改成 `/api.php`（如果是預設的話可忽略）。

```yaml
engines:
  - name: wiki_local
    base_url: https://wiki.local/
    api_path: w/api.php
    search_type: text
```

### 6.3 支援多語言切換

==SearXNG==  允許在搜尋框直接寫 `lang:zh` 或 `language:zh`，這時 `params['language']` 會被寫入。你可以將 `srsort` 或 `search_type` 依照語言改寫。在 `request` 裡加入：

```python
if params.get("language") == "zh":
    args['srwhat'] = 'text'
else:
    args['srwhat'] = 'nearmatch'
```

---

## 7. 部署範例

```bash
# 1. 建立子目錄
mkdir -p searxng/searx/engines
cp mediawiki.py searxng/searx/engines/

# 2. 配置
cat >> searxng/settings.yml <<EOF
engines:
  - name: mediawiki
EOF

# 3. 重新啟動
docker compose up -d searx
```

> 若你使用的是 GitHub Actions / k8s，直接把 `mediawiki.py` 放在容器里就行。

---

## 8. 參考資料

| 主題 | 連結 |
|------|------|
| MediaWiki Action API | https://www.mediawiki.org/wiki/API:Main_page |
| list=search 模組 | https://www.mediawiki.org/w/api.php?action=help&modules=query%2Bsearch |
| timestamp 參數 | https://www.mediawiki.org/w/api.php?action=help&module=srlist[?] |
| ==SearXNG==  參數 | https://github.com/searxng/searxng |

---

### 小結  

- **`mediawiki.py`** 是一個 **高度可配置** 的 ==SearXNG==  搜尋引擎：只要改 `base_url` 或 `api_path`，就能支援任何 MediaWiki 站點。  
- 它實作了 `request()` 與 `response()` 兩個接口，負責組裝 Http URL 以及解析回傳資料。  
- 可以在 `settings.yml` 裡加進去、重啟服務，然後就能在搜尋框裡輸入 `mediawiki:關鍵字` 或直接把它設為預設搜尋引擎。  
- 透過 `search_type`, `srsort`, `srprop` 可以微調返回內容。  
- 如需更進一步的調整（多語言切換、自訂分頁）、只要在 `request()` 內改寫即可。  

祝你使用愉快，快速將 MediaWiki 內容映射到全站搜尋平台！ 🚀