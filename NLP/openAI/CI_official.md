---
layout: default
title: 程式碼解釋器
parent: openAI
grand_parent: 自然語言處理
nav_order: 99
date: 2024-05-26
last_modified_date: 2024-05-26 19:28:52
tags: AI chat
---


# 程式碼解釋器
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


# 程式碼解釋器測試版

- 程式碼解釋器允許助手在沙盒執行環境中編寫和運行 Python 程式碼。 
- 該工具可以處理具有不同資料和格式的文件，並產生具有資料和圖形影像的文件。 
- 程式碼解釋器可讓您的助手迭代運行程式碼以解決具有挑戰性的程式碼和數學問題。 
- 當 Assistant 編寫無法運行的程式碼時，它可以透過嘗試執行不同的程式碼來迭代此程式碼，直到程式碼執行成功。

請參閱此處的[快速入門](https://platform.openai.com/docs/assistants/overview?context=with-streaming)，以了解如何開始使用程式碼解釋器。

## 怎麼運作的

代碼解釋器每次會話收費 0.03 美元。 如果您的 Assistant 在兩個不同的執行緒中同時呼叫程式碼解釋器（例如，每個最終使用者一個執行緒），則會建立兩個程式碼解釋器會話。 預設情況下，每個會話的活動時間為一小時，這意味著如果使用者在同一執行緒中與程式碼解釋器互動最多一小時，您只需為每個會話付費。

### 啟用程式碼解釋器

在 Assistant 物件的 tools 參數中傳遞 code_interpreter 以啟用程式碼解釋器：

```Python
assistant = client.beta.assistants.create(
  instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model="gpt-4o",
  tools=[{"type": "code_interpreter"}]
)
```

然後，模型根據使用者請求的性質決定何時在運行中呼叫程式碼解釋器。 可以透過在助手的說明中進行提示（例如，「編寫程式碼來解決此問題」）來促進這種行為。

### 將文件傳遞給程式碼解釋器

使用此助手的所有運作、都可以存取在助手層級傳遞的檔案：

```Python
# Upload a file with an "assistants" purpose
file = client.files.create(
  file=open("mydata.csv", "rb"),
  purpose='assistants'
)

# Create an assistant using the file ID
assistant = client.beta.assistants.create(
  instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model="gpt-4o",
  tools=[{"type": "code_interpreter"}],
  tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)
```

文件也可以在線程層級傳遞。 這些文件只能在特定線程中存取。 使用文件上傳端點上傳文件，然後將文件 ID 作為訊息建立請求的一部分傳遞：

```Python
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "I need to solve the equation `3x + 11 = 14`. Can you help me?",
      "attachments": [
        {
          "file_id": file.id,
          "tools": [{"type": "code_interpreter"}]
        }
      ]
    }
  ]
)
```

檔案的最大大小為 512 MB。 Code Interpreter 支援多種文件格式，包括 `.csv`、`.pdf`、`.json` 等。 有關支援的文件副檔名（及其相應的 MIME 類型）的更多詳細信息，請參閱下面的支援的文件部分。

### 讀取程式碼解釋器產生的圖像和文件

API 中的程式碼解釋器也會輸出文件，例如產生圖像圖表、CSV 和 PDF。 產生的文件有兩種類型：

1. 圖片
2. 資料檔案（例如包含助手產生的資料的 csv 檔案）

當程式碼解釋器產生映像時，您可以在助手訊息回應的 `file_id` 欄位中尋找並下載該檔案：

```json
{
    "id": "msg_abc123",
    "object": "thread.message",
    "created_at": 1698964262,
    "thread_id": "thread_abc123",
    "role": "assistant",
    "content": [
    {
      "type": "image_file",
      "image_file": {
        "file_id": "file-abc123"
      }
    }
  ]
  # ...
}
```

然後可以透過將檔案 ID 傳遞給 Files API 來下載檔案內容：

```Python
from openai import OpenAI

client = OpenAI()

image_data = client.files.content("file-abc123")
image_data_bytes = image_data.read()

with open("./my-image.png", "wb") as file:
    file.write(image_data_bytes)
```

當程式碼解釋器引用檔案路徑（例如，「下載此 csv 檔案」）時，檔案路徑會作為註解列出。 您可以將這些註釋轉換為下載檔案的連結：

```json
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1699073585,
  "thread_id": "thread_abc123",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "The rows of the CSV file have been shuffled and saved to a new CSV file. You can download the shuffled CSV file from the following link:\n\n[Download Shuffled CSV File](sandbox:/mnt/data/shuffled_file.csv)",
        "annotations": [
          {
            "type": "file_path",
            "text": "sandbox:/mnt/data/shuffled_file.csv",
            "start_index": 167,
            "end_index": 202,
            "file_path": {
              "file_id": "file-abc123"
            }
          }
          ...
```

### Code Interpreter的輸入輸出日誌

透過列出呼叫 Code Interpreter 的 Run 的步驟，您可以檢查 Code Interpreter 的程式碼輸入和輸出日誌：

```python
run_steps = client.beta.threads.runs.steps.list(
  thread_id=thread.id,
  run_id=run.id
)
```

```json
{
  "object": "list",
  "data": [
    {
      "id": "step_abc123",
      "object": "thread.run.step",
      "type": "tool_calls",
      "run_id": "run_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "step_details": {
        "type": "tool_calls",
        "tool_calls": [
          {
            "type": "code",
            "code": {
              "input": "# Calculating 2 + 2\nresult = 2 + 2\nresult",
              "outputs": [
                {
                  "type": "logs",
                  "logs": "4"
                }
                        ...
 }
```

## 支援的文件

對於文字/ MIME 類型，編碼必須是 utf-8、utf-16 或 ascii 之一。

|File format|MIME type|
|-|-|
.c|text/x-c
.cs|text/x-csharp
.cpp|text/x-c++
.doc|application/msword
.docx|application/vnd.openxmlformats-officedocument.wordprocessingml.document
.html|text/html
.java|text/x-java
.json|application/json
.md|text/markdown
.pdf|application/pdf
.php|text/x-php
.pptx|application/vnd.openxmlformats-officedocument.presentationml.presentation
.py|text/x-python
.py|text/x-script.python
.rb|text/x-ruby
.tex|text/x-tex
.txt|text/plain
.css|text/css
.js|text/javascript
.sh|application/x-sh
.ts|application/typescript
.csv|application/csv
.jpeg|image/jpeg
.jpg|image/jpeg
.gif|image/gif
.png|image/png
.tar|application/x-tar
.xlsx|application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
.xml|application/xml or "text/xml"
.zip|application/zip