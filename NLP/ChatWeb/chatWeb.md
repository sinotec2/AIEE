---
layout: default
title: chatWeb的裝置與應用
parent: 自然語言處理
nav_order: 99
date: 2023-08-31
last_modified_date: 2023-08-31 10:32:48
tags: AI chat
has_children: true
permalink: /NLP/ChatWeb
---

# chatWeb的裝置與應用
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

- 這項openAI的gpt3.5 turbo API應用是源自於[SkywalkerDarren/chatWeb(2022/05)](https://github.com/SkywalkerDarren/chatWeb)提供的程式碼。安裝及相關需求詳見github說明。此處說明應用的方式與結果啟發。
- 安裝在[node03:7860](http://200.200.31.47:7860/)。將會使用到node03儲存字庫(csv檔)與finetune模型bin檔。可以使用postgres(但未啟用)。
- 測試1天(含以下)總計使用0.11鎂。尚未測試多人使用會發生甚麼情況
- 除了解析網頁之外，套件也可以解析本地的文字檔案。接受的格式包括pdf、docx、以及txt檔案。
- 類似功能之服務介紹如下

### chatDOC

- [chatDOC](https://chatdoc.com/chatdoc/#/sign-up?invite_code=7fimgzlv7f)是著名電腦作家esor2023年4月介紹推薦的優秀網站。(詳見其[推薦文章](https://www.playpcesor.com/2023/04/chatdoc-pdf-ai.html))
- 可接受檔案格式(形式)：pdf / doc / docx / markdown / epub / txt / OCR
- 免費方案：登錄會員後即可得到3個免費檔案的優惠(僅限pdf檔)
- 推薦會員：每推薦一人入會可得到5個免費檔案的優惠，最多1000個檔案(30日內)
- 付費方案
  - Auto-Subscribe
    - Pro Plan 30 Days $5.99
    - Pro Plan 360 Days $59.9
  - No any deals
    - Pro Plan 30 Days $7.99
- 有'文件集'(collection)功能，類似目錄，可綜合分析集內之所有文件。
- 文檔解析時間比其他服務都長

### chatPDF

- [chatpdf.com官網](https://www.chatpdf.com/)
- 特色
  - 使用chatGPT3.5作為語言模型
  - 會將pdf標題存留，只需點擊標題，即可展開檔案與過去的對話。
  - 可以很精確地回答pdf的細節內容。跨頁仍會有解讀上的問題。
  - 可以進行計算
- 免費版本
  - 120 pages/PDF
  - 10 MB/PDF
  - 3 PDFs/day
  - 50 questions/day
- Plus版本 $5/mo
  - 2,000 pages/PDF
  - 32 MB/PDF
  - 50 PDFs/day
  - 1000 questions/day

### PDF GPT(pdfChatter)

- [bhaskartripathi/pdfChatter](https://huggingface.co/spaces/bhaskartripathi/pdfChatter)是個架在huggingface空間的平台，輸入openAI的API token之後，與chatWeb就有類似的功能，差異只在不能儲存歷史。
- 不過把token貼在網路上似乎不是一件聰明的事。還是不要輕易嘗試。
![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-09-06-15-32-25.png)

### chat-with-pdf

- 這個huggingface的平台[fffiloni/langchain-chat-with-pdf](https://huggingface.co/spaces/fffiloni/langchain-chat-with-pdf)用的全是huggingface的公開模型，因此沒有token的需要。其他界面也都很類似。
- 平台上用了3個模型

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-09-06-15-59-11.png)

- 用的是huggingface的計算資源，所以解析與推演的速度慢了很多(還有queue的問題)。

