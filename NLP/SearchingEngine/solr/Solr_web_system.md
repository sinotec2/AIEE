---
layout: default
title: Solr web system
parent: solr
grand_parent: SearchingEngine
nav_order: 99
date: 2023-11-01
last_modified_date: 2023-11-01 09:01:10
tags: AI chat report
---

# Solr web system
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

- 參考網友提供的程式碼及筆記：[Apache Solr for Web Search](https://jekhokie.github.io/solr/docker/flask/docker-compose/2020/06/24/apache-solr-web-search.html)

## flask_up.py

### 系統架構

- `flask_up`存放在根目錄(`$SOLR_HOME`)
- `index.html`存放在`$SOLR_HOME/templates`下
- 需使用py38以上版本([flask pypi](https://pypi.org/project/Flask/))
- 確定solr及collection都可以匹配。

### 執行

- `python flask_up.py`
- 到 http://127.0.0.1:5000或http://200.200.31.47:5000上鍵入`DataField:Key`即可搜尋
  - DataField：即為csv的橫欄名稱，如film collection之`["id",
      "directed_by","initial_release_date","genre","name","film_vector","_version_"]`等項目
  - Key:欲尋找之目標

![](2023-11-01-13-45-18.png)

### 說明

這段程式碼描述了一個基於 Flask 的網頁應用，用於與本地運行的 Solr 服務互動，進行搜尋和顯示搜尋結果。Solr 是一個流行的、開源的搜索平臺。

**主要功能**：

1. **基本設置**：程式首先導入了所需的模組，然後創建了 Flask 應用實例。定義了 Solr 服務的基本 URL 路徑 `BASE_PATH`。

2. **首頁路由** (`/`)：當用戶訪問應用的首頁或提交一個搜尋請求時，該路由被觸發。

    - 如果使用 GET 請求，應用僅返回一個輸入欄供用戶輸入查詢。
    - 如果使用 POST 請求（用戶已經提交了查詢），則程式會根據用戶的查詢請求 Solr 服務，並將結果顯示在首頁上。
  
    在該路由的邏輯中，用戶的查詢從表單中提取出來，並用於請求 Solr 服務。如果用戶沒有輸入查詢，則返回所有結果(`*:*`)。

3. **啟動伺服器**：程式最後的部分是啟動 Flask 伺服器的代碼，設定為在所有 IP 上運行 (`0.0.0.0`)。

**注意事項**：

1. 在生產環境中，將 Flask 應用設置為在 `0.0.0.0` 上運行可能是不安全的，因為它允許任何人訪問應用。
   1. 最好使用像 [Gunicorn](#gunicorn) 這樣的生產級 WSGI 伺服器，並通過反向代理（例如 Nginx）提供服務。
   2. `flask`內設的通訊端(port)是5000，如果需要更改（mac的5000是預留給其他程式用途），需在`app.run()`內加註，如：`app.run(host='0.0.0.0', port=5001)`
  
2. 這段程式碼假定有一個名為 `index.html` 的模板，用於渲染首頁。你應該在你的 Flask 應用的 "templates" 目錄下有這個文件。

3. 用戶輸入應該經過驗證和清理，以防止潛在的安全問題，例如注入攻擊。

4. 確保 Solr 服務在指定的 `localhost:8983` 上運行且有一個名為 `films` 的 collection。
5. url寫中文的問題：參考[使用python對url編碼解碼](https://www.796t.com/content/1545641490.html)，該版本是python2,對python3而言，要改成`from urllib.parse import quote`。

### 程式碼

```python
import flask
from urllib.request import urlopen
import simplejson
from urllib.parse import quote

app = flask.Flask(__name__)

BASE_PATH='http://localhost:8983/solr/films/select?wt=json&q='

@app.route('/', methods=["GET","POST"])
def index():
    query = None
    numresults = None
    results = None

    # get the search term if entered, and attempt
    # to gather results to be displayed
    if flask.request.method == "POST":
#        query = flask.request.form["searchTerm"]
        query = quote(flask.request.form["searchTerm"])


        # return all results if no data was provided
        if query is None or query == "":
            query = "*:*"

        # query for information and return results
        connection = urlopen("{}{}".format(BASE_PATH, query))
        response = simplejson.load(connection)
        numresults = response['response']['numFound']
        results = response['response']['docs']

    return flask.render_template('index.html', query=query, numresults=numresults, results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')#,port=5000)
```

## interfaces

### html

這個 HTML 文件是一個使用 Flask 和 Solr 的搜尋頁面範例。

1. 首先,它匯入了 Bootstrap CSS 樣式,以美化頁面樣式。
2. 然後它有一個表單,可以讓用戶輸入搜尋詞條,並提交表單到根路由 '/'。
3. 在 Flask 路由中,它會從表單獲取搜索詞條,然後調用 Solr 進行搜尋,並獲取結果。
4. 它使用 Jinja2 模板語句顯示結果的數量,如果有結果的話,會顯示結果列表。
5. 列表顯示 Solr 中每個文件的一些字段,比如 ID、名稱、庫存狀態和價格。

這樣就可以實現一個簡單的 Solr 搜索頁面。當用戶提交搜尋時,它會調用 Solr API,並在頁面上顯示匹配的結果。

Flask 提供了路由和視圖,而 Solr 提供了全文搜尋功能。通過將兩者結合,可以快速構建搜索應用。

這個例子中使用的是 Solr Python 客戶端,也可以使用 Flask-Solr 擴展來更方便的整合 Solr。

```html
s
```

### without html

這裡是一些在 Flask 中整合 Solr 搜尋的方法:

1. 使用 Solr Python 客戶端連接 Solr,執行搜尋,並獲取結果。在 Flask 路由中,可以這樣做:

```python
from solr import SolrClient

@app.route('/', methods=['GET', 'POST'])
def search():
  search_term = request.form.get('searchTerm')
  
  solr = SolrClient('http://localhost:8983/solr/')
  results = solr.query(search_term)

  return render_template('results.html', results=results)
```

2. 使用 Flask-Solr,一個用於整合 Solr 的 Flask 擴展。你可以創建一個 Solr 實例,執行搜尋並返回結果:

```python
from flask_solr import Solr

app.config['SOLR_URL'] = 'http://127.0.0.1:8983/solr'
solr = Solr(app)

@app.route('/', methods=['GET', 'POST'])  
def search():
  search_term = request.form.get('searchTerm')
  results = solr.search(search_term)
  return render_template('results.html', results=results)
```

3. 直接從 Flask 索引數據到 Solr,通過發送更新請求來添加、删除或更新文檔。

```python
from flask import request 
import requests

@app.route('/add')
def add_document():
  doc = {'id':1234, 'name': '產品'}
  requests.post('http://localhost:8983/solr/update', data=doc)
  return '新增文件!'
```

總結來說,你可以從 Flask 查詢 Solr,或者使用 Flask 管理索引到 Solr 的數據。Python Solr 客戶端或 Flask-Solr 擴展使得整合兩者變得簡單。

### Query UI

在 Solr 的使用者介面（UI）中，你可以使用各種參數來建立和執行查詢，*這些關鍵詞也可以用在RESTful API的指令中*。 以下是一些常用的參數及其意義：

1. **q（Query）參數**：這是用來指定查詢字串的參數。 你可以在這裡定義你的搜尋查詢，以符合文件中的內容。 例如：

    ```
    q=title:Solr AND content:Lucene
    ```

    這個查詢會符合標題(title)中包含 "Solr" 並且內容(content)包含 "Lucene" 的文件。

2. **df（Default Field）參數**：用於指定預設的搜尋欄位。 如果你沒有在查詢中明確指定字段，Solr 將使用該字段來搜尋。 例如：

    ```
    df=text
    ```

    這將預設搜尋 "text" 欄位。

3. **fq（Filter Query）參數**：用於新增過濾查詢，以限制搜尋結果的範圍。 過濾查詢不會影響搜尋評分，但可以用於篩選結果。 例如：

    ```
    fq=category:Electronics
    ```

    這將過濾出類別為 "Electronics" 的文件。

4. **sort（Sort）參數**：用於指定結果的排序順序。 你可以按升序（asc）或降序（desc）對欄位進行排序。 例如：

    ```
    sort=price desc
    ```

    這將按價格欄位降序排序。

5. **fl（Field List）參數**：用於指定在搜尋結果中包含哪些欄位。 預設情況下，Solr 會傳回所有字段，但你可以使用 `fl` 參數來指定要傳回的字段清單。 例如：

    ```
    fl=id,title,price
    ```

    這將只傳回文件的 ID、標題和價格欄位。

這些參數可以組合使用，以建立複雜的查詢。 你可以根據你的需求來使用這些參數，以實現你的搜尋功能。

此外，Solr 還提供了更多的進階功能和參數，例如分頁、高亮顯示、facet（分面搜尋）等，以滿足各種搜尋需求。 在 Solr 的使用者介面中，你可以使用 Query 和 Filter Query 部分來建立和調試你的查詢，然後在查詢結果中查看匹配的文檔。

## 名詞解釋

### Gunicorn

[Gunicorn](https://gunicorn.org/)（簡稱 "Gunicorn" 或 "Green Unicorn"）是一個用於運行Python Web應用程序的WSGI（Web Server Gateway Interface）HTTP伺服器。它的名字中的 "Green" 指的是它支持的協程模型，這使得它能夠有效地處理大量的並行連接和請求。

以下是有關Gunicorn的一些主要特點和資訊：

1. **WSGI伺服器：** Gunicorn是一個WSGI伺服器，它遵循WSGI規範，可以用於運行任何符合WSGI標準的Python Web應用程序，包括Django、Flask、Pyramid等。

2. **協程模型：** Gunicorn支持協程（或稱為綠色線程），這使得它能夠高效處理並行請求，而不會消耗過多的系統資源。這對於高流量的Web應用程序非常重要。

3. **簡單易用：** Gunicorn被設計成易於配置和使用。通常，您只需指定要運行的Python應用程序和伺服器端口，它將負責處理請求。

4. **多工作進程：** Gunicorn支持多工作進程模式，這意味著它可以在多個進程中運行您的應用程序，提供更好的性能和可用性。

5. **監視和管理：** Gunicorn提供了一些內置的工具，用於監視伺服器的運行狀態，並在需要時重新啟動或停止伺服器進程。

6. **擴展性：** 雖然Gunicorn本身是一個單一的伺服器，但它可以與反向代理（如Nginx或Apache）結合使用，以實現更高級的部署和負載均衡設置。

Gunicorn是Python Web應用程序部署的常見選擇之一，特別是當需要一個可靠且高效的WSGI伺服器時。它支持不同的配置和部署場景，使得它適用於各種規模和需求的項目。

### Gunicorn安裝布置

Gunicorn（Green Unicorn）是一個用於部署 Python Web 應用程序的 WSGI HTTP 伺服器。以下是安裝和部署 Gunicorn 的一般步驟：

1. 安裝 Gunicorn：
   您可以使用 pip（Python 包管理器）來安裝 Gunicorn。在終端中執行以下命令：

   ```bash
   pip install gunicorn
   ```

   這將下載並安裝 Gunicorn。

2. 準備您的應用程序：
   確保您的 Python Web 應用程序使用 WSGI（Web Server Gateway Interface）規範。通常，Python Web 框架（如 Flask、Django 等）都遵循 WSGI 規範，但您需要確保應用程序準備就緒，可以通過 WSGI 介面與 Gunicorn 進行通信。

3. 啟動 Gunicorn：
   在部署環境中，使用以下命令來啟動 Gunicorn，並將其連接到您的應用程序。替換 `<app_module>` 為您的應用程序模塊名稱，例如 `myapp:app`，其中 `myapp` 是模塊名稱(此處範例為`flask_up`，python程式名稱)，`app` 是 WSGI 應用程序實例。

   ```bash
   gunicorn <app_module>:app
   ```

   例如：

   ```bash
   gunicorn myapp:app
   ```

   Gunicorn 將在預設端口（8000）上啟動，您可以使用 `-b` 選項指定要綁定的 IP 和端口。例如，要綁定到所有 IP 地址的 8080 端口，可以使用：

   ```bash
   gunicorn -b 0.0.0.0:8080 myapp:app
   ```

4. 部署到生產環境：
   在生產環境中，通常會使用反向代理伺服器（例如 Nginx 或 Apache）來處理外部請求，然後將請求**轉發**給 Gunicorn。這有助於提高安全性和性能。請設置反向代理伺服器以將請求**轉發**到 Gunicorn 運行的 IP 和端口。

5. 監控和管理：
   您可以使用 Gunicorn 的管理界面來監控和管理 Gunicorn 進程。啟用管理界面的方法因版本而異，請查閱相關文檔以了解詳細信息。

6. 設定文件：
   您可以通過 Gunicorn 的配置文件來設置 Gunicorn 的行為。創建一個 Gunicorn 配置文件，然後使用 `-c` 選項指定它。例如：

   ```bash
   gunicorn -c gunicorn_config.py myapp:app
   ```

以上是使用 Gunicorn 部署 Python Web 應用程序的基本步驟。請根據您的特定應用程序需求和部署環境進行調整和配置。詳細的 Gunicorn 文檔可供參考，以瞭解更多選項和配置。