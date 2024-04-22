---
layout: default
title: 通過API使用FastChat
parent: FastChat
grand_parent: 自然語言處理
nav_order: 99
date: 2024-01-25
last_modified_date: 2024-01-25 09:35:43
tags: AI chat
---


# 通過API使用FastChat
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

## gradio_client

要透過API進行查詢，需使用`gradio_client Python`庫或`@gradio/client Javascript`包。

```bash
$ pip install gradio_client
```

### fn_index: 0

```python
from gradio_client import Client

client = Client("http://200.200.32.153:55082/")
result = client.predict(
		"vicuna-7b-v1.5-16k,vicuna-7b-v1.5-16k",	# str (Option from: [('vicuna-7b-v1.5-16k', 'vicuna-7b-v1.5-16k')]) in 'parameter_5' Dropdown component
		fn_index=0
)
print(result)
```

- Return Type(s)

```python
(
# str representing output in 'value_9' Textbox component,
# str representing output in 'value_13' Button component,
# str representing output in 'value_14' Button component,
# str representing output in 'value_15' Button component,
)
```

## cURL

```bash
api=http://L40.sinotech-eng.com:55083/v1
curl $api/chat/completions   -H "Content-Type: application/json"   -d '{
    "model": "vicuna-7b-v1.5-16k",
    "messages": [{"role": "user", "content": "Hello! What is your name?"}]
  }'
## ans  
{"id":"chatcmpl-utvSw5XEAgmGAUR73kLwRg","object":"chat.completion","created":1713405660,"model":"vicuna-7b-v1.5-16k","choices":[{"index":0,"message":{"role":"assistant","content":"Hello! My name is Vicuna."},"finish_reason":"stop"}],"usage":{"prompt_tokens":45,"total_tokens":53,"completion_tokens":8}}

## again
curl $api/chat/completions   -H "Content-Type: application/json"   -d '{
    "model": "vicuna-7b-v1.5-16k",
    "messages": [{"role": "user", "content": "Hello! What is your name?"}]
  }'
## ans

{"id":"chatcmpl-fjkmAKmuGXnHdSa52otNrP","object":"chat.completion","created":1713405669,"model":"vicuna-7b-v1.5-16k","choices":[{"index":0,"message":{"role":"assistant","content":"Hello! My name is Vicuna, and I'm a language model developed by Large Model Systems Organization (LMSYS)."},"finish_reason":"stop"}],"usage":{"prompt_tokens":45,"total_tokens":73,"completion_tokens":28}}
```

