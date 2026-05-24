---
layout: default
title: InsightsLM
grand_parent: 自然語言處理
nav_order: 1
date: 2026-05-24
last_modified_date: 2026-05-24T13:11:00
tags:
  - AI
  - notebookLM
parent: notebookLM與類似開源系統
---

# InsightsLM
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

### 摘要

InsightsLM 是一個開源且可自託管的 NotebookLM 替代方案，允許用戶與自有文件進行對話並生成語音摘要。該專案前端採用 React、Vite 與 Tailwind CSS 等現代化工具構建，後端則高度依賴 Supabase 處理資料庫與身份驗證，並使用 N8N 進行工作流自動化。它主打資料隱私控制與高度可自訂性，非常適合需要利用檢索增強生成（RAG）技術來打造專屬且可靠的企業知識庫的開發者與企業。

### 關鍵要點

- InsightsLM 是一款開源的 AI 研究工具，能讓使用者透過自託管的方式保障資料隱私。
- 系統支援文件對話功能，並提供可驗證的資料來源引用，以確保 AI 回答的準確性並減少幻覺。
- 具備類似 NotebookLM 的 Podcast 生成功能，可將上傳的文件內容轉換為語音摘要與討論。
- 專案的前端介面是透過「vibe-coding」方法與 Loveable 工具生成，並使用 React 與 TypeScript 開發。
- 後端架構整合了 Supabase 與 N8N，分別負責核心資料庫儲存以及複雜的自動化工作流邏輯。
- 部署時需在 Supabase 設定 Edge Functions，並關閉舊版的 JWT 密鑰驗證，以適應最新的內部安全驗證機制。
- 若要使用語音生成功能，必須在自託管的 N8N 伺服器上安裝 FFMPEG，該功能無法在 N8N 雲端版上運行。
- 雖然專案程式碼採 MIT 授權，但底層使用的 N8N 具有持續性使用授權，若要將其包裝為商業 SaaS 產品，可能需要額外取得 N8N 企業授權。

### 相關問題

- [如何將 InsightsLM 部署到完全本地端的環境並結合 Ollama 使用開源模型？](chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/sidepanel.html#related)
- [N8N 的持續性使用授權（Sustainable Use License）對企業商業化營運有哪些具體限制？](chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/sidepanel.html#related)
- [在透過 Docker 部署自託管 N8N 時，應該如何正確配置 Dockerfile 以安裝 FFMPEG？](chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/sidepanel.html#related)

### 官網

[github](https://github.com/theaiautomators/insights-lm-public)

