---
layout: default
title: Heroku 
parent:  Platform As A Service
grand_parent: 自然語言處理
nav_order: 99
date: 2023-09-06
last_modified_date: 2023-09-06 16:02:26
tags: AI chat report
---

# Heroku 
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

- 這類的實作看似很多範例可以參考，但第一個就踩雷。伺服器不提供免費方案了。

## database and chatbot

### Heroku 簡介與趨勢

- introduction of [Heroku][wiki]

平臺即服務Heroku將在今年終止免費服務 by [陳曉莉(2022-08-26)@IThome](https://www.ithome.com.tw/news/152729)

from searchGTP
- Heroku 提供免費的服務計劃，稱為 "Heroku Free" 或 "Heroku Hobby"，讓開發者可以部署和運行應用程序，而無需支付費用。然而，這些免費計劃具有一些限制和限制，包括：
  - 睡眠應用程序：免費的 Heroku 應用程序會在一段時間沒有活動後進入休眠模式，這導致應用程序在首次訪問時可能會出現延遲。每當有人訪問應用程序時，它會重新啟動，但這可能需要一些時間。
  - 資源限制：免費的 Heroku 應用程序有限的計算和記憶體資源。如果您的應用程序需要更多資源以支援大量流量或複雜的操作，您可能需要升級到付費計劃。
  - 月使用限制：免費 Heroku 應用程序有每月使用的限制。如果您的應用程序在某個月內超出了這些限制，您可能需要支付額外費用或升級到付費計劃。
  - 資料庫限制：免費 Heroku 資料庫有限制，包括連接數和存儲容量。如果您的應用程序需要更多的資料庫資源，您可能需要考慮升級到付費資料庫計劃。
- 總之，Heroku 提供了免費的應用程序部署和運行選項，這對於簡單的項目或開發人員來說可能是一個不錯的選擇。但是，如果您的應用程序需要更多資源或更高的可用性，您可能需要考慮升級到付費計劃以滿足您的需求。請參閱 Heroku 的官方網站以獲取有關不同計劃和定價的詳細信息。

Heroku 終止免費！分享４個替代的雲端平台 by [jarvus(Aug, 2022)](https://jarvus.dragonbeef.net/note/noteServerless.php)
- render.com
- Fly.io
- Deta.sh
- Google Cloud Run

list of chatbot on line, see [tsai(2021)](https://github.com/bingyan-tsai?tab=repositories)
為聊天機器人連結資料庫！Chatbot學習筆記-Day3 by [Jason Tsai(AAug 26, 2021)@medium.com](https://medium.com/@jasonb0604/學習筆記-day3-5ef7b65797f3)
- 利用聊天機器人對資料庫下指令吧！Chatbot學習筆記-Day4 by [Jason Tsai(Aug 27, 2021)@medium.com](https://medium.com/@jasonb0604/chatbot學習筆記-day4-d7776289bc74)
  - [github](https://github.com/bingyan-tsai/Chatbot-Day4)

[wiki]: https://zh.wikipedia.org/zh-tw/Heroku "Heroku是一個支援多種程式語言的雲平台即服務。在2010年被Salesforce.com收購。Heroku作為最元祖的雲平台之一，從2007年6月起開發，當時它僅支援Ruby，但後來增加了對Java、Node.js、Scala、Clojure、Python以及PHP和Perl的支援。 維基百科"