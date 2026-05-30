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

### 執行
- run@eng07：` C:\Users\kuang\MyPrograms\KnowNote> pnpm dev -- -- --host 172.20.31.19`

### 增加繁體中文


- 新增繁體語系支援：新增 `src/renderer/src/locales/zh-TW` 並複製現有 `zh-CN` 的翻譯檔。
- 自動轉換：新增腳本 `scripts/convert-to-zh-TW.js` 並以 `opencc` 將簡體翻譯自動轉為繁體，已執行轉換。
- 註冊與載入：在 `i18n` 設定中註冊 `zh-TW` 資源（更新 `src/renderer/src/i18n.ts` 與 `src/renderer/src/i18n/index.ts`）。
- 型別與工具支援：擴充相關型別與工具以支援 `zh-TW`（例如 `src/renderer/src/lib/i18n.ts`、`src/renderer/src/store/i18nStore.ts`、`src/shared/types/index.ts`）。
- 設定預設提示詞：將 `zh-CN` 的 prompts 複製到 `zh-TW`，已更新 `src/main/config/defaults.ts`。
- 合併邏輯修正：修正 `src/main/config/settingsManager.ts` 的合併邏輯，動態合併 `defaultSettings.prompts`，確保 `zh-TW` 預設提示詞能被正確讀取。
- Embedding 維度錯誤修正：修正 `src/main/services/KnowledgeService.ts` 的檢索流程，使用查詢向量回傳的維度來取得/建立向量庫，降低 1024 vs 1536 維度不一致錯誤的發生。
- 其他輔助修改：新增 `zh-TW` 在 onboarding 與設定選單中的顯示選項，並更新相容的 UI 檔案。

這些更動已在程式碼庫中實作，並留下可供驗證的檔案與腳本。

### 驗證與建議步驟  

建議的快速驗證項目：  
1. 重新啟動應用並前往「設定 → 提示詞」，切換語言至「繁體中文」，應能看到預設的繁體提示詞（或按「恢復預設」）。
2. 若遇到向量維度不一致（SQLite 報錯），請針對該 notebook 清除向量並重新索引文件，或在 UI 中重新加入文件以觸發重建索引。
3. 若需批次轉換或調整翻譯文字，可編輯 `src/renderer/src/locales/zh-TW` 下的 JSON 檔後重啟應用生效。

### 畫面

![](pngs/Pasted%20image%2020260524180825.png)

模式設定

![](pngs/Pasted%20image%2020260524181855.png)

## 評論

2025年底~2026年2月期間，KnowNote確實引起不少注意，後續沒有繼續發展的理由，猜測可能是：

1. openclaw興起，大眾目光集中在agentic AI，這類以學習為主要服務功能的專案，很快失去舞台。
2. 功能也只限於文件-指令-文件，而不是圖片- 指令-圖片