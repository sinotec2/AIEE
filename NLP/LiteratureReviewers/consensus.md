---
layout: default
title: consensus
parent: Literature Reviewers
grand_parent: 自然語言處理
nav_order: 99
date: 2026-05-21
last_modified_date: 2026-05-21T11:58:34
tags:
---

# consensus
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

![](./pngs/Pasted%20image%2020260521175604.png)
## 背景

Consensus AI 是一個學術研究的 AI 搜尋引擎[bentley](https://www.bentley.edu/library/in-the-know/what-is-consensus-ai)、[marshallgjones](https://marshallgjones.substack.com/p/an-ai-tool-for-reviewing-research)。它旨在加速研究過程，幫助使用者更快地找到重要的資訊([effortlessacademic](https://effortlessacademic.com/consensus-ai-review-for-literature-reviews/))。

**發展歷史與背景：**

- Consensus AI 由 Eric Olson 和 Christian Salem 創立，他們在消費者技術領域有豐富的背景。
- 該公司於 2022 年 9 月成立([.ipl.org](https://www.ipl.org/consensus-ai-a-search-engine-built-for-science-and-research/))。

**環境領域的應用：**

目前沒有明確資訊顯示 Consensus AI 在環境領域的應用。搜尋結果中提及了 AI 對環境的影響，例如產生大量能源和水，以及 AI 訓練和資料中心對環境的影響。

**如何使用 Consensus AI 工具來做學術論文研究：**

- **搜尋文獻**：Consensus AI 是一個專注於學術研究內容的搜尋工具。它能搜尋超過 **2 億**篇科學研究論文。[oregonstate](https://guides.library.oregonstate.edu/consensus)
- **證據合成**：它使用 AI 來合成研究結果的證據型摘要([virginia](https://guides.lib.virginia.edu/consensus))。
- **快速理解研究**：Consensus AI 旨在幫助使用者快速理解特定主題的**同儕評審**研究的內容。
- **尋找、組織和分析科學**：Consensus 是一個 AI 學術搜尋引擎，用於更快地尋找、組織和分析科學。
	
- [官網](https://www.consensus.app/)
- 免費15次搜尋


## 搜尋策略及結果

### 策略

- 組合成更容易搜尋的同意子句
- 按照關鍵字的"聯集"
- 不同子句的交集前20筆


### 結果

![](./pngs/Pasted%20image%2020260521165824.png)

## 分析
![](./pngs/Pasted%20image%2020260521170312.png)


### 參考

![](./pngs/Pasted%20image%2020260521171655.png)

### 串聯**Zotero**

- 檔案 → 匯入 → 檔案(...RIS...) → 開啟

![](./pngs/Pasted%20image%2020260521173443.png)

![](./pngs/Pasted%20image%2020260521173557.png)

- 選取`ctrl-shift-C`
- 貼上 `ctrl-V` 

- Soh, P.-W., Chang, J.-W., Huang, J.-W. (2018). Adaptive Deep Learning-Based Air Quality Prediction Model Using the Most Relevant Spatial-Temporal Relations. IEEE Access 6, 38186–38199. [doi]([https://doi.org/10.1109/access.2018.2849820](https://doi.org/10.1109/access.2018.2849820))
## 價格

- 如果有2個以上同仁愛讀書的，以團隊企業方案就會划算

| ![](./pngs/Pasted%20image%2020260521165249.png) |
| :-------------------------------------------: |
|                     個人方案                      |
| ![](./pngs/Pasted%20image%2020260521171328.png) |
|                    企業共用席位                     |
| ![](./pngs/Pasted%20image%2020260521181903.png) |
|                     API費用                     |



## 深度學習在台灣空氣品質預測的應用：**關鍵模型與研究結果**

台灣近期的研究迅速採用深度學習來改善**PM2.5 和其他污染物**的預測，從而能夠更早發佈公共衛生預警並做出更好的政策決策。

### **主要深度學習架構和目標**

- **LSTM / RNN 系列**
    
    - 利用深度多輸出LSTM模型對台北地區PM2.5/PM10/NOx進行多步驟預測（至t+4），與淺層LSTM模型相比，提高了穩定性和準確率。 (Zhou et al., 2019).
    - 利用RNN/LSTM演算法結合來自77個空氣站和580個氣象站的氣象數據，對全國範圍內的PM2.5進行預測，其R²值比梯度提升、SVM和CART演算法分別提高了約27%和34%的RMSE值。 (Lin et al., 2020).
    - 針對高污染區域優化的LSTM模型，實現了1-24小時均方根誤差(RMSE)為6.3-13.1 μg/m³，並能提供長達9小時的有效預測。 (Tran et al., 2023).
    - 使用 LSTM 和全連接層進行 12 小時空氣品質指數（不僅限於 PM2.5）預測，並已部署在台灣官方監測網路和應用程式中。(Wang et al., 2023).

- **CNN / Hybrid 深度模型**
    
    - CNN-BP 和 MCNN-BP 混合模型用於台灣全境多站點、多時域 PM2.5 監測（長達 72 小時），其性能明顯優於隨機森林、LSTM 和純 ACT 化學傳輸模型，同時縮短了計算時間。 (Kow et al., 2022; Kow et al., 2020).
    - 將卷積神經網路（CNN）與WRF-CMAQ業務預報結合，可將72小時均方根誤差（RMSE）從10.48 μg/m³降低至6.88 μg/m³，並能更好地捕捉高污染事件。(Lee et al., 2024).
    - AE-CNN-BP混合模型用於高雄工業區4小時前高時空PM2.5監測（數百個微型感測器），R²≈0.76–0.82 (Wu et al., 2023).


### 代表模型與預報時距

|Model type|Region / pollutant|Horizon|Citations|
|---|---|---|---|
|DM‑LSTM|Taipei; PM2.5/PM10/NOx|t+1–t+4|(Zhou et al., 2019)|
|MCNN‑BP|Taiwan; PM2.5|up to 72 h|(Kow et al., 2022)|
|CNN‑BP|Taiwan; PM2.5|t+1–t+10|(Kow et al., 2020)|
|RNN/LSTM (dynamic)|Taiwan; PM2.5|24 h (hourly)|(Lin et al., 2020)|
|LSTM‑AQI model|Taiwan; AQI (next 12 h)|12 h|(Wang et al., 2023)|
|AE‑CNN‑BP|Kaohsiung; PM2.5|4 h (dense grid)|(Wu et al., 2023)|

**Figure 1:** 主要深度模型與預報範圍一覽

### **台灣地區的特殊創新****

- **多源資料整合**：結合地面站、氣象站、化學傳輸模式輸出、衛星 AOD、鄰近及前哨站，提升長時距與跨區域預報能力 (Kow et al., 2022; Tran et al., 2023; Kibirige et al., 2021; Wang et al., 2023; Wu et al., 2023).
- **長程輸送與地形效應**：利用衛星偵測遠程傳輸事件 (RTPEs) 的深度網路，+4–72 h 預報誤差改善 10–30% (Kibirige et al., 2021)；部分模型顯式考慮地形與區域差異 (Soh et al., 2018; Lee et al., 2020; Lin et al., 2020).
- **季節性與特定污染物**：SGRU 模型針對 NO₂、SO₂、CO 等季節性序列，MAPE 可低至 0.44–1.2，優於 ARIMA、SARIMA、SVR、季節 LSTM (Zhang & Zhang, 2023; Yang et al., 2024).
- **實務應用**：官方 AQI LSTM 模型已整合進台灣空品監測網與環境資訊推播 App，提供民眾 12 小時活動建議 (Wang et al., 2023).

###  **性能與傳統方法***

跨研究，深度學習模型（LSTM、CNN 混合、GRU/SGRU）始終優於 ARIMA/SARIMA、SVM、隨機森林和單一化學傳輸模式，在 RMSE、MAE、R² 上明顯改善，特別是在多站、多時距與高污染事件預警方面(Kow et al., 2022; Zhou et al., 2019; Kow et al., 2020; Zhang & Zhang, 2023; Lee et al., 2024; Yang et al., 2024; Lin et al., 2020; Tran et al., 2023; Wu et al., 2023).

### **結語**

對台灣而言，深度學習已成為空氣品質預測的核心工具，其應用範圍涵蓋全國PM2.5和空氣品質指數（AQI）到局部工業熱點區域和特定氣體。結合豐富的氣象和衛星資料輸入的混合CNN/LSTM框架能夠提供精準的多小時至多天預測，並已投入實際應用

_These search results were found and analyzed using Consensus, an AI-powered search engine for research. Try it at [https://www.consensus.app](https://www.consensus.app/). © 2026 Consensus NLP, Inc. Personal, non-commercial use only; redistribution requires copyright holders’ consent._

### References

Kibirige, G., Yang, M., Liu, C., & Chen, M. (2021). Using satellite data on remote transportation of air pollutants for PM2.5 prediction in northern Taiwan. _PLOS ONE, 18_. [https://doi.org/10.36227/techrxiv.13734067.v1](https://doi.org/10.36227/techrxiv.13734067.v1)

Kow, P., Chang, L., Lin, C., Chou, C., & Chang, F. (2022). Deep neural networks for spatiotemporal PM2.5 forecasts based on atmospheric chemical transport model output and monitoring data.. _Environmental pollution_, 119348. [https://doi.org/10.1016/j.envpol.2022.119348](https://doi.org/10.1016/j.envpol.2022.119348)

Kow, P., Wang, Y., Zhou, Y., Kao, I., Issermann, M., Chang, L., & Chang, F. (2020). Seamless integration of convolutional and back-propagation neural networks for regional multi-step-ahead PM2.5 forecasting. _Journal of Cleaner Production_. [https://doi.org/10.1016/j.jclepro.2020.121285](https://doi.org/10.1016/j.jclepro.2020.121285)

Lee, Y., Cheng, F., Chien, H., Lin, Y., & Sun, M. (2024). Enhancing real-time PM2.5 forecasts: a hybrid approach of WRF-CMAQ model and CNN algorithm. _Atmospheric Environment_. [https://doi.org/10.1016/j.atmosenv.2024.120835](https://doi.org/10.1016/j.atmosenv.2024.120835)

Lee, M., Lin, L., Chen, C., Tsao, Y., Yao, T., Fei, M., & Fang, S. (2020). Forecasting Air Quality in Taiwan by Using Machine Learning. _Scientific Reports, 10_. [https://doi.org/10.1038/s41598-020-61151-7](https://doi.org/10.1038/s41598-020-61151-7)

Lin, L., Chen, C., Yang, H., Xu, Z., & Fang, S. (2020). Dynamic System Approach for Improved PM2.5 Prediction in Taiwan. _IEEE Access, 8_, 210910-210921. [https://doi.org/10.1109/access.2020.3038853](https://doi.org/10.1109/access.2020.3038853)

Soh, P., Chang, J., & Huang, J. (2018). Adaptive Deep Learning-Based Air Quality Prediction Model Using the Most Relevant Spatial-Temporal Relations. _IEEE Access, 6_, 38186-38199. [https://doi.org/10.1109/access.2018.2849820](https://doi.org/10.1109/access.2018.2849820)

Tran, H., Huang, H., Yu, J., & Wang, S. (2023). Forecasting hourly PM2.5 concentration with an optimized LSTM model. _Atmospheric Environment_. [https://doi.org/10.1016/j.atmosenv.2023.120161](https://doi.org/10.1016/j.atmosenv.2023.120161)

Wang, S., Huang, B., & Hu, M. (2023). A Deep Learning-based Air Quality Index Prediction Model Using LSTM and Reference Stations: A Real Application in Taiwan. _2023 33rd International Telecommunication Networks and Applications Conference_, 204-209. [https://doi.org/10.1109/itnac59571.2023.10368496](https://doi.org/10.1109/itnac59571.2023.10368496)

Wu, K., Hsia, I., Kow, P., Chang, L., & Chang, F. (2023). High-spatiotemporal-resolution PM2.5 forecasting by hybrid deep learning models with ensembled massive heterogeneous monitoring data. _Journal of Cleaner Production_. [https://doi.org/10.1016/j.jclepro.2023.139825](https://doi.org/10.1016/j.jclepro.2023.139825)

Yang, C., Chen, P., Wu, C., Yang, C., & Chuang, L. (2024). Deep learning-based air pollution analysis on carbon monoxide in Taiwan. _Ecol. Informatics, 80_, 102477. [https://doi.org/10.1016/j.ecoinf.2024.102477](https://doi.org/10.1016/j.ecoinf.2024.102477)

Zhang, Z., & Zhang, S. (2023). Modeling air quality PM2.5 forecasting using deep sparse attention-based transformer networks. _International Journal of Environmental Science and Technology, 20_, 13535-13550. [https://doi.org/10.1007/s13762-023-04900-1](https://doi.org/10.1007/s13762-023-04900-1)

Zhou, Y., Chang, F., Chang, L., Kao, I., & Wang, Y. (2019). Explore a deep learning multi-output neural network for regional multi-step-ahead air quality forecasts. _Journal of Cleaner Production_. [https://doi.org/10.1016/j.jclepro.2018.10.243](https://doi.org/10.1016/j.jclepro.2018.10.243)