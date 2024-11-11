---
layout: default
title: 註冊與登入
parent: RAGflow
grand_parent: SearchingEngine
nav_order: 1
date: 2024-10-12 
last_modified_date: 2024-10-12 20:32:31
tags: AI chat report
---

# 註冊與登入  
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

![](./pngs/2024-10-12-20-30-42.png)

1. 測試階段沒有收費、免費使用API解讀、聊天，但長度有限。
2. 帳密
   1. 帳號：郵箱、一旦設定將無法更改。不會寄信到郵箱確認。（`sinotec2@gmail.com`）
   2. 姓名：會出現在團隊協作相關畫面，請用中文全名以方便識別。
   3. 至少8碼、密碼可改，但無忘記密碼功能。(`sinotech-eng`)
   4. 也可使用github帳密登入，安全性較高。
   5. 沒有admin權限身分。
3. 有dev與正式版本可選。
   1. 開發版本(:dev)是為開發者和貢獻者準備的。這些版本會以每日構建的方式發布，可能會因為尚未完全測試而崩潰。；貢獻者無法保證其穩定性，嘗試最新、未經測試的功能需自行承擔風險。
   2. 最新版本(:last)指的是最近一次正式發布的版本。這是穩定版本，對於一般使用者來說，效果最佳。
4. 網址:[https://demo.ragflow.io/login](https://demo.ragflow.io/login)

## 團隊主從關係

- 團的主權責
  - 負責上載檔案、製作知識庫
  - 勾選知識庫的權限：開放給「團隊」
  - 寄發加入團隊的「邀請」給特定對象
  - 管理（刪除）團隊特定成員。
- 團員的權責
  - 接受團主的邀請
  - 檢視、詢問(似乎還不能搜尋）團主製作的知識庫。
  - 修改知識庫

## TODO's

- 目前帳密還需更改程式碼方能接受其他方式登入
- 似乎API還未開放批次建立帳密