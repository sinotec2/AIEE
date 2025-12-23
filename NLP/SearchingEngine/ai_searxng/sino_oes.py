#$ cat /nas2/kuang/MyPrograms/searxng/searx/engines/sino_oes.py
# ──────────────────────────────────────────────────────
# searx/engines/oes.py   (或 searx/engines/oes/search.py)
# ──────────────────────────────────────────────────────
"""
OES
===

`search/query.cgi` 的封裝。
搜尋參數：q = 查詢字；dbs = default-index；type = 1
（如果你想在 UI 上直接讓使用者選「size」或「page」的話，可在 request() 內做對應。）
"""

import requests
from urllib.parse import urlencode

# ----------------------------------------------------------------
# 1. 基本訊息 (SearXNG 會用來顯示、分類)
about = {
    "website": "https://oes.sinotech-eng.com",
    "wikidata_id": None,
    "official_api_documentation": None,
    "use_official_api": False,
    "require_api_key": False,
    "results": "JSON"
}

# 2. 引擎能搜尋哪些類別
categories = ["news", "scientific publications", "files"]
paging = True            # UI 會顯示分頁

# ----------------------------------------------------------------
# 3. API 基地址 (包含固定的後綴)
BASE_URL = "http://172.20.32.158:7651/cgi-bin/search/query.cgi"
BASE_URL = "https://172.20.31.7/cgi-bin/search/query.cgi"
print(f"BASE_URL={BASE_URL}")

# ----------------------------------------------------------------
# 4. 第一步：組裝請求 URL
#    SearXNG 會把 `params` 這個字典傳給你，你可以在這一步拿到 `size`,
#    `pageno` 等，也可以把自己的慣用參數寫死在這裡。
def request(query, params):
    """
    Args:
        query (str): 用戶在搜尋框輸入的文字
        params (dict): SearXNG 傳進來的額外參數
            可能包含 `size`, `pageno`, `lang`, `search_exact` 等
    Return:
        dict: 這個字典必須包含 `url` 這個鍵（完整的 GET URL）
    """
    # 你自己的固定參數
    search_params = {
        "dbs": "default-index",
        "type": "1"
    }

    # 1️⃣ 將使用者的查詢字塞進去
    search_params["q"] = query

    # 2️⃣ 讓 UI 能直接調整「返回筆數」的話，可把 size 轉成 limit
    #    如果 API 支援 `limit`，可修改以下鍵名
    if params and "size" in params:
        search_params["limit"] = params["size"]

    # 3️⃣ 如果你想用 UI 的分頁功能，你可以從 params 看 pageno
    #    並把它加到 search_params 裡（例如 `page=` 或 `p=`，視 API 而定）
    #    這裡示例直接忽略（不做分頁）
    #    如果需要可自行加入：search_params['page'] = params.get('pageno', 1)

    # 4️⃣ 組裝最終請求 URL
    params["url"] = f"{BASE_URL}?{urlencode(search_params)}"

    return params

# ----------------------------------------------------------------
# 5. 第二步：解析回傳並轉成 SearXNG 需要的 dict 規格
def response(resp):
    """
    SearXNG 會把 requests.Response 傳進來，這裡負責：

    1. 讀 JSON
    2. 取出 `results` 清單並做轉換
    3. 回傳一個 list[dict]，每一個 dict 必須至少有
       `title`, `url`, `content`（或 `snippet`）
    """
    try:
        data = resp.json()
    except Exception as exc:
        # 任何解析失敗都視為「沒有結果」而不是 crash
        return []

    out = []
    for r in data.get("results", []):
        out.append({
            "title": r.get("title", ""),
            "url": r.get("url", ""),
            # API 可能用 "snippet" 或 "content"
            "content": r.get("snippet", "") or r.get("content", ""),
            # 你可自行添上更多欄位(可用於 UI 顯示)
            # "tags": r.get("tags", []),
            # "publishedDate": r.get("published", None),
        })
    return out
