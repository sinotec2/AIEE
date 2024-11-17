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

## Streamlit

### 中文介紹與官網

- [owo](https://blog.o-w-o.cc/archives/streamlit-chatelements)
  - 這篇文章探討如何使用 Streamlit 的 st.chat_message 和 st.chat_input 來建立簡單的聊天機器人介面。
  - 作者詳細說明了基本的輸入輸出框架設置，並介紹了透過 st.session_state 來保留對話歷史的方法。
  - 文章以實際程式碼範例展示，對於希望透過 Streamlit 開發互動性聊天機器人的開發者來說很實用。
  - 完整內容可參閱原文。
- StreamLit官網
  - Streamlit 文件提到的 GPT-like 介面構建過程包含了對話框的佈局設置與用戶互動。
  - 核心步驟是使用 st.chat_message 模擬對話氣泡，並將 st.session_state 應用於存儲與管理對話歷史，以維持連貫的對話體驗。
  - 這使得應用能模仿 GPT 的聊天界面，實現用戶請求和模型回應的交換，並提升應用的交互性。
  - 文章確實討論了 API 伺服器連結的相關問題，特別是如何通過 API 進行 LLM（大型語言模型）的請求處理，以使應用能夠回應 GPT-like 對話框中的輸入。
  - Streamlit 示範了如何通過設置 API 請求來獲取生成的回應，並解釋了串接 API 的基礎方法，以保持對話的一致性與流暢性。
  - 詳情可參考Streamlit 官方文件。

### 範例程式

- [GitHub](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)
- Chatbot.py 是一個使用 Streamlit 架設的聊天機器人應用程式，
  - 利用 OpenAI API 生成對話回應。
  - 以下是此程式的詳細說明：

- 輸入：

	•	OpenAI API 金鑰：需要在側邊欄輸入以進行身份驗證。
	•	使用者輸入：使用者在聊天欄位中輸入的問題或對話內容。

- 輸出：

	•	顯示使用者訊息與機器人回應，形成對話記錄。

- 主要邏輯：

	1.	會話管理：利用 st.session_state 追蹤對話歷史，維持上下文。
	2.	訊息處理：對每次輸入呼叫 OpenAI 的 gpt-3.5-turbo 產生回應。

- 注意事項：

	•	OpenAI API 金鑰為必填。
	•	須在環境中安裝 openai 和 streamlit。

## TODO's

- 因無紀錄，如果約定好簡稱，系統將不會有記憶，需每次提醒。
  - 是否可以用檔案紀錄，每次填入作為前提。
- 對話溫度臨時調整(調增)、以因應整合性的法律諮詢
  - 另以綜合性對話API以為因應
