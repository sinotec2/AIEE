---
title: LibreChat 上網搜尋🗃️
tags: AI
layout: default
parent: LibreChat
grand_parent: Utilities
nav_odrer: 5
date: 2025-11-01
modify_date: 2025-12-12T18:08:00
---

# LibreChat 上網搜尋🗃️


> 如何讓 LibreChat 連結 searXNG 並且搜尋 OES 資料庫 🧩

::: info

本文根據與Sonnet4.5/GPT5.1 的實作與對話過程，整理成一份技術摘要，說明如何：

1. 讓 **LibreChat** 透過 **searXNG** 搜尋
2. 使用**searXNG**自訂的 **OES engine**（`sino_oes`）查詢本地 OES 資料庫
3. 避免走外網，只透過 OES engine 回傳結果

:::

---

## 整體架構概觀 🏗️

最終目標的資料流是：

**使用者 → LibreChat →（OES 工具）→ searXNG → OES engine (`sino_oes`) → 回應 LibreChat**

關鍵點：

- searXNG 內已有一個自訂 engine：`sino_oes`（name: `sino oes`）
- searXNG 加上一個 plugin：`oes_route`  
    當 query 以 `OES::` 開頭時，**只啟用 `sino oes` engine**
- LibreChat 不再直接把一般 query 當 web search 丟出去，而是用一個 **OES 專用工具**  
    並配合system prompt，**保留／正確處理 `OES::` 前綴**

---

## searXNG 端：OES engine 與 `oes_route` plugin ⚙️

### 1. 自訂 OES engine：`sino_oes` / `sino oes`

在 `settings.yml` 的 `engines:` 區塊中已有一個自訂 engine，設定如下：

```yaml
engines:
  - name: sino oes          # 供 EngineRef 使用的 name
    engine: sino_oes        # 對應到你的 sino_oes.py
    shortcut: oes
    disabled: false
    enable_http: true
    categories: [general]   # 要能在 general 搜尋中被使用
```

- `name: sino oes`：之後在 plugin 裡用這個 name 過濾 `engineref_list`
- `categories: [general]`：保證在一般搜尋中可以選用
- `shortcut: oes`：可以用 `!oes xxx` 測試這個 engine 是否正常運作

### 2. 問題：預設 `engineref_list` 沒有 `sino oes` ❌

從 debug log 可以看到，某次搜尋的 `engineref_list` 長這樣：

```python
'engineref_list': [
  EngineRef('wikipedia', 'general'),
  EngineRef('currency', 'general'),
  EngineRef('wikidata', 'general'),
  EngineRef('duckduckgo', 'general'),
  EngineRef('google', 'general'),
  EngineRef('lingva', 'general'),
  EngineRef('startpage', 'general'),
  EngineRef('dictzone', 'general'),
  EngineRef('mymemory translated', 'general'),
  EngineRef('brave', 'general')
]
```

其中 **沒有 `sino oes`**，所以就算已經設有 `sino_oes` engine，也不會在第一時間被自動使用(這個版本的特色)。

---

### 3. `oes_route` plugin：把 OES 查詢路由到 `sino oes` 🚦

我們在 searXNG 寫了一個 plugin（例如 `oes_route`），其核心邏輯是：

1. 偵測 query 是否以 `OES::` 開頭
2. 去掉 `OES::` 前綴，更新 `search.search_query.query`
3. 強制把 `engineref_list` 改成只包含 `sino oes`

精簡版的 `pre_search` 可以長這樣：

