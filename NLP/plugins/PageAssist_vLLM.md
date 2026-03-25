---
title: Page Assist連接vLLM
icon: user-cog
star: true
sticky: 10
nav_order: 4
category:
  - 快速上手
  - 基礎知識
  - 教程
  - PageAssist
  - vLLM
contributors: '[{"name": "kuang", "email": "sinotec2@gmail.com", "url":"","contributions":"","commits":""}]'
lastUpdated: 2025-10-15T13:00:00
grand_parent: 自然語言處理
parent: 瀏覽器AI插件
---

# 👩‍💼 Page Assist連接vLLM 🌐


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

::: important

[Page Assist](./PageAssist.md)(連上強大的vLLM使用地端最強gpt-oss)：<br>
<br><br>
必要的理由：(不存在)<br>
充分的理由：地表最強的組合!

:::


## ⚙️Page Assist設定


### 🔗 進入API設定

- 原來的ollama設定不需要刪除，vLLM設定結果會出現在首頁的語言模型選擇處，以便讓使用者切換(3)。
- 進入設定(1)後，選擇`openAI相容API`(2)

![](pngs/Pasted%20image%2020251015134021.png)


### 🚀提供商
- 此處`新增提供商`(編按：一般的API是商業模型，所以稱為`提供商-provider`，後來即使開源系列雖然沒有商業模式，但也列為`提供商`，主要借用其品牌、智財權的概念)
![](pngs/Pasted%20image%2020251015134220.png)
- 先選`提供商`，因為有點多，要下拉一陣子才找得到vLLM。

![](pngs/Pasted%20image%2020251015134959.png)

### 📍Base URL

- 新增伺服器位置(`Base url`)：`http://l40.sinotech-eng.com:8001/v1`。同樣的`/v1`之後不要再加正斜線(`/`)了
- 點選CORS問題修正(`Fix CORS issues`)
- 按下`新增`、離開設定、回到主頁。
- 目前還沒有設訂金鑰，如果哪天規定了金鑰，就在此處填入。

![](pngs/Pasted%20image%2020251015135500.png)

### 💡問題解決

- 🔗測試連線失敗：call ⚕️ Dr. Kuang(04139)💊
- 如果首頁還沒有看到模型的選項，重新整理頁面、更新連線。😍
 

## ✔️vLLM的使用

### 🗣️模型選擇

- 在首頁下拉選單中，會出現ollama與vLLM的商標圖案，以及模型名稱
- 同樣的，可以視使用者的需求選擇不一樣的模型。


![](pngs/Pasted%20image%2020251015141334.png)
- ↓因為系統反應非常快速，請點選向下鍵(&downarrow;)到最後。

### 📈GPU performance

- 記憶體預設是全佔滿，將模型預先載入記憶體，提供使用者最佳的服務。
- vLLM不是FIFO架構設計，會進行LLM batching，彙整前後使用者的請求同時計算、輸出。
- 下圖為同時2個使用者IP、同時提出2個請求之短期GPU/記憶體運轉歷線。GPU沒有顯出樓梯狀的上下爬升下降，而是一次啟動就全力運轉(直到所有的請求都完成)。

![](pngs/Pasted%20image%2020251015142846.png)

### 🕰️整體長期表現

- 思考型的語言模型(如gpt-oss~gpt4o等級、下圖`(1)` 及`(3)`)、相較直覺型的llama3(下圖`(2)`)而言，本來GPU的使用率就比較高，分開2片GPU處理不同等級的需求，有其必要性。
- vLLM與ollama執行gpt-oss的差異，前者有batching機制，不必清空記憶體也不會攪混使用者的session info，後者則需要清空前一使用者佔用的記憶體，再重啟載入語言模型與使用者指令，線形出現明顯的峰谷形態，同時總體效能也較vLLM為低。

![](pngs/Pasted%20image%2020251015152908.png)


