---
title: 在LibreChat執行python
tags: AI
layout: default
parent: LibreChat
grand_parent: Utilities
nav_odrer: 3
date: 2025-11-01
modify_date: 2025-11-23T16:08:00
---


# 在LibreChat執行python

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


## 步驟1️⃣登入介面

- 註冊：姓名、稱謂
- 帳號：任何"**長得像**"email的帳號 (英數@英數)
- 密碼：8碼、請自行記得、系統不會寄信給您找回密碼。


| ![](pngs/Pasted%20image%2020251030121437.png) | ![](pngs/Pasted%20image%2020251030121641.png) |
| --------------------------------------------- | --------------------------------------------- |
| 第一次請自行**註冊**🤩                                | 電子郵件註冊。密碼至少8碼。🎱                              |

## 步驟2️⃣啟動MCP

- 如果沒有看到`mcp-python-interpreter`字樣，需要點擊`MCP`來啟動它。


| ![](pngs/Pasted%20image%2020251123164819.png) |
| :-------------------------------------------: |
|            點擊還沒有連線的MCP伺服器，讓它連線、啟動             |
| ![](pngs/Pasted%20image%2020251123164904.png) |
|   出現`mcp-python-interpreter`表示系統將會回應處理數據的指令   |

<a href="https://www.librechat.ai/videos/mcp_one_click_init.mp4">MCP之啟動mp4</a>


## 步驟3️⃣上傳要分析的數據

| ![](pngs/Pasted%20image%2020251123165432.png) |
| :-------------------------------------------: |
|                按下迴紋針、點選"文本上傳"                 |
| ![](pngs/Pasted%20image%2020251123165556.png) |
|                     上載成功                      |

## 步驟4️⃣點選適當的語言模型

- 因為MCP伺服器就在地端、容器內，所以外部的語言模型動不了，必須選擇地端模型。
- 地端模型中，選一個比較單純的語言模型，如llama3.1:8b，寫程式一個指令一個動作，不會需要太多的推理過程(如vLLM:GPT-OSS)。一翻兩瞪眼。

![](pngs/Pasted%20image%2020251123165933.png)

## 步驟5️⃣自然語言控制程式

- 範例

> 我會給你一個部門報名午餐的名單，請寫一個python程式，分析各部門的總人數，並且執行它，**告訴我結果就好了**。
> 跑碼了。檔案是big5編碼，不是"資資部"，而是"能資部"，重新檢查一下，不要有錯。請重作。
>  
>  寫一個讀取現在時刻的python程式，並且執行它。
>  我需要改成台北時刻啦

- 如果忘了講"直接告訴我結果"，LLM會提供一個程式，按右上角的`執行程式碼`，會連回LibreChat API使用其計算資源。請按"取消"。直接補上"請給我結果"就好了。

|  ![](pngs/Pasted%20image%2020251123170531.png)   |
| :----------------------------------------------: |
|                                                  |
|  ![](pngs/Pasted%20image%2020251123170725.png)   |
| (會連回LibreChat.ai公司，使用其API與計算資源、此處按取消即可。修改prompt) |

- 寫出檔案，還要加上mcp.filesystem，在mcp-python-interpreter內無法單獨完成。範例如下：

> 我會給你一個部門報名午餐的名單，請寫一個python程式，按照各種便當的類別，給我各類便當的訂餐同仁資料表，共4個csv檔案。儲存在/app/logs/目錄下。

- 如果需要直接執行python，請改在jph上作業。🧐
	- 🐍python 執行資源
		- 位置：jph
	- 手冊：
		- 💊[ JupyterHub介面]()
		- 💊[JupyterNB的執行](l)

| ![](pngs/Pasted%20image%2020251123172453.png) |
| :-------------------------------------------: |
|               登入jph(只需帳號、無須密碼)                |

## 步驟6️⃣LibreChat工作站檔案管理

- LibreChat的開放路徑`/app/logs`，可以在[filebrowser]()中出現，目前採開放管理、每日清理政策。

| ![](pngs/Pasted%20image%2020251123210512.png) |
| :-------------------------------------------: |
|    在filebrowser中出現了各式便當.csv檔案，使用者可以下載、刪除。     |
| ![](pngs/Pasted%20image%2020251123211049.png) |
|     filebrowser介面點選檔案名稱(隨即下載)，右鍵也會出現其他功能。     |

## 概念說明🧠：什麼是 MCP 與 MCP-Python-Interpreter？

在深入探討 `mcp-python-interpreter` 之前，我們必須先理解其所依賴的基礎——模型內容協定（MCP）。

### MCP 核心概念速覽

#### 定義：AI的「通用遙控器」

MCP可以被形象地比喻為一個「通用遙控器」。它是一套標準化的通訊規則（Protocol），定義了AI應用（客戶端，如Claude Desktop）如何與各式各樣的外部資料來源和工具（伺服器）進行互動。這些工具可以小至一個本地檔案讀取器，大至一個企業級資料庫或複雜的API服務。

#### 目標：打破整合孤島

在MCP出現之前，每當需要將一個AI模型（如Claude）與一個新的外部系統（如GitHub或本地檔案）連接時，開發者都必須編寫客製化的整合程式碼。這種「點對點」的整合方式不僅耗時，且難以擴展和維護。MCP的目標正是要用一個統一、開放的標準取代這種碎片化的現狀，從而建立一個可互通、可擴展、更可靠的AI工具生態系。

#### 架構：客戶端-伺服器模型

MCP採用了經典的客戶端-伺服器（Client-Server）架構。AI應用程式（如IDE插件、聊天介面）作為**MCP客戶端**，而提供資料或工具能力的程式則作為**MCP伺服器**。兩者之間透過標準化的雙向資料流進行通訊，客戶端可以向伺服器請求資料或觸發動作，伺服器則回傳結果或狀態更新。

![MCP架構示意圖](https://agents-download.skywork.ai/image/rt/ae23cd06d7f1be7871d4da02f7ac7f02.jpg)

模型內容協定（MCP）架構示意圖，展示了AI應用（客戶端）如何透過標準化協定與外部資料和工具（伺服器）進行雙向通訊

### 深入 `mcp-python-interpreter`

#### 精準定義

`mcp-python-interpreter` 是一個具體的MCP伺服器實現，其核心功能是為MCP客戶端（如AI Agent）提供一個受控的環境，使其能夠執行Python程式碼、管理Python套件以及在指定的目錄內操作檔案系統。它將Python的強大能力「暴露」給AI，使其從一個程式碼建議者轉變為一個真正的程式碼執行者。

#### 專案歸屬與普及性

該專案由開源貢獻者 `yzfly` 在GitHub上發起並主要維護，是社群中最早出現且廣受歡迎的Python執行器MCP伺服器之一。根據PulseMCP等第三方平台的統計，其下載量已達17.5k次（截至2025年4月），顯示出其在AI開發者社群中的高度普及性。

#### 核心價值

對於AI工程師而言，`mcp-python-interpreter` 的直接價值在於其「即插即用」的便利性。它提供了一種極其簡單、快速的方式，讓本地或遠端的LLM Agent具備與Python環境互動的實用能力。開發者無需深入了解MCP協定的複雜細節，只需幾行指令便可啟動一個功能完備的Python執行伺服器，極大地降低了構建Agentic AI應用的門檻。

source: [MCP-Python-Interpreter MCP Server：AI工程師深度解析(Skywork 09/30/2025)](https://skywork.ai/skypage/zh-hant/MCP-Python-Interpreter-MCP-Serve：AI工程師深度解析/1972822984677715968)