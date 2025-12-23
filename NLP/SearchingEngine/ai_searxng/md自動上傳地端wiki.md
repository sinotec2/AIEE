---
layout: default
title: md2wili自動上傳
parent: 地端智慧搜尋引擎
grand_parent: SearchingEngine
nav_order: 1
date: 2025-11-11
last_modified_date: 2025-11-11T13:08:00
tags:
  - AI
  - wiki
---

# md2wili自動上傳

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

## 背景說明

### 由來

- wiki文章的格式(==MediaWiki== mw為例)，與一般常用的markdown(md)標記語言不同，需要轉檔、整理、還頗為麻煩。(解決方案為`pandoc`程式)
- 文章改好、上傳、也需特別登入、轉貼、寫標題、摘要、分類等等標籤。(解決方案為api指令操作)
- 整合前2項功能，特別引入AI按照文章內容整理標題、摘要、分類，方便使用者一鍵生成。
- ==MediaWiki==實例的[位址](https://eng06.sinotech-eng.com/wiki/index.php)

### 用途

- 將筆記內容納入地端[searXNG](https://eng06.sinotech-eng.com/wiki/index.php/分類:SearXNG)搜尋
- AI徵詢結果、程式使用手冊、公開筆記之地端發布平台(share-link on premise)
- 穩定、經審查之結果將會出現在[searXNG](https://eng06.sinotech-eng.com/wiki/index.php/分類:SearXNG)之資訊欄(infobox)，如下圖：

![](pngs/Pasted%20image%2020251111201717.png)

## 實例

- 網址：[eng06.sinotech-eng.com/md2mw/](https://eng06.sinotech-eng.com/md2mw/)
- ==不需==帳密
### 畫面

![](pngs/Pasted%20image%2020251111200553.png)

### 檔案輸入

- 由右上方`選擇檔案`開啟`md`檔案
- 檔案名稱不限字尾一定要是`.md`，任何文字檔案都可以。程式將會以markdown進行解析辨識

### 剪貼簿內容

- 直接在左側欄空白處貼上
- 可自行在此編輯

### 預覽

- 在右側欄內顯示

## 標籤之輸入、產出

- 標題：將會作為mediawiki的連結標籤
- 摘要：編輯說明
- 分類：各分頁匯集之類別頁，可以是複數個類別。
使用者可以自行鍵入、或者按下`產生建議`，呼叫地端AI(openai/gpt-oss)來自動產生，再在做必要的修改。


![](pngs/Pasted%20image%2020251111201912.png)

::: note

- 如果連不上地端AI，可以另外開啟一個新的分頁，直接貼上這個網址([https://l40.sinotech-eng.com/v1/models](https://l40.sinotech-eng.com/v1/models))並且接受連線風險就可以順利連線。這是因為公司網路定期會更新連線的cookie。
- 如果還是連不上、或AI反應緩慢(先到[這裡]()檢查GPU負載)，請洽分機08503謝天霖、 09025王子齊。

:::
## 上傳

- 如果預覽沒有太大問題、標籤也都已經產生，便可以進行上傳動作。
- 最後上傳成功，還必須按下`確定`來結束作業。

![](pngs/Pasted%20image%2020251111202417.png)


## 檢核

- 登入[==MediaWiki==](https://eng06.sinotech-eng.com/wiki/index.php)
- 由左側[近期變更](https://eng06.sinotech-eng.com/wiki/index.php/%E7%89%B9%E6%AE%8A:%E8%BF%91%E6%9C%9F%E8%AE%8A%E5%8B%95?hidebots=1&limit=50&days=7&enhanced=1&urlversion=2)


![](pngs/Pasted%20image%2020251111202818.png)

- 可以看到機器人(Kuang@Bot)生成的文章，點入後，直接編輯即可，系統會記錄每一個編輯人員及內容。

![](pngs/Pasted%20image%2020251111203533.png)