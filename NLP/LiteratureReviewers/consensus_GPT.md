---
layout: default
title: consensus_GPT
parent: Literature Reviewers
grand_parent: 自然語言處理
nav_order: 99
date: 2026-02-02
last_modified_date: 2026-02-02T11:58:34
tags:
---
# consensus at OpenAI GPTs
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

## Start-up

- GPT-plus
- 登入openai介面→更多→GPT→(搜尋或下拉點選)

![](pngs/Pasted%20image%2020260521162659.png)

![](pngs/Pasted%20image%2020260521162937.png)

### 功能

![](pngs/Pasted%20image%2020260521163127.png)

## Profomance

> 請搜尋：台灣空氣品質預報的深度學習研究

台灣空氣品質預報的深度學習研究，核心是用**測站歷史污染物資料 + 氣象資料 + 空間鄰近測站資訊**來預測 PM2.5、AQI、O₃、CO 等指標。

### **Evidence**

- 台灣相關研究常用 **LSTM** 處理時間序列；Chang 等人提出 Aggregated LSTM，把本地測站、附近工業區測站與外部污染來源測站整合，用於空氣污染預報 [(Chang et al., 2020)](https://ntut.elsevierpure.com/en/publications/an-lstm-based-aggregated-model-for-air-pollution-forecasting/)；該研究頁面也標示主題包含 Taiwan、PM2.5、LSTM。([National Taipei University of Technology](https://ntut.elsevierpure.com/en/publications/an-lstm-based-aggregated-model-for-air-pollution-forecasting/?utm_source=chatgpt.com "An LSTM-based aggregated model for air pollution forecasting"))

![](pngs/Pasted%20image%2020260521163300.png)


- **CNN-LSTM** 適合台灣 PM2.5 預測，因為 CNN 可抽取特徵、LSTM 可捕捉時間變化；Huang 與 Kuo 的 APNet 結合累積降雨、風速與 PM2.5 歷史資料，表現優於多個傳統機器學習方法 [(Huang & Kuo, 2018)](https://www.mdpi.com/1424-8220/18/7/2220)。 ([MDPI](https://www.mdpi.com/1424-8220/18/7/2220?utm_source=chatgpt.com "A Deep CNN-LSTM Model for Particulate Matter (PM2.5) ...")) ([researchgate](https://www.researchgate.net/publication/326312442_A_Deep_CNN-LSTM_Model_for_Particulate_Matter_PM25_Forecasting_in_Smart_Cities))

![](pngs/Pasted%20image%2020260521164303.png)
- 對台灣多測站情境，研究也開始重視**時空模型**，例如 CRNN 用於台灣 PM2.5 感測節點資料，產生污染擴散預測圖，能同時考慮測站間的空間與時間關係 [(Chen et al., 2021)](https://arxiv.org/abs/2101.06213)。 ([arXiv](https://arxiv.org/abs/2101.06213?utm_source=chatgpt.com "A Novel Prediction Approach for Exploring PM2.5 Spatiotemporal Propagation Based on Convolutional Recursive Neural Networks"))
    ![](pngs/Pasted%20image%2020260521164505.png)

- 最新綜述指出，PM2.5 深度學習預測仍以 LSTM、CNN-LSTM、混合模型為主，但未來趨勢是加入注意力機制、Transformer、多源資料與更標準化的評估架構 [(Zhou et al., 2024)](https://www.sciencedirect.com/science/article/pii/S2666498424000140)。 ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2666498424000140?utm_source=chatgpt.com "Deep-learning architecture for PM2.5 concentration ..."))
    
![](pngs/Pasted%20image%2020260521164411.png)
### **建議研究架構**

資料：環境部測站 PM2.5、PM10、O₃、NO₂、SO₂、CO、AQI，加上氣象局溫度、濕度、風速、風向、降雨、氣壓。  
模型：基準用 ARIMA、Random Forest、XGBoost；深度學習用 LSTM、GRU、CNN-LSTM；進階用 Graph Neural Network、Attention LSTM、Transformer。  
評估：MAE、RMSE、MAPE、R²，並分北中南東、季節、污染事件日比較。

### **結論**

台灣空氣品質預報最適合採用「LSTM/CNN-LSTM + 多測站空間資訊 + 氣象特徵」的深度學習架構，若要提升研究新穎性，可加入圖神經網路或 Transformer。

Like our GPT? Try our full AI-powered search engine and academic features for free at [consensus.app](https://consensus.app/?utm_source=chatgpt)