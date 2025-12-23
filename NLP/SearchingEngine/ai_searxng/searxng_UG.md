---
layout: default
title: SearXNG使用手冊
parent: 地端智慧搜尋引擎
grand_parent: SearchingEngine
nav_order: 1
date: 2025-11-11
last_modified_date: 2025-11-11T13:08:00
tags:
  - AI
  - searching
  - searXNG
---

# SearXNG使用手冊

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




## 🔍 SearXNG 搜尋語法

_(原文出自 [SearXNG 官方文件](https://docs.searxng.org/user/search-syntax.html))_

---

### 🧭 什麼是搜尋語法？

==SearXNG== 是一個可以幫你搜尋網路上資料的「開放原始碼搜尋引擎」，類似 Google、DuckDuckGo，但更注重 **隱私** 🔒。  

「搜尋語法（Search Syntax）」指的是你在搜尋時可以加一些 **特殊符號或關鍵字**，讓搜尋結果更精確、更符合你想找的東西。

---

### 💬 一般搜尋

你可以直接輸入詞語來搜尋：

```
volcano eruption
```

👉 會搜尋包含「volcano（火山）」和「eruption（爆發）」的頁面。

每一個詞都會被獨立搜尋。如果你輸入很多詞，==SearXNG== 通常會找到 **同時包含那些詞** 的結果。

---

### 🕵️‍♀️ 使用引號 "" 搜尋特定片語

想要搜尋「連在一起的字詞」時，用引號：

```
"volcano eruption"
```

👉 只會找**完整句子中出現這兩個字一起（緊鄰）**的結果。  
這個功能就像是在 Google 裡用雙引號—非常實用 👍。

---

### 🚫 排除關鍵字（用減號 -）

如果你想要搜尋某樣東西，但排除掉一種結果，用減號（-）：

```
volcano -eruption
```

👉 會找有「volcano」但**沒有**「eruption」的頁面。

💡 小提醒：減號前 **要有空格**，例如： ✅ `volcano -eruption`  
❌ `volcano-eruption`（這樣會被當作一個字）

---

### 🔢 使用 OR（或）

若你想搜尋「這個 或 那個」：

```
volcano OR earthquake
```

👉 搜尋同時包含「volcano」**或**「earthquake」的頁面。

💡 `OR` 必須大寫（全大寫），否則會被當作一般字詞。

---

### 🔍 使用小括號 () 來組合條件

你可以把條件包在括號裡，讓搜尋邏輯更清楚：

```
(volcano OR earthquake) -news
```

👉 找到提到「火山」或「地震」的頁面，但排除掉有「news（新聞）」的內容。

---

### 📐 使用萬用字元 *（星號）

星號 `*` 可以代表任何字或片語：

```
"volcano * eruption"
```

👉 可以找到像「volcano gas eruption」、「volcano ash eruption」之類的結果。  
這在不確定中間會出現哪個字時很有用 🌋。

---

### 🧩 一些搜尋範例

|輸入|說明|
|---|---|
|`"black hole"`|找到剛好有「black hole（黑洞）」的結果|
|`black -hole`|包含「black」但不要出現「hole」|
|`cats OR dogs`|包含貓或狗的內容|
|`"global * change"`|匹配「global climate change」或「global economic change」等詞組|
|`(cat OR dog) food`|包含「貓食」或「狗食」的結果 🐱🐶🍖|

---

### 🧠 小結

學會搜尋語法 ≠ 變電腦高手 🤖，  
但能讓你在網路上找到更精準、更有用的資訊。

📘 高中小技巧回顧：

- `"引號"` → 搜尋整句詞
- `-關鍵字` → 排除
- `OR` → 兩者擇一
- `()` → 組合邏輯
- `*` → 任何字／空格

---

### 🧡 延伸閱讀

如果你想學更進階的用法（例如使用「!bangs」或特定引擎篩選），可以看 SearXNG 文件的下一頁：「[Search Filters](https://docs.searxng.org/user/filters.html)」。

## 搜尋結果

![](pngs/Pasted%20image%2020251111195445.png)

![](pngs/Pasted%20image%2020251111195519.png)

## 特定引擎

SearXNG 提供了一套搜尋語法，讓你可以修改搜尋的分類、引擎、語言等設定。請參閱偏好設定頁面以查看引擎、分類及語言的清單。

### ! 選擇引擎與分類  

若要設定分類及／或引擎名稱，請使用前綴符號「!」。以下是幾個範例：

在維基百科搜尋巴黎：

```
!wp paris

!wikipedia paris
```

在「地圖」分類中搜尋巴黎：

```
!map paris
```

圖片搜尋：

```
!images Wau Holland
```

搜尋引擎與語言的縮寫也能被接受。引擎／分類的修飾符可以串接且會被同時應用。  
例如：

```
!map !ddg !wp paris  
```
👉 會在「地圖」分類中搜尋，並同時使用 DuckDuckGo 和維基百科搜尋關於巴黎的結果。

### : 選擇語言  

若要設定語言過濾器，請使用前綴符號「:」。範例如下：

以自訂語言在維基百科搜尋：

```
:fr !wp Wau Holland
```

### !! 外部 Bang 指令  

SearXNG 支援來自 DuckDuckGo 的外部 Bang 指令。若要直接跳轉到外部搜尋頁面，請使用「!!」前綴。範例如下：

以自訂語言在維基百科搜尋：

```
!!wfr Wau Holland
```

請注意，此搜尋將直接在外部搜尋引擎上執行，因此 SearXNG **無法保護你的隱私**。

### !! 自動重新導向  

當在搜尋查詢中包含「!!」（以空格分隔）時，你會自動被重新導向至第一個搜尋結果。這個行為類似於 DuckDuckGo 的「好手氣（Feeling Lucky）」功能。範例如下：

搜尋一個查詢並自動跳轉到第一個結果：

```
!! Wau Holland
```

請記住，被重新導向的結果無法保證可信度，並且使用此功能時 SearXNG 無法保護你的個人隱私。請自行承擔風險使用此功能。

### 特殊查詢  

在偏好設定頁面中，你可以找到特殊查詢的關鍵字。以下是一些範例：

- 產生隨機 UUID：

```
random uuid
```

- 計算平均值：

```
avg 123 548 2.04 24.2
```

- 顯示你的瀏覽器使用者代理字串（需啟用功能）：

```
user-agent
```

- 將字串轉換為不同的雜湊摘要（需啟用功能）：

```
md5 lorem ipsum

sha512 lorem ipsum
```

### 🧡啟用AI摘要

- 在所有過濾器、關鍵字的最前面，以`ai`開頭

如

```
ai !swiki searxng
```


![](pngs/Pasted%20image%2020251111195052.png)