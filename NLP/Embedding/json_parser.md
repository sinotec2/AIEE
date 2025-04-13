---
layout: default
title: 解析表格
parent:  文檔之內嵌
grand_parent: 自然語言處理
nav_order: 99
date: 2024-01-25
last_modified_date: 2024-01-25 09:35:43
tags: AI chat
---


# 解析表格
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

> “LLM 支援 JSON 格式查詢與理解”,這包括llama3嗎？

很棒的問題！

是的，LLaMA 3（尤其是 Meta 官方的 LLaMA 3 8B / 70B 模型），在設計上就已經對 JSON 結構具備一定的理解能力，雖然不像 GPT-4 Turbo 那樣專門針對 JSON 做強化，但它：
	•	可以 解析嵌套 JSON 資料。
	•	能夠理解 key-value 關係的語意，如 "條文": "..."。
	•	支援結構化 prompt，例如你問：「請根據下面 JSON 中的 ‘第2條’ 給我說明內容。」

⸻

LLaMA 3 處理 JSON 的能力特點如下：

能力	支援程度	備註
基本 JSON 結構理解	支援良好	可當作資料格式或查詢知識
嵌套 JSON 查詢	支援中等	需要你設計明確 prompt
自動生成 JSON 回應	支援良好	可控制格式與 key 名稱
JSON 與自然語言的來回轉換	中等偏好	有時需微調提示詞以避免混亂



⸻

如何善用 LLaMA 3 處理 JSON 查詢？

範例 1：查詢嵌入的條文資料

[
  {
    "條號": "第1條",
    "內容": "本辦法依據 XX 條規定訂定之",
    "備註": "法規依據"
  },
  {
    "條號": "第2條",
    "內容": "用人單位應每月通報人員異動情形",
    "備註": "含試用期人員"
  }
]

你可以這樣問：

請找出上述 JSON 中第2條的內容，以及它的備註說明。

或設計更正式的提示：

你是一位了解政策規定的 AI。請依據下方 JSON，回答第2條的主要內容是什麼？若有備註，請一併說明。



⸻

實務建議（如果你用的是 LlamaIndex + LLaMA 3）
	1.	將表格轉為一筆筆 JSON 丟入 chunk 中
	•	每個 chunk 約可塞 1~3 條規則（依 token 數）
	•	也可以使用 metadata 欄位存「條號」等索引資訊
	2.	查詢時使用自然語言與條號、關鍵詞查詢結合
	•	LLaMA 3 的 contextual matching 表現已經不錯，會根據嵌入內容與查詢語意給出精準內容
	3.	進一步結合 reranker 可強化效果
	•	若你在用如 ColBERT / Cohere Rerank 模型，可在初步檢索後做語意強化排序

⸻

如果你告訴我你目前用哪個版本的 LLaMA 3（如 8B 還是 70B，有沒有經過 finetune），以及你是用在本地 Ollama、Together.ai、或其他推理服務，我可以給你更精準的調整建議。你是怎麼部署 LLaMA 3 的呢？