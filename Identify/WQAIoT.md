---
layout: default
title: 水質微型監測器的發展與應用
parent: 型態與辨識
grand_parent: utilities
nav_order: 99
date: 2023-08-09
last_modified_date: 2023-08-18 15:55:45
tags: AI AIoT
---

# 水質微型監測器的發展與應用

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

- 廉價、連續式、常效型水質監測微型感測器，相較於空氣盒子來說，是困難許多。不單面對河川、海域變化無常的水位、潮流、洪水，即使正常情況下還存在著薄膜積垢、破損等等問題，政府這5年來編列有關水質微型監測器的研究經費超過30億，委託工研院的研發經費也超過3億，仍然持續在發展中，並未有顯著技術轉移、也還沒有達到量產的目標。
- 這個情況可能是將研發的目標訂成取代傳統的標準水質檢測，而忘了水質項目設立的目標，是在保護水中生物、用水標的本身。
- 相對的在水產養殖的領域，並不因為沒有適合的微型監測器就停止發展它們的人工智慧，反倒以直接拍攝水面魚產的活動進行行為的辨識，來反推水質。並經由環境中的溫度等等因素進行預報。或許這個途徑值得我們參考。

## 水質微型監測器的發展

### 政府發展計畫

- 研究計畫
  - 環保署 (2020)，水質感測物聯網精進及數據分析應用計畫。
  - 環保署 (2020)，發展及推廣水質感測器執法應用服務試驗計畫。
  - 環保署 (2021)，高效化智慧水聯網應用設置計畫。
  - 環保署水科技物聯網應用平台([限會員帳密登入](https://wiot.epa.gov.tw))

- 彭書憶、楊博傑、陳范倫、朱振華、王榮豪 (2019)，「水質物聯網於工業與民間應用發展」，([工業技術研究院 IEK 產業情報網](https://ieknet.iek.org.tw/))
- 彭書憶、陳范倫、米姿蓉(2021)水質感測物聯網現地規劃與環境執法應用([工業污染防治　第 153 期 (Nov. 2021)](https://proj.ftis.org.tw/eta/WebPhotos/2021/153-07-水質感測物聯網現地規劃與環境執法應用.pdf))
- 王榮豪、李思儒、朱振華、王儀婷、黃至聖(2021)感測材料與微型化感測器開發應用於環境水質感測。[《工業材料雜誌》413期](https://www.materialsnet.com.tw/DocView.aspx?id=46945)

- 科技部(2021)民生公共物聯網數據應用及產業開展計畫(核定本)。政府科技發展中程個案計畫書[審議編號：110-1901-09-20-02](https://ws.www.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMjk1L3JlbGZpbGUvNzcyMy8yODk3NzAvNmQxOTdkMzQtMDE4OS00M2M3LTgxY2YtMmIyNmJiZGU2NDEyLnBkZg%3D%3D&n=5bu65qeL5rCR55Sf5YWs5YWx54mp6IGv57ay6KiI55Wr57Ch5LuLLnBkZg%3D%3D&ico%20=.pdf)
  - 科技部111民生公共物聯網數據應用及產業開展計畫  
> - O1優化環境品質感測物聯網體系，連結在地
> O1KR1 全國最適化規模精進7,000 點空品感測聯網應用、高效化 **120 點智慧水質感測物聯網**設置、發展 16 個寧靜區聲音辨識物聯網體系、建構 8 個環境電磁波監測物聯網體系。行政院環境保護署：O2 發展新世代水質感測物聯網，提升環境檢測技術及維護飲用水安全及品質
> O1KR2 發展環境治理智慧應用最佳服務、運用物聯網感測數據查察 27 件重大污染事件、深化在地環境資訊運用之民眾服務
> O1KR3 發展自動化環境污染管理系統、應用 **200 組移動感測聯網**發展都市污染管制服務
> - O2推動環境物聯網**國產化能量**
> O2KR1 研發「複合長效空品及水質物聯網感測器」，國內外專利申請 12 件。技轉與技術服務廠商環境感測器關鍵技術 13 案，協助廠商導入環境物聯網應用領域，加速產品化
> O2KR2 發展都市空氣品質 3D監測及模擬平台，精進重大空污事件之預報及成因診斷
> O2KR3 建置感測元件模組及服務平台並進行國產化研發試製，建立智慧微塵感測器產業鏈，並落實 1-3 個團隊於終端場域完成整合測試
> - 高效益智慧水質物聯網應用設置
> 開發光學式抗生物膜干擾之水質物聯監測系統雛型
> 水質物聯網感測模組定期監測水質變化，但受到生物膜增生附著、偵測環境惡劣，量測系統的不穏定，需要耗費大量資源與人力維護。本計畫開發長效耐用之水質物聯監測系統，創新解決生物膜干擾之長效技術，以及開發高效率多重檢測技術，可減少系統功耗以及提升耐久性，減少人力維運。
> 現行水質監測模組因監測環境複雜，導致監測元件失準與故障率高，需頻繁進行維運，使整體監測系統成本居高不下。本計畫參考國內主要水質監測物聯網系統佈建單位與環保公民團體所提出的水質監測系統布建需求，開發長效型水質監測感測系統，具備體積小、低耗電量、分析迅速及易與物聯網架接等優勢，適用大量布建，可輔助環保單位與減少維運成本，提升監測效益，提供民眾即時資訊。
> 優化第一代光學式COD/SS/ 銅重金屬水質物聯監測系統。

- 長效型水質感測技術[ITRI > 產業服務 > 技術移轉](https://www.itri.org.tw/ListStyle.aspx?DisplayStyle=13_content&SiteID=1&MmmID=1036233405427625204&Trt_idx=6609)
> 利用多波長光譜感測技術，整合多種環境水質感測器，如: 化學需氧量(COD)、固體懸物(SS)等，可即時於模組內進行多重水質參數融合演算，提升準確度。並利用光機與水體採樣流道分離設計，便於維護人員於現場施工維護，降低整體系統維運成本。

- 複合式監測 守護民眾健康[經濟日報 > 產業 > 科技產業2023/07/02](https://money.udn.com/money/story/11162/7271969)

> 經濟部技術處委託工研院團隊研發「複合式水質感測系統」，以**多通道光譜檢測技術**，可同時檢測化學需氧量（COD）、水中固體懸浮物（SS），重金屬銅離子（Cu2+）濃度、導電度、酸鹼值、溫度等。並以光學抑菌方法，抑制水中菌種增生速度，避免影響感測器準確度，延長感測器壽命，同時搭配水體取樣設計、最佳化電源管理技術，減少人工維護頻率，達到長效運作效益，
> 除例行性工業與民生用水監測，亦可建置在無法供電的水源區、河道、溝渠等，擴大監測覆蓋範圍，搭配物聯網技術動態掌握水質資訊，守護民眾用水安全。

### 自製DO微感器

陳仁和 (2012). 延伸式閘極場效電晶體溶氧微感測器之研究. 指導教授:黃義佑，電機工程學系研究所. 國立中山大學, 高雄市.([url](https://hdl.handle.net/11296/f66k49))
> 主要製程步驟包含四次黃光微影及四次薄膜沉積製程，研究中將探討分析電晶體通道寬長比、源/汲極幾何圖形與聚苯乙烯溶氧感測層對溶氧微感測器之特性影響。
> 本論文所開發之延伸式閘極場效電晶體溶氧微感測器晶片尺寸為11 mm×13 mm×0.5 mm，感測區域之面積為1 mm×1 mm。根據量測結果顯示，於2 ~ 6 ppm溶氧濃度量測範圍下，最佳化溶氧微感測器之感測靈敏度與線性度分別高達35.36 mV/ppm與98.83 %，感測響應時間僅為180~200 sec，故適合發展為即時監控之溶氧感測微系統。

- 侯文祥、游政勳，2005，低造價溶氧感測器之研發，[農業工程學報，51(4): 40~53](http://ntur.lib.ntu.edu.tw/bitstream/246246/176432/1/09.pdf)。
- 侯文祥、鄭雅元、陳以容(2008)低造價溶氧感測儀之試作研究(2)，[農業工程學報第54卷第3期](http://www.twaes.org.tw/ae/htmdata/05403014.pdf)。
- 薄膜溶氧計/DO485，[銘祥科技實業股份有限公司](https://www.jnc-tec.com.tw/main/productDetail.aspx?PID=p0000085&CID=c0000004)

## predictive DO Sensors

### Liu et al.(2021)

- Liu, H., Yang, R., Duan, Z., Wu, H. (2021). **A Hybrid Neural Network Model for Marine Dissolved Oxygen Concentrations Time-Series Forecasting Based on Multi-Factor Analysis and a Multi-Model Ensemble.** Engineering 7, 1751–1765. [doi](https://doi.org/10.1016/j.eng.2020.10.023)

> Compared with statistics-based models, AI-component models have much better forecasting performance. 

Table 1. A summary of the reviewed state-of-the-art data-driven DO forecasting methods.

Category-Statistics-based models

Research content	|Reference	|Year of publication|Contribution
-|-|-|-
ARIMA model|[10]|2010|The ARIMA method was applied to study stationary and nonstationary time series
Grey model|[11]|2018|The grey model was proposed to forecast the trend term of DO
Bayesian model|[12]|2018|A bayesian evidence framework was applied to obtain optimal parameter values
-|[13]|2017|The performance of the new bayesian regression model and the new autoregressive modified fuzzy linear regression method in DO prediction were compared
MLR model|[14]|2013|The MLR model was used to characterize and propagate the uncertainty of DO changes
-|[15]|2016|The MLR model was utilized to evaluate the performance of multiple models, such as LSSVM, multivariate adaptive regression splines (MARS), and the M5 model tree (M5Tree)
AI-component models
Research content|Reference|Year of publication|Contribution
-|-|-|-
Basic prediction models|[21]|2016|The improved fuzzy neural network method was used to predict low DO events
-|[18]|2020|The prediction performance of ELM and MLP on daily DO concentration was compared
-|[17]|2012|The MLP and RBNN models based on ANNs were used as a comparison with MLR models based on statistical methods
-|[30]|2013|ANNs, ANFIS, and gene expression programming (GEP) were used to compare the prediction performance of DO concentration
-|[16]|2014|The k-means clustering method and MLP were combined to improve the prediction accuracy of the model
-|[19]|2018|Several data-driven methods were used for modeling a comparison of daily DO concentration prediction, such as LSSVM, MARS, and M5Tree
Optimization method for neural networks|[23]|2018|The GA algorithm was adopted to optimize the center and width of the FNN
-|[24]|2018|The best parameters of the BPNN were determined by the PSO algorithm
-|[27]|2019|The dual-scale DO soft-sensor modeling method was applied to improve forecasting performance
-|[25]|2014|The CPSO was employed to optimize the kernel parameter and the regularization parameter of the LSSVR model
-|[26]|2017|The FFA was used to optimize the three parameters of MLP
Deep learning methods|[28]|2020|Deep matrix factorization was adopted for DO forecasting
-|[29]|2020|A deep belief network was applied to improve forecasting performance
Optimization method for decomposition algorithms|[40]|2019|The decomposed series was reconstructed by the sample entropy (SE) method to make forecasting easier
Ensemble methods|[38]|2018|ISMLR + MLR + ANN was used to hierarchically predict high and low concentration data
-|[39]|2020|By a comparison with multiple models such as ELM, ANNs, ANFIS, CART, and MLR, the application potential of the BMA ensemble model was verified
Feature-selection methods|[22]|2019|k-medoids clustering based on segmentation was applied to select features
-|[23]|2018|Correlation analysis was adopted for feature selection
Decomposition methods|[36]|2019|DWT and VMD were adopted to decompose the original data
-|[12]|2018|EEMD was utilized to improve DO forecasting performance

### Xiao et al.(2017)

- Xiao, Z., Peng, L., Chen, Y., Liu, H., Wang, J., Nie, Y. (2017). T**he Dissolved Oxygen Prediction Method Based on Neural Network**. Complexity 2017, e4967870. [doi](https://doi.org/10.1155/2017/4967870)

> the prediction accuracy of the neural network is the highest, and all the predicted values are less than 5% of the error limit, which can meet the needs of practical applications, followed by AR, GM, SVM, and CF. 
> The DO value in aquaculture water is susceptible to **solar radiation**, **temperature**, **pressure**, **wind speed**, and **other** environmental factors. 

### García del Toro et al., (2022)

- García del Toro, E.M., Mateo, L.F., García-Salgado, S., Más-López, M.I., Quijano, M.Á. (2022). **Use of Artificial Neural Networks as a Predictive Tool of Dissolved Oxygen Present in Surface Water Discharged in the Coastal Lagoon of the Mar Menor (Murcia, Spain)**. International Journal of Environmental Research and Public Health 19, 4531. [doi](https://doi.org/10.3390/ijerph19084531)

### Hadjisolomou et al., (2022)

- Hadjisolomou, E., Antoniadis, K., Vasiliades, L., Rousou, M., Thasitis, I., Abualhaija, R., Herodotou, H., Michaelides, M., Kyriakides, I. (2022). **Predicting Coastal Dissolved Oxygen Values with the Use of Artificial Neural Networks: A Case Study for Cyprus**. IOP Conf. Ser.: Earth Environ. Sci. 1123, 012083. [doi](https://doi.org/10.1088/1755-1315/1123/1/012083)

> Several surface water quality parameters such as water temperature, nitrogen species (ammonium, nitrite and nitrate), phosphorus, pH, salinity, electrical conductivity, and chlorophyll-a served as the ANN's input parameters. 
> An ANN with a 9-5-1 topology was developed and ANN managed to predict with good accuracy the DO levels, with the Coefficient of determination (r2) as high as r2=0.991 for the test set.
> - water temperature is the most influential factor

## water temperature

### Ficklin et al., (2023)

- Ficklin, D.L., Hannah, D.M., Wanders, N., Dugdale, S.J., England, J., Klaus, J., Kelleher, C., Khamis, K., Charlton, M.B. (2023). Rethinking river water temperature in a changing, human-dominated world. Natature Water 1, 125–128. [doi](https://doi.org/10.1038/s44221-023-00027-2)
- Do, H.X., Gudmundsson, L., Leonard, M., Westra, S. (2018). **The Global Streamflow Indices and Metadata Archive (GSIM) – Part 1: The production of a daily streamflow archive and metadata.** Earth System Science Data 10, 765–785. [doi](https://doi.org/10.5194/essd-10-765-2018)
  - freely available at https://doi.pangaea.de/10.1594/PANGAEA.887477
  - Gudmundsson, L; Do, HX; Leonard, M et al. (2018): The Global Streamflow Indices and Metadata Archive (GSIM) - Part 2: Time Series Indices and Homogeneity Assessment. https://doi.org/10.1594/PANGAEA.887470

## 基隆河模擬應用

### 水質數據之模式應用

- 張嘉玲、張建業、陳起鳳、林鎮洋、康世芳(2022)基隆河污染源及水質潛在衝擊分析([農業工程學報｜第 66 卷 - 第 2 期](http://www.twaes.org.tw/ae/htmdata/06802002.pdf))

### 早期研究

- [陳筱華(1989)河川污染特性及水質數學模式之探討--以基隆河為例](https://hdl.handle.net/11296/3563hu)
  - [基隆河水質模式探討(I)—缺氧、硝化作用與模式參數](https://tpl.ncl.edu.tw/NclService/pdfdownload?filePath=lV8OirTfsslWcCxIpLbUfjpw-4y5Z-rY8s1III5K_Uc7nJaLd9PWlGZOK73_3WTa&imgType=Bn5sH4BGpJw=&key=WJLx52tzgkFyeaERrRsEQ1ma-eBIi7fQto6l1bJF0IgeVVU9OyINO4qBZJhLTxWd&xmlId=0005306374)
- 柳文成、許銘熙、吳啟瑞、謝文雄(2007)基隆河底泥耗氧之研究。[臺灣㈬利第53卷第2期](https://www.researchgate.net/profile/Chi-Ray-Wu/publication/287906323_Study_on_Sediment_Oxygen_Demand_in_Keelung_River/links/567a5fae08aeaa48fa4c374b/Study-on-Sediment-Oxygen-Demand-in-Keelung-River.pdf)
  - 各測站底泥耗氧量之均值與標準偏差
  - (a)關渡橋 (b)士林焚化廠 (c)百齡橋 (d)中山橋(e)大直橋(f)高速公路橋

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-08-14-11-19-29.png)|![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-08-14-11-25-25.png)
:-:|:-:
各測站底泥耗氧量之均值與標準偏差|底泥耗氧量隨著季節的變化 (a)中山橋與百齡橋
![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-08-14-11-27-22.png)|![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-08-14-11-27-41.png)
(b)關渡橋與士林焚化爐|(c)大直橋與高速公路橋

## Rethingking

### 河川治理之智慧化

1. 清淤工程施作之時機
2. 河水水溫之監控
   - 初期降雨之截流
   - 河川浮動太陽能板船營造遮蔭效果
   - 控制上層溫水不流入之入流閘門壩(橡皮壩)
   - 截彎取直、河道限縮以增加流速、
3. 跨部門之資料整合(如USGS主辦的[EcoSHEDS](https://www.usgs.gov/apps/ecosheds/#/))

### DO之替代

1. 水溫、配合氣象預報之河水溫度預報
2. 河面影像、水面魚類群聚之影像辨識