---
layout: default
title: 對話機器人API
parent: RAGflow
grand_parent: SearchingEngine
nav_order: 99
date: 2024-10-30 
last_modified_date: 2024-10-30 20:32:31
tags: AI chat report
---

# 對話機器人API  
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

- RAG與一般的聊天機器人差異在於會顯示其生成的依據，可以進行追蹤及驗證。
- RAGFlow提供了聊天機器人的API伺服器，經由token給定可以取用上線的知識庫。

## API之啟用

- API token的產生
- RESTful 網址

## RESTFul網址之應用 

- iframe
- proxy

## 聊天機器人的差異

項目|RAGFlow|API連線
-|-|-
登入帳密|是|否
顯示依據檔案|是|否
對話記憶|是|否
附加檔案|否|是
使用統計|否|是
調整對話溫度等條件|是|否

- API對話機器人雖無詳細的對話紀錄，但仍然有用量的總量統計，可供成效檢討。

## TODO's

- 因無紀錄，如果約定好簡稱，系統將不會有記憶，需每次提醒。
  - 是否可以用檔案紀錄，每次填入作為前提。
- 對話溫度臨時調整(調增)、以因應整合性的法律諮詢
  - 另以綜合性對話API以為因應