```python
def pre_search(self, request, search):
    q = getattr(search.search_query, "query", "")
    if not isinstance(q, str):
        return True

    q_stripped = q.strip()
    if not q_stripped.upper().startswith("OES::"):
        return True

    # 1. 去掉 OES:: 前綴
    new_q = q_stripped[len("OES::"):].strip()
    search.search_query.query = new_q
    setattr(search, "_oes_mode", True)

    engineref_list = getattr(search.search_query, "engineref_list", [])
    logger.debug("[OES_ROUTE] engineref_list before: %r", engineref_list)

    new_engineref_list = []

    # 2. 先嘗試從現有 engineref_list 中找 name == "sino oes"
    for er in engineref_list:
        name = getattr(er, "name", None)
        if name is None and isinstance(er, (list, tuple)) and len(er) >= 1:
            name = er[0]
        if name == "sino oes":
            new_engineref_list.append(er)

    # 3. 如果找不到，就 clone 一個 EngineRef 出來
    if not new_engineref_list:
        if engineref_list:
            template = engineref_list[0]
            try:
                category = getattr(template, "category", None)
                if category is None and isinstance(template, (list, tuple)) and len(template) >= 2:
                    category = template[1]
                if category is None:
                    category = "general"

                new_er = type(template)("sino oes", category)
                new_engineref_list = [new_er]
                logger.debug("[OES_ROUTE] created new EngineRef for 'sino oes': %r", new_er)
            except Exception as e:
                logger.warning(
                    "[OES_ROUTE] failed to clone EngineRef for 'sino oes' from template %r, error=%r; keep original list",
                    template,
                    e,
                )
                new_engineref_list = engineref_list
        else:
            logger.warning("[OES_ROUTE] engineref_list is empty, cannot inject 'sino oes'")
            new_engineref_list = engineref_list

    search.search_query.engineref_list = new_engineref_list

    logger.debug(
        "[OES_ROUTE] OES mode on. query=%r, engineref_list after=%r",
        new_q,
        getattr(search.search_query, "engineref_list", None),
    )
    return True
```

重點說明：

- **前綴判斷**：只對 `OES::`（大小寫不分）開頭的查詢生效
- **去掉前綴**：實際搜尋關鍵字是 `OES::` 後面的內容（例如「曠**」）
- **EngineRef 處理**：
    - 若 `engineref_list` 已有 `sino oes`，只保留它
    - 若沒有，就用 `engineref_list[0]` 當樣板 `template`，  
        建一個 `type(template)("sino oes", category)` 的新 `EngineRef` 放進去
    - 避免直接 import `EngineRef`，保持對 searXNG 版本的相容性

如此一來，當 `query = "OES:: 曠**"` 時：

- plugin 會把 query 改成 `"曠**"`
- 並把 `engineref_list` 改為只剩 `[EngineRef('sino oes', 'general')]`
- 後續只有 OES engine 會被呼叫 ✅

---

## LibreChat 端：避免 OSS 把 `OES::` 當雜訊 🧠

### 問題

遇到的問題是：LibreChat／LLM 在看到使用者輸入：

```text
"oes:: 曠**"
```

時，模型(GPT-OSS)自己推理：

> "The user says: `oes:: 曠**`. It looks like someone is requesting info about the Chinese name 曠**...  
> We need to search the web. Let's search for 曠**."

等於：

- 把 `oes::` 當成奇怪字串
- 自動改寫成普通 web 搜尋
- **沒讓 query 帶著 `OES::` 前綴** 傳到 searXNG

### 解法：用 System Prompt 鎖死 `OES::` 行為 🔐

在 LibreChat 的 System Prompt 中加入清楚的規則，像這樣（我們最後成功的做法）：

```text
【OES 查詢規則】

1. 使用者輸入如果以「OES::」或「oes::」開頭，這是一個 **特殊前綴**，用來指定要查詢 OES 資料庫。
2. 對於這種輸入，你必須：
   - 保留這個前綴，不要刪除、不解釋、不改寫。
   - 不要把整句話改成「看起來像是在找某個人，我們去網路搜尋」，也不要幫它改成其他自然語言問句。
3. 當你需要對帶有「OES:: / oes::」前綴的內容進行搜尋時：
   - 優先使用「OES 專用搜尋」工具（例如名為 `oes_search` 的工具），
   - 並將 `OES::` 後面的內容當作查詢字串傳給該工具。
4. 帶有「OES:: / oes::」前綴的輸入 **禁止** 使用一般的「web search」或「網路搜尋」工具。
5. 不要試圖推測「OES:: 是什麼縮寫」或寫出類似：
   - "It looks like someone is requesting info about..."
   - "We need to search the web. Let's search for ..."
   這樣的文字。遇到 OES 前綴，只要照上述規則處理即可。
```

這段 prompt 的效果：

- 阻止模型把 `OES::` 視為「奇怪的程式語言／library prefix」並擅自解釋
- 明確告訴模型：**看見 `OES::` 就啟用 OES 專用路徑，不要走 web search**

實際測試後，也證實「光靠 prompt 調整就成功」，不需要另外再寫甚麼工具。✅

---

## LibreChat 與 searXNG 的環境設定調整 🧩


除了程式與 prompt 之外，要讓 LibreChat 穩定透過 searXNG 查詢 OES 資料庫，實務上還需要對：

- LibreChat 的 **`.env`**
- searXNG 的 **`settings.yml`**

