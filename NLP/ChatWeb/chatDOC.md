---
layout: default
title: chatDOC的應用
parent: chatWeb的裝置與應用
grand_parent: 自然語言處理
nav_order: 99
date: 2023-08-31
last_modified_date: 2023-09-22 17:07:25
tags: AI chat
---

# chatDOC的應用
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

- 文件檔案的搜尋、解析、綜合等等對話(chatbot)有許多API、付費、或自建方案，如其他地方所做的說明。
- 實地進行測試比較，發現以chatDOC.com的表現較佳。此處即以其為測試對象，以提供未來使用的參考。

### chatDOC 簡介

- [chatDOC](https://chatdoc.com/chatdoc/#/sign-up?invite_code=7fimgzlv7f)是著名電腦作家esor2023年4月介紹推薦的優秀網站。(詳見其[推薦文章](https://www.playpcesor.com/2023/04/chatdoc-pdf-ai.html))
- 可接受檔案格式(形式)：pdf / doc / docx / markdown / epub / 
- txt / OCR
- 免費方案：登錄會員後即可得到3個免費檔案的優惠(僅限pdf檔)
- 推薦會員：每推薦一人入會可得到5個免費檔案的優惠，最多1000個檔案(30日內)
- 有'文件集'(collection)功能，類似目錄，可綜合分析集內之所有文件。
- 文檔解析時間比其他服務都長、解析較為仔細

### 付費方案

- Auto-Subscribe
  - Pro Plan 30 Days $5.99
  - Pro Plan 360 Days $59.9
- No any deals
  - Pro Plan 30 Days $7.99

### 可能應用場域

- 文義搜尋
  - 與一般全文搜尋不同，不只是相同字串的搜尋，而是按照指令相同文義
  - 環評審查、服務建議書簡報、計畫期中末簡報之答詢。
  - 可以在目錄(collection)中點選檔案指定範圍來問問題，如果計畫分包眾多、報告太複雜、零碎，直接問chatDoc可能會較為有效。
  - 除了列出原文，chatDOC也會將其濃縮或口語化，便於(即時)製作簡報
- 契約稿閱讀、審查、法律條文解讀
  - 契約內容龐雜，chatDoc可以協助找到重要細節，並提出邏輯性、口語直白的回應。
- 摘要重點
  - 下包提供內容太多，語法又不太相同，在納入本文時會發生困難，可以要求chatDOC調整成一致的語法，摘要各下包文件內容再予以整併。
  - 協助論文回顧之撰寫、條列簡報重點

### 問題與對策

- 簡體字的問題
  - 將簡體字、大陸語法的文字剪下、貼在google translate即可翻譯成繁體、台灣語法的文字。
- 資安防護
  - 有關個資、商業或技術的重要情資，在上載檔案時，使用者還是必須自行研判負責。

## 應用範例

### 文件字義搜尋

{% include question.html content="列出這份文件中有關PM2.5增量濃度的敘述" %}

這份文件中有關PM2.5增量濃度的敘述如下：

文件片段[18a]提到，本計畫的PM2.5日平均值最大增量濃度主要在高雄市本計畫排放源的附近，對其他地方的影響較為有限。
文件片段[18b]指出，營運期間2部機組同時運轉下，對於各縣市PM2.5年平均值濃度最大影響增量為0.06 μg/m3，發生在高雄市，其他地方的影響較小。
文件片段[19a]表格呈現了營運期間各敏感點的PM2.5最大增量濃度模擬評估結果，列出了鳳源社區和二苓社區的數據，包括最大增量濃度模擬值、背景值濃度註、最大增量加成背景後濃度、以及空氣品質標準。
文件片段[19b]指出，綜合上述，對於PM2.5空氣品質影響而言，本計畫營運後所衍生最大影響之增量濃度經加成背景值後，仍未能符合空氣品質標準。然而，因為濃度增量非常有限，對PM2.5的空氣品質影響也相對較小。

{% include question.html content="文件中的百分之90是怎麼回事?" %}
{% include question.html content="搜尋文件中所有的標題列" %}

### 法律條文解讀

{% include question.html content="在本文中"各級主管機關"的義務與工作項目為何?" %}

根据文档摘录，"各级主管机关"在本文件中的义务和工作项目包括：

- 定期公告固定污染源的检测频率等级，并根据条件和规定确定所需的检测等级。[2a]
- 确认固定污染源空气污染物收集设施、防制设施、使用原（物）料及燃料之项目与用量，并进行监督排放检测。[3a]
- 对符合条件的固定污染源进行例行性定期檢測，并公开排放检测的日期。[1]
- 对特定情形下的固定污染源实施功能性定期检测，如申报例行性定期检测的结果与申请操作许可证的检测值差异达到50%以上，以及存在未经操作许可证核定的收集、处理设施或排放管道排放空气污染物等情形。[2b][2c][2d]
- 对固定污染源功能性定期检测的查核，需要确认檢測計畫內容、固定污染源空气污染物收集设施、防制设施、使用原（物）料及燃料之项目与用量、监督排放檢測等。[3a]
- 对公私场所设置的空气污染防制专责人员的参与进行功能性定期检测，并要求製程操作单位同时到场确认。[3b]
- 对公私场所具备修正检测计划内容的情况，要求符合规定的检测计划修正内容，并依许可证管理办法的规定，提出操作许可证内容变更或異動之申请。[4]
- 对不符合本辦法規定的情况，应根据不同情形进行相应的处理，如通报直轄市、縣（市）主管機關、恢复下次例行性定期檢測等。[6a]
对达到特定条件下固定污染源的改善複測进行监督。[6b]
- 同意免实施例行性定期檢測的管理措施。[7a]
- 对未符合核准適用免實施例行性定期檢測之规定的情况进行回复并修正公告的檢測頻率級數。[7b]
- 对特定情形下固定污染源的处理，如连续两次例行性定期檢測结果不符合调整规定、发生稽查、功能性定期檢測或例行性定期檢測的情形，以及固定污染源製程、設施或操作條件改变致使排放量或种类增加等，回復檢測頻率級數。[9a][9b][9c][9d] 

### 摘要重點

{% include question.html content="以中學生能理解的語法，將本文的內容歸納100字的摘要。" %}
{% include question.html content="條列出本文件的簡報重點" %}
{% include question.html content="條列這份文件中有關空氣品質的章節架構。" %}
{% include question.html content="摘述本段的事實" %}