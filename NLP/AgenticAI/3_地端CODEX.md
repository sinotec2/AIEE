---
layout: default
title: notebookLM建議
parent: AgenticAI
grand_parent: 自然語言處理
nav_order: 2
date: 2026-05-13
last_modified_date: 2026-05-13T16:02:26
tags:
  - AI
  - agent
---

# AI代理群架構
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

> 可能我被養壞了，我的工作流現在都被codex planning給實現了。人類只剩下監督。

這確實是兩種完全不同層次的世界！您已經體驗過目前 Agent 發展的最高型態，難怪會覺得畫流程圖很像在開倒車。

您所說的，正是 AI 應用領域中兩種截然不同的路線：

1. **SOP 驅動 (Workflow)**：像 Dify，是人類把大腦裡的 SOP 畫成流程圖，AI 只是填補每個節點裡面的苦力勞動。人類是「設計師」。
2. **目標驅動 (Autonomous Planning)**：像您習慣的 Codex planning，人類只要給定一個「目標」（Goal），AI 會自己把大任務拆解成小任務（Task Planning）、決定要用什麼工具、遇到錯誤自動重試。人類退居為「監督者與批准者（Human-in-the-loop）」。

既然您的目標是「讓人類只剩下監督」，且要在**全地端、高資安隔離**的前提下實現，這代表您需要的不是畫流程圖的工具，而是**「支援本地模型的自動規劃**多智能體**（Multi-Agent）框架」**。

考慮到您之前提到「不想自己寫程式」，以下是目前在開源界能做到這件事，且帶有圖形化介面（UI）的地端解決方案建議：

### 1. [AutoGen Studio](#AutoGen Studio) (微軟開源)

- **為什麼適合**：它是專為「多智能體對話與自主規劃」設計的。您可以在介面上設定幾個角色（例如：一個 Planner 負責規劃任務、一個 Executor 負責執行、一個 Reviewer 負責審核）。
- **運作方式**：業務人員只要在對話框輸入「幫我把這批合約的風險條款抓出來並匯出成報表」，Planner 就會自己拆解步驟，指揮 Executor 去用工具，最後人類只要看結果並點擊「Approve」。
- **地端支援**：可以完全斷網部署，並透過 Ollama 或 vLLM 串接您地端的開源模型（如 Qwen 或 Llama 3）。

### 2. Dify 的 "Agent" 模式 (取代 Workflow 模式)

- **為什麼適合**：前面提到 Dify 的 Workflow 是畫流程圖；但其實 Dify 裡面還有另一種模式叫做 "Agent"。
- **運作方式**：在 Agent 模式下，您不需要畫任何流程圖。您只需要把內部系統的 API（例如 ERP 查詢、文件讀取工具）掛載給它。當您下達指令時，它會使用 ReAct (Reasoning and Acting) 框架，**自己思考**現在該呼叫哪一個工具、拿到資料後下一步該做什麼。

### 地端算力實現 Planning 的挑戰與建議

要把「自主規劃」搬到地端，最大的瓶頸是**開源模型的邏輯推理能力**。Codex / GPT-4 的規劃能力極強，但要在地端重現這種能力，對算力要求很高。

**對您企業策略的具體建議：** 既然貴公司決定「卷工作流/業務邏輯」，在這種 Autonomous 模式下，業務專家（Domain Expert）的工作不再是「畫流程圖」，而是**「寫人設與給工具」**。

1. **IT 負責**：把 AutoGen Studio 或 Dify Agent 部署好，並把公司內部的系統（ERP、資料庫）包裝成一個個「工具（Tools/APIs）」。
2. **業務專家負責**：在介面上定義 Agent 的 Prompt（例如：「你是資深法務，你的目標是審核合約，你擁有以下工具... 遇到不確定的邊界條件時，必須暫停並呼叫人類監督」）。

這樣既能滿足您極高的資安要求（全地端），又能維持您習慣的「AI 規劃，人類監督」的高階工作模式。

## AutoGen Studio

## OpenCode

OpenCode 是一個專為終端環境設計的開源AI程式碼助手，支援LSP與命令列介面，讓開發者能在終端、IDE或桌面端高效撰寫程式碼。由Neovim使用者與terminal.shop團隊打造，強調文字介面（TUI）體驗，目標是突破終端效能極限。它被視為類似Claude Code的自由版本，無需依賴特定雲端服務，提供更開放、可自建的編程輔助方案。