做一些對應調整。這些設定主要確保：

1. LibreChat 正確連到你的 searXNG 服務（而不是外部網路的搜尋 API）
2. searXNG 真的啟用你的 `sino_oes` engine 與 `oes_route` plugin
3. OES engine 被歸類在正確的類別（`general`），能被路由插件選到

以下用「範例形式」說明，實際名稱請依你環境微調。

---

### 1. LibreChat `.env`：指向本機 searXNG 🧪

在 LibreChat 的 `.env`（或等價的環境設定檔）中，你應該有類似這樣的設定，告訴 LibreChat：

- searXNG 的 base URL
- 是否啟用這個 search backend

例如：

```env
# searXNG base URL（依你的實際 host / port 調整）
SEARCH_SEARXNG_ENABLED=true
SEARXNG_ENABLED=true
SEARXNG_INSTANCE_URL=http://***/searxng
JINA_API_KEY=***
# 如果 LibreChat 有多個 search provider，這裡可以指定 searXNG 為預設
SEARCH_PROVIDER=searxng
```

幾個重點：

- **BASE_URL 一定要指向你那個有 OES plugin 的 searXNG 實例**
    - 若你同時跑「一個純外網搜尋版」和「一個帶 OES 的本地版」，要確保 LibreChat 用的是後者
- 若 LibreChat 本身還有其他外部搜尋（例如 DuckDuckGo / Bing / Google），  
    你可以：
    - 關掉那些 provider，或
    - 在工具層清楚區分「web_search」與「oes_search」，避免混用

你實際上已做了這類調整，因此當 LibreChat 呼叫 search 工具時，其實是打到「你自架的 searXNG + OES plugin」，而不是直接外網 API。

---

### 2. searXNG `settings.yml`：啟用 OES engine 與 plugin ⚙️

在 searXNG 的 `searx/settings.yml` 中，有幾個關鍵小修改。

#### 2.1 啟用並歸類 `sino_oes` engine

在 `engines:` 區塊中新增（或確認存在）類似這段：

```yaml
engines:
  - name: sino oes          # EngineRef 使用的名稱
    engine: sino_oes        # 對應你寫的 sino_oes.py
    shortcut: oes
    disabled: false
    enable_http: true
    categories: [general]   # 非常重要：屬於 general 類別
```

關鍵點：

- `name: sino oes`
    - plugin 會用這個字串來篩選(添加) `engineref_list` 中的項目
    - 你後面 `EngineRef('sino oes', 'general')` 也是用這個名字
- `engine: sino_oes`
    - 必須對應到 `searx/engines/sino_oes.py`（或你實際放置的 module 名）
- `categories: [general]`
    - 你的 OES 查詢是一般文字查詢（非 image / news），因此必須掛在 `general` 類別下
    - 這樣 `OES::` 查詢在 general context 中才找得到 OES engine

#### 2.2 啟用 `oes_route` plugin

在 `settings.yml` 的 `plugins:` 區塊，新增或開啟你的路由插件：

```yaml
plugins:
  - name: oes_route
    enabled: true
    # 若有其他參數，可在此補充
```

或在 plugins 列表中，將 `oes_route` 那一行的 `disabled: true` 改為 `false` 或移除掉。

只要這個 plugin 在 searXNG 啟動時被載入：

- 它會攔截 `pre_search`
- 看到 query 以 `OES::` / `oes::` 開頭，就會：
    - 去掉前綴
    - 強制改寫 `engineref_list` 為「只含 `sino oes`」

#### 2.3 search的回傳格式

在 `settings.yml` 開頭的 `search:` 區塊有對回傳格式的設定，一定要新增`json`：

```yaml
search:
...
  formats:
    - html
    - json
```


---

### 3. 最後的驗證流程 🧪✅

整合 `.env` 與 `settings.yml` 調整之後，可以再跑一輪 end-to-end 測試：

1. **LibreChat `.env`**
    
    - 確認 `SEARCH_SEARXNG_BASE_URL` 指向你 OES 版 searXNG
    - 若有多個 search provider，確定 searXNG 在你需要的情境中被選中
2. **searXNG `settings.yml`**
    
    - `engines:` 有 `sino oes`，`categories: [general]`
    - `plugins:` 有 `oes_route`，`enabled: true`
