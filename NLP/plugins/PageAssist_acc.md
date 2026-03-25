---
title: 加速Page Assist的效能
icon: user-cog
star: true
sticky: 10
nav_order: 4
category:
  - 快速上手
  - 基礎知識
  - 教程
contributors: '[{"name": "kuang", "email": "sinotec2@gmail.com", "url":"","contributions":"","commits":""}]'
lastUpdated: 2025-10-10T17:00:00
grand_parent: 自然語言處理
parent: 瀏覽器AI插件
---

# 👩‍💼 加速Page Assist的秘訣 🌐


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

[Page Assist](./PageAssist)(頁面輔助的加速訣竅)：<br>
<br><br>
必要的理由：降低GPU負荷<br>
充分的理由：避免壅塞、盡早取得語言模型的結果

:::


## 按照工作特性選擇語言模型

- 單純的詢問 &rightarrow;
	- mistral http://eng06.sinotech-eng.com:55083
	- llama3.1 http://l40.sinotech-eng.com:55080 
- 複雜的推論 &rightarrow;
	- GPT oss http://l40.sinotech-eng.com:55083
- 即使測試狀況下：2種語言模型、在同一片GPU上，回答同一個問題，其記憶體(黃線)與GPU使用率(藍線)的時間序列如下圖所示、就速度和占用資源來說，有很大的差異。


![](PA_pngs/Pasted%20image%2020251010185337.png)

## 清除站存記憶體

- PA內設的"保留時間"是5分鐘
	- 意思是：請求後模型在記憶體中保持的時間（預設：5分鐘）
	- 縮短這個時間(如3s)，會讓記憶體保持在最乾淨的狀態，這樣可以服務更多人，避免當機。
- 在`設定`&rightarrow; `Ollama設定`&rightarrow; `模型設定`&rightarrow; `保留時間`

![](PA_pngs/Pasted%20image%2020251010190431.png)


## 避免讀取歷史紀錄

- 聊天紀錄儲存在使用者的本機電腦中，其中有不少的資訊，歡迎隨時回訪、搜尋、剪貼。
- 但是如果使用者要"繼續聊"，就要考慮一下了，因為程式會上載所有過往的歷史對話做為背景，會占用流量、記憶體跟GPU計算的時間。
- 如果只是需要簡答題的答案，不會重複取用，可以用`臨時聊天`，不會記錄。
- 隨時開始新聊天，也是降低GPU負荷的好方法。
- 如果發現硬碟吃得太兇了，可以清除不會再查詢的過往紀錄，

![](PA_pngs/Pasted%20image%2020251010190828.png)