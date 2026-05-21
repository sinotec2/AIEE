---
layout: default
title: Scholar GPT
parent: Literature Reviewers
grand_parent: 自然語言處理
nav_order: 99
date: 2026-05-21
last_modified_date: 2026-05-21T11:58:34
tags:
---

# Scholar GPT
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

![](pngs/Pasted%20image%2020260521182435.png)


利用超過2億筆資源與內建的批判性閱讀能力來強化研究。輕鬆存取 Google Scholar、PubMed、bioRxiv、arXiv 等資料庫。

工具調用：sider_ai__jit_plugin.advancedScholarSearch

## 範例

> 請搜尋：台灣空氣品質預報的深度學習研究

台灣近年在「空氣品質預報（Air Quality Forecasting）」與「深度學習（Deep Learning）」的研究相當活躍，研究主題集中於 PM2.5、AQI、臭氧（O₃）以及多站點時空預測。主要方法包括 LSTM、CNN-LSTM、GRU、RNN、Autoencoder 與 GIS 空間模型等。研究單位則以臺大、成大、暨大、中研院相關合作團隊為主。

---

台灣近年在「空氣品質預報（Air Quality Forecasting）」與「深度學習（Deep Learning）」的研究相當活躍，研究主題集中於 PM2.5、AQI、臭氧（O₃）以及多站點時空預測。主要方法包括 LSTM、CNN-LSTM、GRU、RNN、Autoencoder 與 GIS 空間模型等。研究單位則以臺大、成大、暨大、中研院相關合作團隊為主。

---

# 台灣空氣品質預報深度學習研究概況

## 主要研究方向

### 1. PM2.5 短期預測

最常見的研究主題，通常預測未來 1–48 小時 PM2.5 濃度。

常見模型：

* LSTM（Long Short-Term Memory）
* GRU（Gated Recurrent Unit）
* CNN-LSTM 混合模型
* RNN
* Transformer（近年開始出現）

輸入資料：

* 環境部空品監測站資料
* 氣象資料（風速、濕度、溫度）
* 衛星資料
* 微型感測器資料

---

### 2. 時空空氣品質預測（Spatio-Temporal Forecasting）

結合：

* GIS
* 地理人工智慧（GeoAI）
* 深度神經網路

目標：

* 同時預測多測站
* 補足測站稀疏問題
* 建立區域性污染擴散模型

---

### 3. 工業區與高雄污染預測

高雄因重工業聚集，是重要研究案例：

* 石化污染
* VOCs
* PM2.5
* 臭氧

許多研究採：

* 多站點深度學習
* 大數據模型
* 工業排放 + 氣象整合

---

# 代表性研究（台灣）

以下整理較具代表性的研究與論文。

---

## 1. 蘇評威（2018）

### 《運用最相關的時空間關係之可適性深度學習空氣品質預測模型》

* 學校：成功大學
* 方法：

  * CNN
  * 多神經網路融合
  * 時空關聯分析
* 預測：

  * 最長 48 小時 AQI/PM2.5

特色：

* 使用台灣環保署監測站資料
* 強調「測站間關聯性」

