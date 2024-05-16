---
layout: default
title: 在https靜態網頁中嵌入AI聊天
parent: Anything LLM
grand_parent: 自然語言處理
nav_order: 99
date: 2024-05-16
last_modified_date: 2024-05-16 20:45:29
tags: AI chat
---


# 在https靜態網頁中嵌入AI聊天
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

### 目標

- 在https靜態網頁(如vuepress)中，鑲嵌AI小幫手。
- 與既有的GPT套件整合，不另外撰寫系統程式。

### 工作流程

- 啟動anythingLLM生產服務
- AnythingLLM[新增工作區](./AnyChat_mng.md#新增工作區)、[載入網頁內容文字檔](./AnyChat.md#檔案網頁與資料的連結)、[設定語言模型](./AnyChat_mng.md#設定工作區)、新增[Embedded Chat](./AnyChat_adm.md#嵌入對話)
- [複製程式碼](./EmbChat.md#程式碼)到靜態網頁的frontmatter。
- 重新編譯靜態網頁、發表網頁、測試效果
- 調整anythingLLM的設定，只要不更改工作區名稱、程式碼不會更動、就不需要重新編譯。

### 整合時面臨的限制

- 靜態網頁的要求（需求）
  - https靜態網頁中，不允許鑲嵌http網頁或服務。
  - http靜態網頁，沒有辦法連接IPA服務，僅能是公開網頁，不能限定讀者。
- 生產階段anythingLLM的作法
  - 官網建議以docker方式營運、開關較為單純、避免直接使用node、會更改使用者的環境(`nvm`與其他環境變數)。
  - docker啟動的anythingLLM服務，必須接到一個本地http端口，不能接到https端口。主機上端口如果設定被apache https監聽，就不能作為docker的出口，反之亦然。
  - 官網沒有[啟動node服務](./product_yml.md#node生產方案)的相關說明
- apache2網頁伺服器的限制
  - http和https對端口的綁定有很大的出入，後者必須有`Listen {port} https`指令，否則即時使用`<VirtualHost *：{port}>`指令，也不能開啟https://端口。
  - anythingLLM的公開網頁(server/public)內容，其根目錄必須是`http(s)://host.domain_name:port`，不能是某個https的目錄。用apache 目錄設定、alias、反向代理等方式，也都不能作用。
- node.js/apache2 HTTPS服務的衝突
  - 生產階段node會啟動其內定的HTTPS服務，不能與工作站apache2 https有相同的key.pem、cert.pem。
  - 使用者本地瀏覽器對SSL CERT許可的設定方式，也會影響鑲嵌的效果，因為會同時使用2組CERT。
    - 可行的隱私權設定：Chrome的標準
    - Edge可以分別登入vuepress及anythingLLM的https網頁，無法接受鑲嵌整合。但`http://devp.sinotech-eng.com/emb.html`中可以接受鑲嵌`https`的服務。
- Embedded Chat所用的LLM，必須是anythingLLM的preferencd LLM(eg. `LLM_PROVIDER='openai'`)，不能是工作區專用LLM。

## 靜態網頁的要求（需求）

http方案雖然直接、有效整合，但問題缺點還不少

1. 既有的網頁系統，如vuepress網誌、iis內部官網首頁、工程服務網頁等等，絕大多數都是https。
2. 新的系統也許可以同時維持http/https平行運作，但舊系統要複製並且獨立運作，就不容易了。
3. 很多系統是dotnet專案，還需要編譯才能發布，http的鑲嵌內容確實會造成相容性的錯誤。
4. 如果獨立服務的系統，還可以維持http方案，但面臨整合、分眾、帳密管控等等，似乎就再也沒有這個選項了。

## 生產階段anythingLLM的作法

- docker最大的困難在於必須使用主機的網路伺服器來管理端口。docker映像內部一個端口、外部主機搭配一個端口，不單是重複設定，而且docker與apache2的https還不相容，二者對端口都有強烈的佔有權，這使得docker方案變得不可行。
- 絕大多數的服務可以維持使用官網建議的docker方案，不需要整合、也不需要https。只需要留一個端口，專門服務網頁小幫手即可。
- 官網雖然沒有[啟動node服務](./product_yml.md#node生產方案)的相關說明，但提供了`Dockerfile`、`docker-compose.yml`，以及`docker-entrypoint.sh`等腳本，可以從其中找到啟動的方式。
- [執行批次腳本](./product_yml.md#執行批次腳本)
  - 安裝、編譯、產生schema（只需執行一次）、
  - 啟動服務要注意
    - 環境變數`NODE_ENV=production`
    - 從備份檔案複製`.env`檔案
    - 記得部署schema
    - 依序啟動`server/index.js`與`collector/index.js`等2個伺服器。
- 啟用node.js的HTTPS相關程式，需設定`server/.env`檔案，如[.env檔案設定](./product_yml.md#env檔案設定)
  - `SERVER_PORT='https://eng06.sinotech-eng.com:3014'` ，這個設定似乎不太經典，但系統沒有報錯，如果不設https前綴，仍然會回到http前綴、或`localhost`，有其必要性。然此設定會被系統覆蓋，記得每次從備份檔再複製一份。
  - `ENABLE_HTTPS='true'`:這個設定會讓`index.js`啟動相應的HTTPS服務，dockerfile內也沒有下載啟用apache2的痕跡，足見其HTTPS服務是有別於apache2的。
  - `HTTPS_CERT_PATH`、`HTTPS_KEY_PATH`:SSL的認證檔，必須**不同**於apache2的證書與金鑰。
- 排程設定
  - 啟動比較沒有問題，按照程序循序執行即可(不必每次安裝編譯)。
  - 關閉則要小心執行。因為`index.js`使用了絕對路徑，可以此為特徵進行篩選，將其pid予以刪除。

    ```bash
    #!/bin/bash
    for $i in $(ps -ef|grep node|grep '/nas2/kuang/MyPrograms/anythingLLM'|grep index.js|awk '{print $2}');do
      kill -9 $i
    done
    ```

## apache2與node.js https相容性問題

- apache2是靜態網頁平台依賴的伺服器，node.js是語言模型的伺服器，二者都是https，有自己的SSL金鑰與憑證、啟動的設定詳[前](#生產階段anythingllm的作法)。

### 金鑰與憑證的檔案可讀性

- apache2的執行者是`root`，金鑰與憑證可以設成`og-rwx`。
- node.js的執行者是一般人，金鑰與憑證產生後必須讓`og+r`。

### 瀏覽器的差異表現

使用者瀏覽器的選擇與SSL設定方式，將會影響是否出現小幫手。

- Chrome
  - 經多次重新整理會可以出現
- Edge
  - 似乎不接受node.js的金鑰與憑證。

## CORS跨域服務

CORS 是 "Cross-Origin Resource Sharing" 的縮寫,即跨源資源共享。

跨源資源共享是一個 Web 標準,它定義了瀏覽器和服務器如何以安全的方式處理跨源 HTTP 請求。這是為了解決瀏覽器的同源政策限制,該政策禁止一個源(origin)的網頁訪問另一個源的資源。

CORS 透過在 HTTP 響應頭中加入特定的標頭,允許瀏覽器和服務器進行安全的跨源交互。這些標頭包括:

- `Access-Control-Allow-Origin`: 指定允許訪問該資源的**來源**域。
- `Access-Control-Allow-Methods`: 指定允許的 HTTP 請求方法。
- `Access-Control-Allow-Headers`: 指定允許的自定義請求頭。
- `Access-Control-Expose-Headers`: 指定允許瀏覽器訪問的響應頭。

通過設置這些 CORS 標頭,服務器可以控制哪些來源、哪些方法和哪些請求頭可以安全地訪問該資源。這是一種跨源訪問的機制,可以增強 Web 應用程式的安全性。

###  Apache2 設定

在 Apache2 中啟用 CORS 跨域訪問,可以在conf檔案中使用 `mod_headers` 模組來配置。以下是一個示例配置:

1. 首先確保 `mod_headers` 模組已經啟用。在 Ubuntu/Debian 系統上,可以使用以下命令啟用:

   ```
   sudo a2enmod headers
   ```

2. 在 Apache 的配置文件中(通常位於 `/etc/apache2/apache2.conf` 或 `/etc/apache2/sites-available/default.conf`)添加以下 CORS 配置:

   ```apache
   
       Header set Access-Control-Allow-Origin "*"
       Header set Access-Control-Allow-Methods "GET,POST,OPTIONS,DELETE,PUT"
       Header set Access-Control-Allow-Headers "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range"
       Header set Access-Control-Expose-Headers "Content-Length,Content-Range"
   
   ```

   這個配置允許所有來源(`"*"`)訪問您的 Apache 服務,並允許 GET、POST、OPTIONS、DELETE 和 PUT 等 HTTP 方法。您也可以根據需要調整 `Access-Control-Allow-Methods` 和 `Access-Control-Allow-Headers` 的值。

3. 保存配置文件並重啟 Apache 服務:

   ```
   sudo systemctl restart apache2
   ```

這樣就完成了 Apache2 的 CORS 跨域訪問配置。您可以使用瀏覽器開發者工具或其他測試工具來驗證跨域請求是否成功。

需要注意的是,在生產環境中,您可能需要根據具體的安全需求來調整 CORS 策略,例如限制允許的來源域名,而不是使用通配符`"*"`。

### 發展階段的作法

- embed chat採用`http://localhost:3014`的方式來服務，即使是`https`的靜態網頁，也不會發生跨域限制的問題。

```bash
這是因為當你在本地環境(http://localhost)上運行服務時,瀏覽器會自動放寬跨域限制,允許同源的HTTPS網頁(https://...)訪問http://localhost上的服務。這是為了方便開發者在本地調試和測試時使用。

但是,一旦你將應用部署到正式環境(非localhost),就必須嚴格遵守CORS規則,因為瀏覽器會阻止跨域訪問,除非服務器端配置了正確的CORS策略。所以在正式環境中,你需要確保服務器端開啟了適當的CORS設置,以允許跨域訪問。
```

### node.js修改

如果你的服務是透過Docker 容器部署的，並且你需要在Docker 容器內設定CORS 規則以允許跨域請求，你可以在你的Node.js 服務中設定CORS 規則，然後在Dockerfile 中將該服務打包到 Docker 映像中。

以下是在 Node.js 中設定 CORS 規則的簡單方法：

```javascript
const express = require('express');
const cors = require('cors');
const app = express();

// 允許所有網域的跨域請求訪問
app.use(cors());

// 其他路由或中介軟體設定
app.get('/', (req, res) => {
   res.send('Hello World!');
});

app.listen(3000, () => {
   console.log('Server is running on port 3000');
});
```

確保在你的 Node.js 服務中正確設定了 CORS 規則。 然後，在你的 Dockerfile 中，建置映像時將這個服務打包進去。

以下是一個簡單的 Dockerfile 範例：

```Dockerfile
# 使用官方 Node.js 14 鏡像作為基礎鏡像
FROM node:14

# 建立工作目錄並將應用程式程式碼複製到工作目錄
WORKDIR /app
COPY . .

# 安裝依賴
RUN npm install

# 暴露端口
EXPOSE 3000

# 啟動服務
CMD ["node", "app.js"]
```

## 成果畫面

### 小幫手icon + 

![](emb_pngs/2024-05-15-17-37-52.png)

### 打開、對話成果

![](emb_pngs/2024-05-15-17-07-18.png)

## ToDo‘s

- 版面衝突
  - 小幫手的+與vuepress的回到頁首（火箭），太靠近、大小差不多會彼此干擾。
  - `anythingllm-chat-widget.min.js`是放在vuepress的頁尾，所產生的物件無法遮蔽vuepress的`此頁內容`
  - 小幫手不受縮放影響。
- 瀏覽器選擇性SSL的問題



