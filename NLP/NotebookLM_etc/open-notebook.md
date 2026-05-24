---
layout: default
title: open-notebook
grand_parent: 自然語言處理
nav_order: 1
date: 2026-05-24
last_modified_date: 2026-05-24T13:11:00
tags:
  - AI
  - notebookLM
parent: notebookLM與類似開源系統
---

# open-notebook
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

根據您目前瀏覽的 **Open Notebook** 介面以及其核心設計，這是一款**以 AI 為核心驅動 heavy-duty 知識管理與創作的工作坊**。

它的核心構想是：**「讓使用者能自由組合各式 AI 模型，將碎片化的資訊從『採集』、『處理』一路推進到『自動化創作』與『深度管理』。」**

以下為您詳細拆解 Open Notebook 的四大核心功能區塊與設計構想：

---

## 一、 四大核心功能架構

從系統的側邊欄導覽，可以看到 Open Notebook 完整的知識處理工作流：

### 1. 採集 (Capture)

- **來源：** 這是知識輸入的起點。支援將各種外部資訊（如網頁、文件、筆記等）匯入系統中，作為後續 AI 處理的「原始燃料」。
    

### 2. 處理 (Process)

- **筆記本：** 核心的知識沉澱空間。使用者可以在這裡結構化地整理採集到的資料。
    
- **詢問與搜尋：** 整合了 RAG（檢索增強生成）技術。使用者不僅僅是「搜尋」關鍵字，而是可以直接對著自己的筆記庫、知識庫進行深度提問，讓 AI 根據使用者的專屬資料給出精準解答。
    

### 3. 創作 (Create)

- **播客 (Podcast)：** 這是 Open Notebook 的一大亮點功能（類似 Google NotebookLM 的 Audio Overview）。它能將密密麻麻的文字筆記或報告，自動轉換為雙人對談或單人演講的**語音播客**，讓知識能用「聽」的方式被快速吸收。
    

### 4. 管理 (Manage)與進階

- **模型與設定：** 開放高度自主權，讓使用者自由管理與配置不同的 AI 供應商。
    
- **轉換：** 專門處理自動化摘要、見解提取、內容格式轉換等批量工作。
    

---

## 二、 獨特的設計構想：大腦模型分工（Model Routing）

Open Notebook 的核心構想與一般單一聊天軟體（如 ChatGPT 網頁版）最大的不同在於：**「因才適用、多模型協同」**。

在設定中，它將 AI 任務細分，允許使用者為不同的場景配置最適合的模型：

|**任務用途**|**系統推薦與設定邏輯**|**畫面中的實際配置範例**|
|---|---|---|
|**聊天模型 (Chat)**|用於日常對話、快速問答，需要速度快且成本低。|`gpt-5-mini`|
|**工具模型 (Tools)**|用於函數調用 (Function Calling)、執行複雜指令或調用外部工具。|推薦使用 OpenAI 或 Anthropic|
|**大上下文模型 (Large Ctx)**|用於閱讀整本書、超長報告或數百頁的論文。|`gpt-5-mini` (推薦 Gemini 的百萬代幣大窗口)|
|**嵌入模型 (Embedding)**|將文字轉換為向量，負責專屬知識庫的「精準搜尋與比對」。|`text-embedding-3-small` / `bge-large-zh`|
|**語音轉換 (TTS / STT)**|負責將筆記轉為播客（文字轉語音）或將錄音轉為文字。|`whisper-1` / `gpt-4o-mini-tts`|

---

## 三、 高度的生態開放性（自由相容）

從您目前的畫面中可以看到，Open Notebook 的構想是**不綁定任何單一廠商**。不論是雲端頂級商業模型，還是本機隱私模型，它都能完美相容：

- **頂級雲端 AI：** 支援 OpenAI、Anthropic、Google AI、DeepSeek、Mistral、XAI (Grok) 等。
    
- **在地開源與隱私：** 支援透過 **Ollama** 或 **vLLM** 接入本地運行的開源模型（例如畫面上已設定的 `gemma4:31b` 或 `gpt-oss-20b`）。這意味著企業或個人可以將敏感資料完全留存在本地，確保隱私安全。
    
- **中繼整合商：** 支援 OpenRouter 等聚合平台，方便切換各種小眾或最新模型。
    

---

## 總結

**Open Notebook** 不只是一個筆記軟體，而是一個「可私人訂製的 AI 知識加工廠」。它的構想是打破傳統筆記「只藏不用」的僵局，透過後台多模型的彈性協同（文字、向量、語音），幫使用者把海量資料真正轉化為可以隨時檢索、甚至能自動產出播客音訊的「活知識」。
### 官網

[github](https://github.com/lfnovo/open-notebook)

## 實作

[內部伺服器位置](http://node01.sinotech-eng.com:8505/notebooks)

![](pngs/Pasted%20image%2020260524172659.png)

## 供應商與模型

- 從左側管理→模型進入
- 必須嚴格按照各種類別，選擇適用的語言模型，(類似範例所示)

![](pngs/Pasted%20image%2020260524173710.png)

- 只有API_KEY連線型態，devices、會員型態還沒有建立。


![](pngs/Pasted%20image%2020260524172908.png)

### 地端模型

- 可接受ollama跟openAI Compatible

![](pngs/Pasted%20image%2020260524173416.png)

## TODO's

[] devices連線，用API_KEY並不合理
[] text to image/image to text功能尚待開發
[] 個人desktop執行APP的編譯尚未完成(自動掃描並把 `.venv\Lib\site-packages` 中的 `*__mypyc*.pyd` 加入 `open_notebook_api.spec`，然後重新執行一次完整的 PyInstaller build)。
[] 播客功能尚未測試成功(tts模型未勾選在API功能項目中)