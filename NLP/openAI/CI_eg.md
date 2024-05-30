---
layout: default
title: 程式碼解釋器範例
parent: openAI
grand_parent: 自然語言處理
nav_order: 99
date: 2024-05-30
last_modified_date: 2024-05-30 10:06:43
tags: AI chat code_interpreter
---

# 程式碼解釋器範例

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

- 目標：啟動openAI code interpreter助理，完成NLP指令(zero code)，執行csv檔案分析
- 架構
  - 指定分析檔案對象(分析單元)
  - 啟動助理(session、計費單元)
  - 接受NLP指令，上傳指令、完成分析、解析結果、列印結果

## 檔案對象範例

- 檔名：`any20240529.csv`
- 各分組的對話次數,參與人數,文件詞組,port等內容
- 最末列為"合計"，不應納入分析。
- 欄位值有可能會有加號(`+`)、千分位(`,`)等字元標示的干擾，並非單純的整數
 
```python
In [64]: !head -n1 any20240529.csv
,分組,對話次數,參與人數,文件詞組,port
In [65]: !tail -n1 any20240529.csv
14,合計,750+,59+,"3,357,487+",NaN
```

## 安裝與環境設定

- `conda activate llm`：啟動python  3.9.16
- `pip install openai`：以下使用 open 1.30.4
- `export OPEN_AI_KEY='sk-***'`：環境變數
- `pip install ipython && ipython`：安裝、啟動作業環境
  
## 執行步驟

### 指定分析檔案對象

```python
from openai import OpenAI
client = OpenAI()

fname='any20240529.csv'
file = client.files.create(
  file=open(fname, "rb"),
  purpose='assistants'
)
```

### 啟動助理

```python
assistant = client.beta.assistants.create(
  instructions="You are a personal python tutor. When asked a coding question, write and run code to answer the question.",
  model="gpt-4o",
  tools=[{"type": "code_interpreter"}],
  tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)
```

### 定義串流

- 串流的內容需要綁定**主題**(`thread_id`)與前述**助理**(`assistant_id`)
- 構成**主題**(`thread`)
  - 每個NLP指令(`cmd`)需搭配角色(`role`)、附件(`attachments`)、並包括在內容(`content`)之內，以形成主題的訊息(`messages`)
- 定義完`stream`，隨即提交執行(讀取即執行)。
- 後處理：`event`的內容非常龐雜，由其中萃取我們需要的訊息即可。
  - 名稱篩選：`event`名稱為`'thread.message.completed'`
  - 內容篩選：`event.data.content[0].text.value`


```python
def run_cmd(cmd):
  thread = client.beta.threads.create(
    messages=[
    {
      "role": "user",
      "content": "I need to solve the problem \`"+cmd+"\`. Can you help me?",
      "attachments": [
        {
          "file_id": file.id,
          "tools": [{"type": "code_interpreter"}]
        }
      ]
    }
  ]
  )

  stream = client.beta.threads.runs.create(
    thread_id=thread.id,assistant_id=assistant.id,stream=True
  )
  for event in stream:
    if  event.event=='thread.message.completed': print(event.data.content[0].text.value)

  return
```

## 執行與結果

### 執行方式

```python
In [67]: run_cmd("哪個分組有最高的「參與人數」?")
In [68]: run_cmd("哪各分組有最高的「參與人數」，且分組名稱不等於「合計」?")
In [69]: run_cmd("哪個分組有最高的「參與人數」，注意欄位的值有可能有加號(「+」)的干擾，且分組名稱不等於「合計」?")
```

### 執行結果

```python
In [69]: run_cmd("哪個分組有最高的「參與人數」，注意欄位的值有可能有加號(「+」)的干擾，且分組名稱不等於「合計」?")
Sure, let's start by inspecting the contents of the uploaded file to understand its structure. This will help us to solve the problem by identifying the group with the highest "participant count."

We will load and display the first few rows of the file to get an idea of its format.
It seems the file format is not recognized as CSV or Excel. Let's check the exact name and extension of the file to identify its type.
The file does not have an extension, which is probably why it couldn’t be identified properly. Let’s try reading the file as a CSV with different delimiters and determine its structure.

We will read the first few lines as text to better understand how to parse it.
The file appears to be in CSV format, and it looks like it uses commas as delimiters. Additionally, certain columns have "+" signs and spaces within the values.

Here is the plan:

1. Load the file as a CSV, handling potential spaces and "+" signs in the participant counts.
2. Filter out any rows where the group name is "合計".
3. Convert the "參與人數" column to numeric values by removing any "+" signs.
4. Identify the group with the highest participant count.

Let's perform these steps in code.
The dataframe has been loaded successfully. Now, let's focus on cleaning and processing the "參與人數" column to identify the group with the highest participant count. We will remove any "+" signs and convert the values to numeric. Also, we will filter out rows where the group name is "合計".
The group with the highest number of participants is \( 研發及資訊部 \) with 7 participants.

If you need any further analysis or assistance, feel free to ask!
```