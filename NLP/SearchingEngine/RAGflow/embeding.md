---
layout: default
title: 文檔解析
parent: RAGflow
grand_parent: SearchingEngine
nav_order: 99
date: 2024-10-16 
last_modified_date: 2024-10-16 11:47:08
tags: AI chat report
---

# 文檔解析
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

- 不同文檔類型的解析方式不同
- ragflow提供了下列幾種方式，主要針對文章的樣式

1. gereral: 一般性的文檔 
2. Q&A：一對一的段落關係
  {% include question.html content="
   "Q&A" 分塊方法說明
    此塊方法支持 excel 和 csv/txt 文件格式。

    如果文件以 excel 格式，則應由兩個行組成 沒有標題：一個提出問題，另一個用於答案， 答案列之前的問題列。多工作表狀況，只要行列正確結構，就可以接受。
    如果文件以 csv/txt 格式為 用作分開問題和答案的定界符。
    未能遵循上述規則的文本行將被忽略，並且 每個問答對將被認為是一個獨特的部分。
  "%}
3. Resume：有必要的段落
4. Manual：
5. Table：
6. Paper：2欄的特殊格式
7. Book：除2欄的特殊格式，也有封面、目錄與圖表穿插
8. Law：條文的架構、換行與斷句


![pngs/2024-10-16-11-46-19.png](pngs/2024-10-16-11-46-19.png)
