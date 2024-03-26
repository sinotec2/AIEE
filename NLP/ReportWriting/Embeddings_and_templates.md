---
layout: default
title: Embeddings and templates
parent: 生成式AI協助報告撰寫
grand_parent: 自然語言處理
nav_order: 99
date: 2023-09-13
last_modified_date: 2023-09-15 16:02:26
tags: AI chat report
---

# Embeddings and templates
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

## embedding

嵌入[tutorial](https://platform.openai.com/docs/guides/embeddings)

- 什麼是嵌入？OpenAI 的文本嵌入衡量文本字符串的相關性。嵌入通常用於：
  - 搜索（結果按與查詢字符串的相關性排名)
  - 聚類（文本字符串按相似性分組）
  - 推薦（推薦具有相關文本字符串的項目）
  - 異常檢測（識別出相關性很小的異常值）
  - 多樣性測量（分析相似性分佈）
  - 分類（文本字符串按最相似的標籤進行分類）

### 問答式知識管理

- 範例：智慧化知識管理問答解決方案：利用 ChatGPT 和 Embedding 的 LLM 模型應用 by SimonLiu(2023/06) @[Medium](https://blog.infuseai.io/custom-km-qa-solution-chapgpt-openai-api-embedding-6a3c30860fbc)
- ![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*LUM0wSuumOspP-mEAzwNLg.png)
- ![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*_OAH1R7la2rSeCLzzA7NPA.png)
- 用到了[streamlit](https://docs.streamlit.io/)之UI

### playground example

[openAI playground](https://platform.openai.com/playground)

- 系統消息可用於指定模型在其回復中使用的角色、任務說明、步驟方法說明、文章風格、
  - 當我請求幫助寫一些東西時，你會回復一份文檔，其中每個段落至少包含一個笑話或有趣的評論。
  - 您將獲得兩篇關於同一主題的文章（用 XML 標籤分隔,eg <article>）。首先總結每篇文章的論點。然後指出哪一個提出了更好的論點並解釋原因。
  - 您將獲得論文摘要和建議的標題(以python dict形式)。論文標題應該讓讀者清楚地了解論文的主題，但也應該引人注目。如果標題不符合這些標準，請提出 5 個替代方案。
  - 使用以下分步說明來響應用戶輸入。第 1 步 - 用戶將為您提供三引號中的文本。用一個句子總結這段文字，並加上前綴“Summary:”。步驟 2 - 將步驟 1 中的摘要翻譯成西班牙語，並添加前綴“翻譯：”。

playground 範例

- 文字處理/生成
  - Summarize for a 2nd grader:Simplify text to a level appropriate for a second-grade student.
  - Parse unstructured data:Create tables from unstructured text.
  - Mood to color:Turn a text description into a color.
  - Turn by turn directions: Convert natural language to turn-by-turn directions.
  - Rap battle writer:Generate a rap battle between two characters.
- 專業文書
  - Keywords: Extract keywords from a block of text.
  - Product name generator:Generate product names from a description and seed words.
  - Memo writer:Generate a company memo based on provided points.
  - Airport code extractor:Extract airport codes from text.
  - Lesson plan writer:Generate a lesson plan for a specific topic.
  - Grammar correction: Convert ungrammatical statements into standard English.
- 聊天、對話
  - Emoji Translation﹕Translate regular text into emoji text.
  - Emoji chatbot:Generate conversational replies using emojis only.
  - Marv the sarcastic chat bot:Marv is a factual chatbot that is also sarcastic.
  - Interview questions:Create interview questions.
  - Socratic tutor:Generate responses as a Socratic tutor.
  - Meeting notes summarizer:Summarize meeting notes including overall discussion, action items, and future topics.
  - Review classifier:Classify user reviews based on a set of tags.
  - Pro and con discusser:Analyze the pros and cons of a given topic.
- 電腦專業
  - Calculate time complexity：Find the time complexity of a function.
  - Explain code:Explain a complicated piece of code.
  - Python bug fixer:Find and fix bugs in source code.
  - Spreadsheet creator:Create spreadsheets of various kinds of data.
  - Tweet classifier:Detect sentiment in a tweet. 
  - VR fitness idea generator:Generate ideas for fitness promoting virtual reality games.  
  - Function from specification:Create a Python function from a specification.
  - Improve code efficiency:Provide ideas for efficiency improvements to Python code.
  - Single page website creator:Create a single page website.
  - Translation:Translate natural language text.
  - Natural language to SQL:Convert natural language into SQL queries

In/Out\ Field|一般學生|專業文書|聊天、對話|電腦專業
-|-|-|-|-
Extract/Summarize|2nd grader/Parse unstructured/Mood to color|Keywords/Meeting/Review classifier|-|Explain code/Tweet/
Generate|rap|Product name/Lesson plan|Marv/Interview/Socratic/Emoji/Pro and con|Spreadsheet/VR/Function/website/SQL
Transform|Turn|Grammar/Airport/Memo|Emoji Translation|Calculate time/Python/Improve code/Translation
code*||||Python/SQL/website/Improve/time/Explain/Function
NatureLanguage*|Turn|||translation/SQL
StructureData*|Parse|||Spreadsheet

## 文件模板

基于微模板的法院裁判文书辅助生成的方法和系统 by 万玉晴、聂耀鑫、张亮(2019)@[patents.google](https://patents.google.com/patent/CN110888943A/zh)

### 文案工具

10 個最佳 AI 寫作工具和生成器（以及 2 個要避免的 AI 作家）by  馬特阿爾格倫 研究的 WSR團隊SEPTEMBER 13, 2023 @[websiterating](https://www.websiterating.com/zh-TW/productivity/best-ai-writing-tools/)

### 範例

- [用chatgpt寫報告的6好處/](https://gooptions.cc/用chatgpt寫報告的6好處/)

```bash
產品名稱：智能手錶
目標市場：中國大陸
市場規模：？
市場趨勢：？
競爭優勢：？
建議策略：？
```

- [ChatGPT怎麼用？透過寫報告、程式範例 讓你快速掌握人工智能對話技巧](https://tw.news.yahoo.com/chatgpt怎麼用-透過寫報告-程式範例-讓你快速掌握人工智能對話技巧-053834185.html)
  - ChatGPT 主要有 11 大功能與 38 種應用場景

![](https://media.zenfs.com/en/cnyes.com.tw/1b98425fc0a3d846a3ec3ae77c08df51)
  - 「寫出一篇有關＿＿＿的研究報告，報告須引述＿＿＿，並引用＿＿＿的觀點。」
  - 「你現在是個＿＿專家，請幫我用＿＿＿寫一個函式，它需要做到＿＿功能。」

- 如何使用 AI ChatGPT 指令 – 3 倍提升寫程式、寫報告等工作效率？ [思程](https://www.innopreneur.io/blogs/technology/martech/ai-openai-chatgpt-prompt-generator/)
  - 報告簡介：為［報告主題］寫一段簡介。
  - 生成大綱：為［報告主題］編制大綱，包括前言、主要段落和結論。
  - 編寫結構：為［報告主題］寫一個大綱或組織結構。
  - 編寫草稿：為［報告主題］寫一篇初稿，需包含［數量］個可進一步闡述的要點。
  - 研究報告：寫一篇關於［研究主題］的報告，引用最新的研究並引用專家的意見。
  - 反駁觀點：就［附上論述］提出合理的反駁論點，每點需有佐證。
  - 報告結論：總結以下內容的主要觀點和建議。［附上內容］
  - 資料來源：為［報告主題］提供可靠且高質量的資料來源或參考文獻。
- 使用 ChatGPT 指令寫文本：生成不同風格和語調的文章
  - 撰寫標題：為［文章主題］寫一個吸引人的標題。遵循［規則例如：加表情符號］
  - 撰寫文章：針對［特定主題］生成博客文章，風格要求［例如：專業］。
  - 產品文案：將以下關鍵字生成產品文案，強調［例如：功能和價值］。［附上關鍵字］
  - 修改文法：檢查並修正以下文章的文法錯誤，並提出改進建議。［附上文章］
  - 優化文章：重寫以下文章，使其更有說服力和吸引力。［附上需要修改文章］
  - 翻譯文章：將以下文章翻譯成［例如：英文］。［附上待翻譯的文章］
  - 精簡修改：將以下段落縮減至 50 字內，保留核心信息。［附上段落］
  - 社交貼文：以［某主題］為基礎，寫一個引人共鳴的社交媒體貼文。
  - 回覆電郵：以［職業］的身份寫一封電郵，涵蓋［重點內容］。［附上電郵內容］
- 使用 ChatGPT 指令整理資料：高效處理數據、抽出重點和簡化分析
  - 搜集資料：找有關［某個主題］的最新研究和統計數據。
  - 分析數據：分析以下數據，找出［特定因素］與［相關變數］之間的關聯。［附上數據］
  - 視覺數據：請將以下數據視覺化，方便展示［某個觀點］。［附上數據］
  - 數據報告：根據以下數據，寫有關於［某個主題］的簡報。［附上數據］
  - 摘錄重點：從以下報告中抽出最重要的五個觀點。［附上報告連結或內容］
  - 尋求建議：根據以下數據分析結果，提供改善和優化建議。［附上數據分析結果］
  - 加入數據：為以下文章添加［某個主題］相關的統計數據和研究成果。［附上文章］

## chatGPT code interpreter

-  ChatGPT Code Interpreter 八種應用：分析 Excel、製作圖表與動畫
 by [ Esor Huang 7月 08, 2023 ](https://www.playpcesor.com/2023/07/chatgpt-code-interpreter-excel.html)
 
## 什麼是 Azure AI 文件智慧服務？

2023/09/11@[learn.microsoft](https://learn.microsoft.com/zh-tw/azure/ai-services/document-intelligence/overview?view=doc-intel-3.1.0)
