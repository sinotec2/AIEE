---
layout: default
title: 在https靜態網頁中嵌入AI聊天
parent: Anything LLM
grand_parent: 自然語言處理
nav_order: 99
date: 2024-04-23
last_modified_date: 2024-04-23 13:33:53
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
- 與既有的GPT套件整合，不另外撰寫程式。

### 整合時面臨的限制

- https靜態網頁中，不允許鑲嵌http網頁或服務。
- http靜態網頁，沒有辦法連接IPA服務，僅能是公開網頁，不能限定讀者。
- docker啟動的anythingLLM服務，必須接到一個本地http端口，不能接到https端口。
- 生產階段node會啟動其內定的HTTPS服務，不能與工作站apache2 https有相同的key.pem、cert.pem。
- anythingLLM的公開網頁(server/public)內容，其根目錄必須是`http://host.domain_name:port`，不能是某個https的目錄。用apache 目錄設定、alias、反向代理等方式，也都不能作用。
- Embedded Chat所用的LLM，必須是anythingLLM的preferencd LLM(eg. `LLM_PROVIDER='openai'`)，不能是工作區專用LLM。
- 使用者本地瀏覽器對SSL CERT許可的設定方式，也會影響鑲嵌的效果，因為會同時使用2組CERT。
  - 可行的隱私權設定：Chrome的標準
  - Edge可以分別登入vuepress及anythingLLM的https網頁，無法接受鑲嵌整合。但`http://devp.sinotech-eng.com/emb.html`中可以接受鑲嵌`https`的服務。


![](emb_pngs/2024-05-15-17-37-52.png)

![](emb_pngs/2024-05-15-17-07-18.png)