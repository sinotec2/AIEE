---
epoch: 1777880730272
modelKey: "gpt-5-mini|github-copilot"
topic: "Emoji Insertion Rules"



tags:
  - copilot-conversation
---

**user**: Add relevant emojis to enhance {}. Follow these rules:
    1. Insert emojis at natural breaks in the text
    2. Never place two emojis next to each other
    3. Keep all original text unchanged
    4. Choose emojis that match the context and tone
    Return only the emojified text.
[Context: Notes: NLP/bilingual/DEEPL.md]
[Timestamp: 2026/05/04 15:45:30]

**ai**: ---
layout: default
title: DEEPL
parent: Bilingual AI Processing
grand_parent: 自然語言處理
nav_order: 99
date: 2026-05-04
last_modified_date: 2026-05-04T05:28:34
tags: AI chat
---

# DEEPL 🌐
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents 📑
  </summary>
  {: .text-delta }
- TOC 📚
{:toc}
</details>
---

## 背景 🌟

![](pngs/Pasted%20image%2020260504143718.png)
🖼️
![](pngs/Pasted%20image%2020260504143904.png)
🖼️
![](pngs/Pasted%20image%2020260504144212.png)
🖼️

```bash
pip install deepl
```
💻

```python
import deepl

auth_key = "{YOUR_API_KEY}" # replace with your key
deepl_client = deepl.DeepLClient(auth_key)

result = deepl_client.translate_text("Hello, world!", target_lang="DE")
print(result.text)
```
🔑

## MCP server ⚙️

開發者工具 🔧

## DeepL MCP 伺服器 🤖

複製頁 📋

使用 DeepL MCP 伺服器，為 Claude、游標及其他 AI 代理加入翻譯功能。 🔁

### 文件索引 📚
> 
> 請於以下網址取得完整文件索引：[https://developers.deepl.com/llms.txt](https://developers.deepl.com/llms.txt) 🔗
> 
> 使用此檔案先發現所有可用頁面，再進一步探索。

**本頁會顯示：**

- DeepL MCP 伺服器的功能與使用時機 🔎
- 如何安裝並設定它以支援 Claude Code 與 Claude Desktop 🛠️
- 你的 AI 代理有哪些工具可用 🧰

該[DeepL MCP 伺服器](https://github.com/DeepLcom/deepl-mcp-server)是一個開源的（MIT 授權）[模型情境協定](https://modelcontextprotocol.io/)該伺服器讓 AI 代理能使用 DeepL 的翻譯、文字優化及詞彙表功能。MCP 讓 AI 代理透過標準化協定發現並呼叫外部工具——您的代理會向 MCP 伺服器發送工具請求，伺服器會呼叫 DeepL API 並回傳結果。 🔗

如果你想從零開始使用 DeepL API 建立自訂 MCP 伺服器，請參考[MCP 伺服器手冊](https://developers.deepl.com/docs/learning-how-tos/examples-and-guides/deepl-mcp-server-how-to-build-and-use-translation-in-llm-applications). 📘

### [​先決條件](https://developers.deepl.com/docs/getting-started/deepl-mcp-server#prerequisites) ✅

- [Node.js](https://nodejs.org/)V18 或更新版本 🟢
- 一個 DeepL API 金鑰（[建立免費帳號](https://www.deepl.com/en/pro/change-plan#developer)) 🔑

### [​快速入門](https://developers.deepl.com/docs/getting-started/deepl-mcp-server#quick-start) 🚀

直接用 npx 運行伺服器：

```
npx deepl-mcp-server
```
▶️

或者本地安裝：

```
npm install deepl-mcp-server
```
▶️

### [​配置](https://developers.deepl.com/docs/getting-started/deepl-mcp-server#configuration) 🛠️

- 克勞德密碼 🔐
    
- Claude Desktop 🖥️
    
- 其他 MCP 用戶端 🔗
    

只需一個指令，將 MCP 伺服器加入 Claude Code：

```
claude mcp add deepl -e DEEPL_API_KEY=your-api-key -- npx deepl-mcp-server
```
🔗

Claude Code 現在每次會議都能使用 DeepL 翻譯工具。 🤖

### [​可用工具](https://developers.deepl.com/docs/getting-started/deepl-mcp-server#available-tools) 🧰

設定完成後，您的 AI 代理可以使用以下工具： 🧩

| **工具**                 | **描述**                                                                          |
| ---------------------- | ------------------------------------------------------------------------------- |
| `translate-text`       | 利用自動來源語言偵測，翻譯語言間的文字                                                             |
| `translate-document`   | Translate documents (PDF, DOCX, PPTX, XLSX, HTML, TXT) with format preservation |
| `rephrase-text`        | Improve and rephrase text with customizable writing style and tone              |
| `get-source-languages` | List all available source languages                                             |
| `get-target-languages` | List all available target languages                                             |
| `get-glossary-info`    | Retrieve details about a specific glossary                                      |
| `get-glossary-entries` | Fetch dictionary entries from a glossary                                        |
| `list-glossaries`      | List all glossaries in your account                                             |

### 範例用法 💡

一旦 MCP 伺服器連接完成，你可以向你的 AI 代理提出以下問題：

- 「請用正式語氣將這封郵件翻譯成德文。」 🇩🇪
- 「把我的report.pdf翻譯成法文」 🇫🇷
- 「把這段話說得更專業一點」 ✍️
- 「DeepL 支援哪些語言？」 🌍
- 「給我看看行銷詞彙表裡的條目」 📖

客服人員會自動使用適當的 DeepL 工具來完成該請求。 🤝

### 下一步 ➡️

現在你已經知道如何使用 DeepL MCP 伺服器：

- **探索資料來源：**審查[GitHub 上的 DeepL MCP 伺服器](https://github.com/DeepLcom/deepl-mcp-server)完整文件與原始碼 🔎
- **自己打造：**請關注[MCP 伺服器手冊](https://developers.deepl.com/docs/learning-how-tos/examples-and-guides/deepl-mcp-server-how-to-build-and-use-translation-in-llm-applications)從零開始建立自訂的 MCP 伺服器 🛠️
- **設定認證：**了解[DeepL API 認證](https://developers.deepl.com/docs/getting-started/auth)以及金鑰管理 🔐
- **使用用戶端函式庫：**探索[官方 SDK](https://developers.deepl.com/docs/getting-started/client-libraries)適用於 Python、Node.js 等 📚
[Timestamp: 2026/05/04 15:46:47]