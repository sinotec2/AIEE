---
layout: default
title: 原版README
parent: swirl搜尋引擎
grand_parent: 自然語言處理
nav_order: 99
date: 2023-11-04
last_modified_date: 2023-11-04 20:37:49
has_children: true
tags: AI chat report
---

# swirl README
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

### AI命令搜尋引擎的open source範例

是的，有一些開源專案提供了使用AI來實現搜尋引擎的範例。以下是一些範例：

1. **Marqo**¹：這是一個開源的向量搜尋引擎，專為AI應用程序設計。它提供了一個全面的向量搜尋智能，包括向量生成、存儲和檢索。這意味著Marqo允許用戶跳過來自OpenAI或Hugging Face等的第三方向量生成工具，通過單一的API提供所有服務。

2. **Swirl**²：這是一個用Python和Django構建的開源搜尋平台，可以無縫地統一資料庫（SQL和NoSQL）、雲服務、搜尋提供商、資料孤島和像Miro、Jira、GitHub等工具的搜尋。Swirl允許用戶進行單一查詢，立即從多個平台匯集和呈現相關數據。

3. **simple-code-search-engine-using-open-ai-api**³：這是一個使用Open AI API的簡單代碼搜尋引擎的範例。該專案提供了安裝和使用說明。

以上都是一些很好的開源範例，你可以參考他們的代碼來學習如何使用AI來實現搜尋引擎。請注意，這些專案的具體實現可能會因為你的具體需求而有所不同。

來源: 與 Bing 的交談， 2023/11/4