3. **實際查詢**
    
    - 在 LibreChat 輸入：`OES:: 曠**`
    - 檢查 searXNG log：
        - 有 `OES_ROUTE` plugin 的 debug：  
            [OES_ROUTE] OES mode on. query='曠', engineref_list after=[EngineRef('sino oes', 'general')]
        - 只有 `searx.engines.sino oes` 的 log
        - 沒有 google / duckduckgo / brave 等外網 engine

一旦這三層都正確，你就完成了：

> LibreChat `.env` → searXNG `settings.yml` → `oes_route` plugin → OES engine  
> 一條完整、只走本地 OES 資料庫、不打外網的搜尋路徑 🎯

---

如果你願意，之後我們也可以再寫一個「**完整部署 checklist**」版，把：

- `.env` 範例
- `settings.yml` 片段
- plugin 架構
- prompt 規則

整理成一頁表格，給未來你自己或其他人照表抄一遍就能部署。
---
## 進一步強化：在 LibreChat 定義 OES 專用工具 🧰

雖然你目前靠 prompt 已經能穩住行為，但為了結構更清楚，可以額外做：

1. 在 LibreChat 工具列表中定義一個 `oes_search` 工具
2. 由後端把呼叫轉成 `q=OES:: {user_query}` 丟給 searXNG

### 1. Tool 定義（範例）

（依你實際的 LibreChat 格式調整）

```jsonc
{
  "name": "oes_search",
  "description": "Search the local OES corpus via searXNG. Use this instead of general web search for OES:: queries.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The query string for OES, without the OES:: prefix."
      }
    },
    "required": ["query"]
  }
}
```

### 2. 後端 handler：包一層 `OES::` 前綴

```python
import requests

def handle_oes_search_tool(query: str):
    searxng_query = f"OES:: {query}"

    resp = requests.get(
        "http://localhost:8888/search",
        params={
            "q": searxng_query,
            "format": "json",
        },
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()
```

### 3. 和 Prompt 結合

在 System Prompt 補充：

```text
When the user input starts with `OES::` or `oes::`:
- Remove only the prefix.
- Call the `oes_search` tool with the remaining string as the `query`.
- Do not call any generic web search tool for these queries.
```

如此一來，路線就非常乾淨：

- 使用者：`OES:: 曠**`
- LibreChat：遵守 prompt → 用 `oes_search` 工具，傳 `"曠**"`
- 後端：`q="OES:: 曠**"` → searXNG
- searXNG：`oes_route` plugin 啟動，**只跑 `sino_oes`**

---

## 驗證成功的方式 ✅

你可以透過 searXNG log 來確認整條路是否正確：

1. 在 LibreChat 輸入：`OES:: 曠**`
2. 檢查 searXNG log 會看到：
    - `OES_ROUTE` plugin 啟動：
        
        ```text
        [OES_ROUTE] OES mode on. query='曠**', engineref_list after=[EngineRef('sino oes', 'general')]
        ```
        
    - 只有 OES engine：
        
        ```text
        DEBUG   searx.engines.sino oes  : ...
        ```
        
    - 沒有：
        
        ```text
        DEBUG   searx.engines.googleDEBUG   searx.engines.duckduckgoDEBUG   searx.engines.brave...
        ```
        

只要滿足以上，代表：

- LibreChat 沒「吃掉」`OES::` 前綴
- searXNG 的 plugin 正確改寫 `engineref_list`
- 查詢只打本地 OES 資料庫，而非外網 🌐❌

---

## 小結 🎯

從我們的過程看下來，「讓 LibreChat 連結 searXNG 並搜尋 OES 資料庫」的關鍵有三：

1. **searXNG 端**
    
    - 有自訂的 OES engine（`sino_oes` / `sino oes`）
    - 有 `oes_route` plugin，辨識 `OES::` 前綴並強制只跑 `sino oes`
2. **LibreChat 端**
    
    - 用 System Prompt 清楚定義 `OES::` 前綴行為，禁止模型誤解／改寫
    - 避免把 `OES::` 查詢丟給一般 web search 工具
3. **（可選）OES 專用工具**
    
    - 定義 `oes_search` 工具
    - 後端封裝：統一把 query 轉成 `q=OES:: xxx` 給 searXNG

現在已經成功讓整條路跑起來 🎉  

TODO：如果之後想把這套再擴充成：  
「OES 搜尋 → 自動摘要 → 回 LibreChat」，或加上多種前綴（例如 `KB::`, `DOCS::`），可以再一起設計下一層架構。

## 畫面

![](pngs/Pasted%20image%2020251212134648.png)


![](pngs/Pasted%20image%2020251212134711.png)