---
layout: default
title: KnowNote
grand_parent: 自然語言處理
nav_order: 1
date: 2026-05-24
last_modified_date: 2026-05-24T13:11:00
tags:
  - AI
  - notebookLM
parent: notebookLM與類似開源系統
---

# KnowNote
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

[KnowNote](https://github.com/MrSibe/KnowNote) 是一款專為學習者和開發者設計的**在地優先（Local-first）、開源、免 Docker** 的 AI 知識庫與筆記工具（被視為 Google NotebookLM 的優質開源替代方案）。

以下為您整理其核心功能：

### 📚 知識庫與文件管理

- **多格式匯入：** 支援 PDF、Word (`.docx`)、PowerPoint (`.pptx`)、Markdown、TXT 以及網頁內容的匯入。
    
- **自動解析：** 系統會自動對文件進行結構化解析與內容提取。
    
- **在地快速儲存：** 使用 SQLite 作為底層資料庫，確保資料在本地端的高效儲存與讀取。
    

### 🤖 AI 智慧問答與推理

- **RAG 檢索增強生成：** 結合文件上下文進行 AI 對話，大幅降低大模型瞎編的機率。
    
- **精準溯源：** AI 給出解答的同時，會附帶精確的**來源內容引用標記**，點擊即可查看原文出處。
    
- **多模型對接：** 採用 Provider 架構設計，支援自主接入 OpenAI、DeepSeek、Ollama（本地執行模型）等多種 LLM API。
    

### 🧠 筆記與視覺化知識輸出

- **三欄式版面：** 介面採用「知識庫 · AI 問答 · 筆記輸出」的高效設計，方便邊查邊寫。
    
- **結構化筆記生成：** 可以直接將對話內容或提取的核心重點，轉化為系統化的結構筆記。
    
- **一鍵生成心智圖：** 支援根據文件或對話內容，在獨立視窗中一鍵渲染出心智圖（Mind Map），幫你理清知識脈絡。
    

### 🔒 在地優先與輕量化設計

- **免 Docker / 免伺服器設定：** 基於 Electron + React + TypeScript 打造的桌面客戶端（支援 Windows 和 macOS），下載後雙擊即可使用，對非後端開發者非常友善。
    
- **資料完全掌控：** 所有文件、向量資料均保存在本地端，支援離線使用（若搭配本地 Ollama 模型，可實現完全單機的隱私保護）。
    
- **高效向量檢索：** 內建 `sqlite-vec` 擴充功能，無需部署龐大的向量資料庫，即可在本地實現快速、準確的語義搜尋。
    

---

###  💡 **項目開發藍圖（Roadmap）：**

> 
> 目前作者仍在持續推進以下功能的開發，未來將會陸續上線：
> 
> - 🚧 **音訊上傳與語音轉文字（Transcription）**>     
> - 🚧 **根據文件自動生成測驗題目（Quiz）**
> - 🚧 **根據筆記一鍵生成 PPT 簡報**
>
## 實例


![](pngs/Pasted%20image%2020260524180825.png)

模式設定

![](pngs/Pasted%20image%2020260524181855.png)