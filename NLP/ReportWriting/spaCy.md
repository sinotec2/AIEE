---
layout: default
title: spaCy之應用
parent: 生成式AI協助報告撰寫
grand_parent: 自然語言處理
nav_order: 99
date: 2023-10-05
last_modified_date: 2023-10-05 16:02:26
tags: AI chat report
---

# spaCy之應用

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

- [官網](https://spacy.io/)。有英文解析範例，文字轉詞性分類。
- 中文說明
  - 【自然語言處理 - spaCy】初探強大的工具庫spaCy， 讓機器讀懂我們的語言吧。 by [阿Han的軟體技術棧](https://vocus.cc/article/64ad4ab6fd89780001f182eb)
    - 詞性Parser解析、分析相依關係、Named Entity Recognition (NER)

## txt2db範例

spaCy 是一款用於自然語言處理（NLP）任務的強大工具，它可以用於文字處理、實體辨識、句法分析等任務。 將報告文字資料庫化的過程通常包括以下步驟：

1. **文字資料收集**：首先，您需要收集報告文字數據，可以是從各種來源取得的文字檔案或資料。

2. **資料預處理**：在將文字資料儲存到資料庫之前，需要進行一些資料預處理。 這包括去除不需要的特殊字元、標點符號、停用詞等。 spaCy 提供了用於文字清理的功能，如標記化、詞幹提取和停用詞移除。

3. **實體識別**：如果報告文字包含命名實體（如人名、地名、組織機構名等），您可以使用 spaCy 進行實體識別。 這有助於將文本中的實體資訊提取出來，以便更好地組織和檢索。

4. **句法分析**：句法分析可以幫助您理解文本中單字之間的關係。 spaCy 提供了句法分析的功能，可以用於提取詞彙之間的依賴關係，例如主詞、謂語和受詞。

5. **文字特徵提取**：根據您的需求，可以從文本中提取各種特徵，例如關鍵字、主題標籤、情緒分析等。 spaCy 可以用於詞彙特徵提取。

6. **資料庫建模**：選擇一個資料庫系統（如MySQL、PostgreSQL、MongoDB等）來儲存文字資料。 根據您的資料結構，設計資料庫模型並建立相應的表格。

7. **資料導入**：將經過預處理和特徵提取的文字資料匯入資料庫。 您可以使用資料庫操作庫（如SQLAlchemy）來進行這些操作。

以下是一個簡單的範例，展示如何使用 spaCy 處理文字並將其儲存到資料庫中（以SQLite為例）：

```python
import spacy
import sqlite3

# 載入spaCy模型
nlp = spacy.load("en_core_web_sm")

# 範例文字
text = "這是一份報告文字。報告中包含了一些重要資訊。"

# 預處理文本
doc = nlp(text)

# 建立SQLite資料庫連接
conn = sqlite3.connect("report_database.db")

# 建立遊標
cursor = conn.cursor()

# 建立報表表格
cursor.execute("""
     CREATE TABLE IF NOT EXISTS reports (
         id INTEGER PRIMARY KEY,
         text TEXT,
         entities TEXT,
         syntax_tree TEXT
     )
""")

# 擷取實體資訊
entities = ', '.join([ent.text for ent in doc.ents])

# 提取句法分析資訊
syntax_tree = ', '.join([f"{token.text} ({token.dep_})" for token in doc])

# 插入數據
cursor.execute("INSERT INTO reports (text, entities, syntax_tree) VALUES (?, ?, ?)",
                (text, entities, syntax_tree))

# 提交更改並關閉連接
conn.commit()
conn.close()
```

這只是一個簡單的範例，實際應用中可能需要更複雜的資料處理和模型。 具體的資料庫選擇和表格結構設計也會根據您的需求而改變。 使用 spaCy 可以簡化文字處理和特徵提取的過程，有助於將文字資料有效地儲存到資料庫中。