(1) Meet Marqo, an open source vector search engine for AI applications. [techcrunch](https://techcrunch.com/2023/08/16/meet-marqo-an-open-source-vector-search-engine-for-ai-applications/).

(2) Creating an ‍ Open Source Search Platform:[ Search Engines with AI - DEV Community](https://dev.to/swirl/creating-an-open-source-search-platform-search-engines-with-ai-swirl-2m0h).

(3) Hokid/simple-code-search-engine-using-open-ai-api: Example of simple code search engine using Open AI API - [GitHub](https://github.com/Hokid/simple-code-search-engine-using-open-ai-api).

(4) [swirlai/swirl-search](https://github.com/swirlai/swirl-search).

## Marqo and vector database

source: Meet Marqo, an open source vector search engine for AI applications, Vector generation, storage, and retrieval through a single API. by [Paul Sawers@psawers / 9:00 PM GMT+8•August 16, 2023@techcrunch.com](https://techcrunch.com/2023/08/16/meet-marqo-an-open-source-vector-search-engine-for-ai-applications/)

### 更全面的「端到端」向量搜尋

向量資料庫是現代人工智慧運動的無名英雄，它儲存圖像、影片和文字等非結構化數據，使人們和系統能夠搜尋未分類的內容。 它們對於大型語言模型 (LLM) 尤其重要，例如 GPT-4（為 ChatGPT 提供支援），這在很大程度上是由於資料庫能夠在創建或更新資料時支援即時索引和搜尋 - 這很重要用於個性化功能、推薦系統、情緒分析等。

對產生人工智慧的需求不斷增加，使無數向量資料庫新創公司成為人們關注的焦點，從而獲得了大量的現金。 光是在4 月份，我們就看到Pinecone 和Weaviate 分別籌集了1 億美元和5000 萬美元，以發展他們的向量資料庫智慧，而同月，剛起步的向量資料庫新貴Chroma 和Qdrant 分別獲得了1800 萬美元和750 萬美元的種子融資。 去年年底，Milvus 開源向量資料庫背後的核心開發者 Zilliz 鎖定了 6,000 萬美元的資金。

因此，很明顯，致力於幫助基礎設施跟上人工智慧炒作列車步伐的公司需求量很大，澳洲新創公司 Marqo 現在正在尋求利用更全面的「端到端」向量搜尋方法來利用這一點。

### 痛點

Marqo 去年 6 月在墨爾本成立，是西雅圖亞馬遜機器人部門前首席機器學習科學家 Jesse Clark 和雪梨亞馬遜網路服務 (AWS) 資料庫軟體工程師 Tom Hamer 的創意。

Marqo 的核心任務是解決非結構化資料難題，根據一些估計，非結構化資料佔所有創建資料的 90%。 隨著越來越多的人轉向生成人工智慧來回答他們的線上查詢或創建新的圖像和藝術品，這只會加劇對新工具來理解這一切的需求。

與現有的現有產品相比，Marqo 的一個核心賣點是它承諾提供開箱即用的全套向量搜尋智能，包括向量生成、儲存和檢索。 這意味著 Marqo 允許用戶繞過 OpenAI 或 Hugging Face 等第三方向量產生工具，透過單一 API 提供所有內容。

「向量搜尋很難實現——向量資料庫只是難題的一部分，開發人員發現將所有必需的元件組合在一起以建立具有最佳相關性、延遲和可靠性的基於向量的搜尋體驗具有挑戰性，」Marqo合作夥伴說。創辦人兼執行長 Tom Hamer 在給 TechCrunch 的電子郵件中解釋。 “Marqo 提供了一個端到端系統，將所有這些元件**整合在一起**，解決了開發人員的主要痛點。”

此外，搜尋系統的好壞取決於它們產生的結果，這意味著相關性、準確性和「最新性」是任何資訊儲存和檢索系統不可或缺的一部分。 Hamer 表示，這就是 Marqo 立即提供的功能。

「如果開發人員想要不斷提高搜尋結果的相關性，他們必須手動訓練新的人工智慧模型來產生向量，」他繼續說道。 “Marqo 的**持續學習技術**將允許搜尋根據用戶參與度（例如點擊、‘添加到購物車’等）自動改進，這對於電子商務和其他最終用戶搜尋用例尤其重要。”

Marqo 去年籌集了 66 萬英鎊（84 萬美元）的種子前資金，今天宣布籌集 440 萬美元的新種子資金，以加倍商業能力。 其中包括今天正式向公眾推出的新雲端服務，以補充現有的開源 Marqo 專案。

### 開源因素

與許多競爭對手一樣，Marqo 的開源精神是一種非常刻意的舉動，旨在討好開發者社區，他們能夠修補和定制產品，以確定它是否適合他們。 反過來，這意味著他們可能更有可能向公司高層推薦產品，甚至為產品開發做出貢獻。

「我堅信開源產品的開發會帶來更高品質的成果，」哈默說。 「在開源基礎上建立 Marqo 使我們能夠與用戶建立**緊密的反饋循環**，並以極快的速度迭代以建立開發人員實際需要的產品。 開源也是很好的客戶獲取管道。 客戶可以準確地看到他們所購買的商品，他們可以免費試用並確保 Marqo 適合他們的用例。”

總而言之，開源通常需要大量資源來執行生產級產品，無論是在人力投入還是基礎設施方面。 這就是 Marqo Cloud 加入競爭的地方。

「對於不需要即時搜尋且最終用戶數量較少的用戶，或者對於建立概念驗證的用戶來說，自架開源產品是一個很好的選擇，」Hamer 繼續說道。 “Marqo 的雲端平台為我們的客戶處理雲端資源的基礎設施、維護和運營，確保最佳性能和成本效率。”

雖然 Marqo 無論如何都是一家澳洲新創公司，但它在英國註冊了一家母公司，其第一個投資者 Creator Fund 就位於英國。 該公司還聲稱在倫敦設有一個小型辦事處，目前只有一名員工，不過該公司希望將其擴展為包括銷售、行銷和客戶支援的部門，以支持其在歐洲的雄心壯志。
Marqo 的種子輪融資由澳洲 VC Blackbird Ventures 領投，Creator Fund 參與，兩者均參與了種子輪前的投資。 在最新一輪融資中，Marqo 也吸引了 January Capital 和 Cohere 聯合創始人 Ivan Zhang 和 Aidan Gomez 的投資。

## Swirl

[swirlai/swirl-search](https://github.com/swirlai/swirl-search) is open source software that simultaneously searches multiple content sources and returns AI ranked results.

### 三步驟完成設定

![](https://camo.githubusercontent.com/2e8a3a2d0345b29d2163569905a9d9a832e64bf0543f63e7691a7a3a2db01a99/68747470733a2f2f646f63732e737769726c2e746f6461792f696d616765732f416e696d6174696f6e5f312e676966)

### 使用API訪問網站

![](https://camo.githubusercontent.com/c2d20d9f469ed27110309dc8e4cd7d05c9f6019cd3f7622c8676563428a1c043/68747470733a2f2f646f63732e737769726c2e746f6461792f696d616765732f416e696d6174696f6e5f322e676966)

### 目前已有端口之網站

![](https://camo.githubusercontent.com/c78c5bd5439f2291d585695efa47da696600c68064767791e9015148f4ed0a35/68747470733a2f2f646f63732e737769726c2e746f6461792f696d616765732f436f6e6e6563746f72735f322e706e67)

### 搜尋畫面

![](https://camo.githubusercontent.com/5b08179da2762bce140e78bc7d924e247093fec4d358307c84ee6d4eb0c22359/68747470733a2f2f646f63732e737769726c2e746f6461792f696d616765732f67616c6178795f75695f322e706e67)

## redis installation

- swirl的內存管理使用[redis][redis]

### gcc 9

- 會需要gcc 9(詳[Redis資料庫安裝筆記](https://hackmd.io/@suyenting/SyrcLvYyd))
  
```bash
# 首先在CentOS7上安裝gcc
sudo yum -y install centos-release-scl
sudo yum -y install devtoolset-9-gcc devtoolset-9-gcc-c++ devtoolset-9-binutils

# scl命令啟用僅在當前shell有效 退出shell後重進會回復成原本設定(即沒有gcc)
scl enable devtoolset-9 bash

# 查看gcc版本
gcc --version
# 取得Redis安裝壓縮檔
wget https://download.redis.io/releases/redis-6.0.10.tar.gz

# 解壓縮
tar xzf redis-6.0.10.tar.gz

# 切換當redis安裝資料夾路徑
cd redis-6.0.10

# 執行編譯
make
src/redis-server (will be hang)
```  

- note on NODE03:fail to update yum repo
- note on DEVP：規避c7-media找不到CDROM的錯誤。

```bash
sudo  yum --disablerepo=c7-media -y install centos-release-scl
sudo  yum --disablerepo=c7-media -y install devtoolset-9-gcc devtoolset-9-gcc-c++ devtoolset-9-binutils
```

### installatoion of docker

```bash
sudo  yum --disablerepo=c7-media -y install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo  yum --disablerepo=c7-media -y install docker-ce
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

```

### installatoion of docker-composer

>= py39

```bash
 pip install docker-compose
```

### installation of swirl

OPENAI_API_KEY without quotes

```bash
export MSAL_CB_PORT=8000
export MSAL_HOST=localhost
export OPENAI_API_KEY=‘<your-OpenAI-API-key>’
conda activate py39
docker-compose pull && docker-compose up
```

### login

Enter the username `admin` and password `password`, then click Login. ([usergiude](https://docs.swirl.today/Quick-Start.html#open-the-galaxy-ui))

admin UI -> `http://localhost:8000/admin/auth/user/`

### Terms of Service

- [source](https://swirl.today/terms-of-service/)

### Chinese AI response

1. in `./swirl/rag_prompt.py`
2. add prompts

```python
        self._prompt_text = f"Answer this query '{query}' given the following recent search results as background information. \
Do not mention that you are using the provided background information. Please cite the sources at the end of your response. \
Ignore information that is off-topic or obviously conflicting, without warning about it. \
Please answer in Tradition Chinese."
```

### use internal lan IP

1. edit `.env` and './static/api/config/default'
2. add or replace `localhost` with `200.200.32.195`

```bash
ALLOWED_HOSTS=localhost,host.docker.internal,200.200.32.195
```

```bash
kuang@DEVP /home/swirl-search
$ tail ./static/api/config/default
    "oidc": true,
    "strictDiscoveryDocumentValidation": false,
    "tokenEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/token",
    "userinfoEndpoint": "https://graph.microsoft.com/v1.0/me",
    "skipIssuerCheck": true
  },
  "webSocketConfig": {
    "url": "ws://200.200.32.195:8000/chatgpt-data"
  }
}
```

### use new providers

1. edit vi SearchProviders/xxx.json
   1. active、default、page_fetch_config_json
2. `python swirl_load.py SearchProviders/google_pse.json -u admin -p password` (xxx=`google_pse`)

```json
{
        "name": "techproducts - Apache Solr",
        "active": true,
        "default": true,
        "connector": "RequestsGet",
        "url": "http://localhost:8983/solr/{collection}/select?wt=json",
        "query_template": "{url}&q={query_string}",
        "query_processors": [
            "AdaptiveQueryProcessor"
        ],
        "query_mappings": "collection=techproducts,PAGE=start=RESULT_ZERO_INDEX,NOT=True,NOT_CHAR=-",
        "result_processors": [
            "MappingResultProcessor",
            "CosineRelevancyResultProcessor"
        ],
        "page_fetch_config_json": {
                "cache": "false",
                "headers": {
                "User-Agent": "Swirlbot/1.0 (+http://swirl.today)"
                },
                "timeout": 10
        },
    "response_mappings": "FOUND=numFound,RESULTS=response.docs",
    "result_mappings": "title=name,body=features,response",
    "credentials": "",
    "tags": [
        "TechProducts",
        "Solr",
        "Internal"
    ]
}
```

### TODO's

1. Solr results without proper links
2. prompting engineering

[redis]: https://zh.wikipedia.org/zh-tw/Redis "Redis是一個使用ANSI C編寫的開源、支援網路、基於記憶體、分散式、可選永續性的鍵值對儲存資料庫。根據月度排行網站DB-Engines.com的資料，Redis是最流行的鍵值對儲存資料庫。 維基百科"