連結：
[https://nckur.lib.ncku.edu.tw/handle/987654321/258497](https://nckur.lib.ncku.edu.tw/handle/987654321/258497)

---

## 2. 莊宜庭（2019）

### 《基於遞迴神經網路之深度學習建立 PM2.5 預測模型》

方法：

* RNN
* LSTM

特色：

* 台灣 PM2.5 時序預測
* 比較傳統統計法與深度學習差異

---

## 3. 林子琦（2019）

### 《短期空氣品質應變措施於多種天氣型態之有效性分析與效益評估》

* 臺灣大學
* 使用 LSTM 分析北部空品區

重點：

* 深度學習與氣象型態結合
* 探討政策與空污關係

連結：
[https://www.airitilibrary.com/Article/Detail/U0001-0608201922042200](https://www.airitilibrary.com/Article/Detail/U0001-0608201922042200)

---

## 4. 黃宇丞（2021）

### 《應用機器學習方法預測 PM2.5—以大台北地區為例》

比較：

* 線性回歸
* 機器學習
* 深度學習（LSTM）

結果：

* 深度學習優於傳統統計模型

連結：
[https://www.airitilibrary.com/Article/Detail/U0001-1402202218532400](https://www.airitilibrary.com/Article/Detail/U0001-1402202218532400)

---

## 5. 吳冠諺（2021）

### 《建立大數據深度學習模式以推估區域性多時刻空氣品質—以高雄市為案例》

方法：

* AE（Autoencoder）
* CNN
* LSTM
* GRU

特色：

* 高雄工業區案例
* 多時間尺度預測

PDF：
[https://tdr.lib.ntu.edu.tw/bitstream/123456789/79750/1/U0001-1808202115134400.pdf](https://tdr.lib.ntu.edu.tw/bitstream/123456789/79750/1/U0001-1808202115134400.pdf)

---

## 6. 盧慧鴻（2018）

### 《以 LSTM 預測細懸浮微粒值規畫最佳行徑路線》

特色：

* 行動裝置應用
* 即時 PM2.5 預測

結合：

* 路徑規劃
* 空污避讓

連結：
[https://www.airitilibrary.com/Article/Detail/U0020-1608201814284100](https://www.airitilibrary.com/Article/Detail/U0020-1608201814284100)

---

## 7. 林祐如（2024）

### 《基於地理人工智慧方法與微型感測器數據進行 PM2.5 濃度未來數小時時空預測》

* 成功大學

方法：

* GeoAI
* LSTM
* 微型感測器

特色：

* 台中市案例
* 多站點空間預測

連結：
[https://nckur.lib.ncku.edu.tw/handle/987654321/313409](https://nckur.lib.ncku.edu.tw/handle/987654321/313409)

---

## 8. 邱普運等（2024）

### 《深度學習：環境資料數位化的應用》

內容：

* AI/DL 在台灣環境預報應用
* 比較：

  * LSTM
  * GRU
  * Transformer

PDF：[https://www.ncir.niar.org.tw/Files/Doc/Publication/InstTdy/241/02410153.pdf](https://www.ncir.niar.org.tw/Files/Doc/Publication/InstTdy/241/02410153.pdf)

---

# 台灣研究的技術趨勢

## 早期（2017–2020）

主流：

* ANN
* RNN
* LSTM

特徵：

* 單測站
* 時序預測

---

## 中期（2020–2023）

主流：

* CNN-LSTM
* GRU
* Autoencoder

特徵：

* 多測站
* 加入氣象資料
* 高雄工業區研究增加

---

## 最新（2024–2026）

新方向：

* GeoAI
* Transformer
* Graph Neural Network（GNN）
* 多模態資料融合

特徵：

* 微型感測器
* 衛星影像
* 即時預警
* Edge AI

---

# 台灣研究常用資料來源

## 環境部（原環保署）空品監測資料

AQX：[https://airtw.moenv.gov.tw/](https://airtw.moenv.gov.tw/)

開放資料：[https://data.moenv.gov.tw/](https://data.moenv.gov.tw/)

---

## 中央氣象署資料

氣象變數：

* 溫度
* 濕度
* 風速
* 降雨

---

## 微型感測器平台

例如：

* AirBox
* LASS

常用於：

* 高密度空污監測
* Deep Learning 時空分析

---

# 目前研究挑戰

## 1. 台灣地形複雜

* 山脈
* 海陸風
* 都市峽谷效應

使預測困難。

---

## 2. 測站數量有限

因此近年大量研究：

* 空間插值
* GNN
* GeoAI

---

## 3. 極端污染事件

例如：

* 境外沙塵
* 中國污染傳輸
* 冬季逆溫

深度模型仍不易預測。

---

# 建議閱讀順序（入門 → 進階）

## 入門

1. 黃宇丞（2021）
2. 莊宜庭（2019）

---

## 中階

3. 林子琦（2019）
4. 吳冠諺（2021）

---

## 進階

5. 蘇評威（2018）
6. 林祐如（2024）
7. 邱普運等（2024）

---

# 延伸研究方向（值得做）

若你想做研究，台灣目前熱門方向包括：

* Transformer 空污預測
* GNN 空氣品質模型
* 衛星 + 地面站融合
* Explainable AI（XAI）
* 極端事件預警
* Edge AI 即時空污預測
* 空污與健康風險整合

---

# 參考文獻（整理）

1. 蘇評威（2018）。《運用最相關的時空間關係之可適性深度學習空氣品質預測模型》。成功大學。
2. 黃宇丞（2021）。《應用機器學習方法預測 PM2.5—以大台北地區為例》。臺灣大學。
3. 林子琦（2019）。《短期空氣品質應變措施於多種天氣型態之有效性分析》。臺灣大學。
4. 吳冠諺（2021）。《建立大數據深度學習模式以推估區域性多時刻空氣品質》。臺灣大學。
5. 林祐如（2024）。《基於地理人工智慧方法與微型感測器數據進行 PM2.5 時空預測》。成功大學。
6. 盧慧鴻（2018）。《以 LSTM 預測細懸浮微粒值規畫最佳行徑路線》。暨南國際大學。
7. 邱普運等（2024）。《深度學習：環境資料數位化的應用》。科儀新知。
8. 莊宜庭（2019）。《基於遞迴神經網路之深度學習建立 PM2.5 預測模型》。

---

**You've experienced ScholarGPT — now meet what's next.**
*Scholar Deep Research Agent* elevates your research game with:
🔍 350M+ trusted papers from top academic publishers, updated hourly.
🧠 Advanced multiple AI models dig through millions of sources for pinpoint insights, fast.
📝 Auto-generated highlights, smart notes, and visual reports
📁 All saved directly to your AI-powered knowledge base
ScholarGPT helped you search. Now, transform how you think.
[Explore Scholar Deep Research](https://bit.ly/43rXgSx)
