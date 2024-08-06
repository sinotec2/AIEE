---
layout: default
title: AI在水廠及管線工程領域之應用
parent: 回顧與綜覽
nav_order: 99
date: 2023-08-15
last_modified_date: 2023-08-22 10:42:27
tags: AI
---

# AI在水廠及管線工程領域之應用

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

## 歐美目前進度

### 工研院產發所報導

- 創新永續水之道／AI+大數據創新解方 搶救水資源大作戰([2023-03-20 11:48 聯合新聞網／工業技術與資訊](https://udn.com/news/story/6905/7042846))
  > 工研院產業科技國際策略發展所分析師陳昭文指出，水資源管理的挑戰不外乎「即時資訊難獲得」、「異常事件難防範預測」、「資訊龐雜未規格化」3類。...市調機構MarketsandMarkets統計，全球智慧水資源管理市場規模將在2026年達到224億美元，未來3年，年平均複合成長率超過10%。
  > **計算流體力學與數據分析 輕鬆完成遠端水質監控**(比利時公司AM-TEAM)幫助荷蘭水利委員會只花6個禮拜就完成人工需耗時1年的汙水測試作業，並節省了10萬歐元經費。美國維吉尼亞州汙水處理廠，亦已將其產品用於臭氧淨水處理程序，進行預測情境的**數位模擬測試**。
  > **AI數位孿生系統　提前24小時預知系統故障**(西班牙自來水業者的關係企業Idrica)進行水系統管漏偵測、飲用水與汙水處理作業管理、智慧灌溉服務。這套數位孿生系統已替西班牙瓦倫西亞的自來水公司減少18%的漏水損失，哥倫比亞自來水公司的供水系統維護成本也因此降低了20%。
  > **水資源危機預測系統　智慧城市未來必備**
  > 法國的Suez Smart Solutions透過人工智慧與大數據分析，進行供水系統與廢水處理和檢測作業即時監控，可以提前20小時預警未來可能發生的洪災旱與汙染事件危機。
  > Suez Smart Solution積極參與全球許多智慧城市計畫，除了水資源資料之外，也將氣象中心、電力公司的開放性資料，比如氣溫、雨量、電價費率等，一同納入系統，提供更準確的管理與預測服務，且多半以結盟參與方式進行，例如在美國，自來水公司的水網管線監控服務與AI軟體業者Fracta合作，而在澳洲雪梨的物聯網水資源管理應用服務，則是與大數據管理平台業者 NEC合作。
  > **數位農業軟體平台　資訊共享提升產量**
  > 舊金山的科技業者The Climate Corporation，由Google等科技公司員工共同創立，打造數位農業軟體平台，解決氣候變遷造成的水資源短缺與農業減產問題。
- AM-TEAM (Advanced modelling services for process optimisation and design) ([About us](https://www.am-team.com/) and [customer](https://www.am-team.com/en/customer-stories/index.html))
- Idrica是由125年歷史的水務公司Global Omnium所創立，專職在發展並銷售該母公司數位轉型的之成果。

### CFD的應用

- CFD當中富含許多流體力學、紊流理論、質量、動量、能量守恆定律，以及多年來學者專家投入的參數化理論，經由現代顯示軟體的包裝，提供使用者貼近現實的數值經驗。這項利器也隨著計算機能力的提升、計算雲端化過程，而變得越來越普及。
- CFD再水廠、管線設施的應用詳見[CFD在水務工程中的應用與AI發展](https://sinotec2.github.io/AIEE/CAE/CFD/)

### rethinking overview

- 過去我們將設計與現場經驗濃縮在設計規格、規範裡，然而個案現地狀況層出不窮，需要設計人員發揮團隊發揮創意，在規設階段解決大半、真正運轉操作階段解決其他。而這些問題無非是可以量化的環境數據條件，是可以經由其他個案的累積以及機械學習的過程，達到智慧化的目標。
- 這不是意味著不再需要設計規範，而是在規範的合理範圍內，得出更加適切、更精確、更少過度設計、更需依靠數據預先判斷來操作的最佳方案。
- 按照實場規格條件製作數值模式的用意，不只在強化規設的合理性、在減少現場操作的試誤，更在於增加極端情況、意外災害的應變能力(包括風災、強降雨、洪水、流行病、缺水、地震、大規模野火、甚至戰爭)。這對於氣候變遷的當今環境而言，是非常必要的知識能力。
- 國外經驗模式在本地的適用性，對於需要邊界初始條件的推論型模式確有其困難，但經由給定正確的條件並加以率定校調之後即可應用。然而對於類神經網路、機械學習模式而言，本地、類似規模的實場數據卻屬必要，其模型預報的意義不會超出其數據本身。不過就充分性而言，這類模式是不會拒絕任何有意義的數據的、即使代表性不那麼高。

## 自來水處理廠

### 精準加藥

- 自來水公司2023年提出擬在清洲淨水場建立AI精準加藥的示範計畫，應用該廠過去20萬筆數據，解決傳統反饋式加藥造成水質震盪的問題、並有效減少污泥量[^15]。
- 臥龍智慧謝文彬博士  
  - 用AI解決水資源問題，臥龍智慧年節省上百萬水費([知勢2021/11/13](https://edge.aif.tw/aipoint-interview/))
  - 年省百萬水費！臥龍智慧靠AI加藥系統為企業節水減碳([知勢2021/11/30](https://meet.bnext.com.tw/articles/view/48487?))
  - 工業局《永續產業發展期刊》2021年12月製作了有關水資源的特刊，當中收錄了一篇由謝文彬博士及其團隊所撰寫有關水處理數位轉型的文章，當中不但介紹了他們在產業界的服務實績，也分享他們對水處理領域智慧化前景與路徑的看法。[^53]
  - AI助攻新世代智慧廢水處理廠([新電子2023年04月18日](https://www.mem.com.tw/ai助攻新世代智慧廢水處理廠/))
- 隆忠企業有限公司
  - AI智能加藥廢水處理系統為企業節省水資源([Home->實績案例->廠務水務系統->AI智能加藥廢水處理系統為企業節省水資源](https://longzhong.com.tw/zh-tw/cases.php?act=view&id=50))

[^15]: 台灣自來水（股）公司第八區管理處操作課(2023)自來水水質再進化 AI 精準加藥，112 年度經濟部中小企業處新創採購-場域實證‧共創解題。[經濟部中小企業處](https://www.spp.org.tw/spp/file_downloads/question/台灣自來水股份有限公司第八區管理處操作課─自來水水質再進化AI精準加藥.pdf)
[^53]: 謝文彬、林庭瑋、張力夫、范煥榮(2021)智慧水處理與水回收數位轉型新契機([工業局永續產業發展特刊91期pp60~67](https://proj.ftis.org.tw/isdn/Download/FileDownLoad?fileid=210))

### 反洗終點判斷

逢甲環科系吳志超教授
- 吳志超、楊惠玲、賴思樺、陳劭瑜(2022)智能影像辨識應用於濾池反洗終點判斷之研究 。中華民國自來水協會會刊 (中華民國自來水協會)(2022-08)

## 自來水滲漏檢測

- 李丁來、林子立、盧烽銘、黃香蘭(2017)台灣自來水管網漏水檢測技術現況與展望([自來水會刊第35卷第1期](https://tpl.ncl.edu.tw/NclService/pdfdownload?filePath=lV8OirTfsslWcCxIpLbUfg1V9cr4x1WcPDtJtzCNlHoNYlUXbu6_j6Ydd8gbOtpR&imgType=Bn5sH4BGpJw=&key=rVo9VgdvPyHzBS_-UcHMGhOFS3ON8V3LfTWQBCdCLsgeVVU9OyINO4qBZJhLTxWd&xmlId=0006861097))

  > 常用主動檢漏法、技術及設備概略如下:1.音聽法、2.環境調查法(路面情況、管線上方道路草木茂盛、路邊溝渠清水長流等情況判定)、3.餘氯檢測法(有效餘氯可將 DPD 氧化，使其轉變為紅色化合物，通過目視比色判斷)、4.分段查漏法(夜間分段逐次進行供水幹管與分支管測漏)、5.夜間小區最小流量測定法、6.升壓檢漏法、7.窨井查漏法、8.相關儀檢測法(量測漏水聲波沿管線傳播之時間差)

### 現有技術：聽音測漏

- 全球首創 AI 巡檢漏水技術！工研院助花東震後災區快速復水([科技新報2022年11月15日](https://technews.tw/2022/11/15/imarc/))
  > 只要 3 秒就能辨識水管是否發生洩漏，並在花東地震後協助台灣自來水公司查出災區 27 處供水管線異常，其中 25 處診斷正確，辨識準確率高達92.5%

  > 這項技術為全球首創結合本土化漏水診斷設備**擷取現場動態音訊**，透過 AI 人工智慧漏水音診斷模型，整合 5G、AIoT 資訊同步進行洩漏事件辨識與漏點定位，採面-線-點由大到小管網檢漏策略概念，快速精準管網洩漏定位技術，可應用於金屬、PVC 等複合管道漏水檢測。

### 衛星檢測技術

- Earth Observation That Sees Below the Surface
- Actionable AI-driven insights from beneath the surface of the Earth
- ASTERRA provides a number of industries with intelligence and insights from beneath the surface of their largest installations. Without breaking ground, ASTERRA uses patented algorithms and artificial intelligence to detect leaks, assess pipes, explore minerals, and locate moisture near major installations.([ASTERRA](https://asterra.io/))
- 以色列商Utils(now ASTERRA)
  - 使用衛星上合成孔徑雷達(synthetic aperture radar, SAR)之回波圖像進行差異分析
  - 空間解析度100M、地面下3公尺、最低偵測水量(0.5L/min)
  - 能區分汙水、地表水、飲用水

|![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-08-15-08-54-29.png)|
|:-:|
|雷達影像漏水檢測熱區圖 from Warner, B. (2021), “Water tech that’s out of this world". [Atlas of the Future](https://atlasofthefuture.org/project/utilis/)|

## 工業用水、節水

### 冷卻水精準加藥

- 用AI解決水資源問題，臥龍智慧年節省上百萬水費([知勢2021/11/13](https://edge.aif.tw/aipoint-interview/))
  > 石化廠每日用水量18000噸，其中冷卻水塔的用水量佔總用水量的52％。導入AI精準加藥系統...一年下來，13座水塔就省下約七百多萬的水費。
  > Sensor全防禦系統自動判斷警訊是Sensor本身問題還是系統問題，並且在Sensor異常狀態時，預警並提醒保養及健康狀態。

### 智慧水處理與水回收數位轉型

- 謝文彬、林庭瑋、張力夫、范煥榮(2021)智慧水處理與水回收數位轉型新契機([工業局永續產業發展特刊91期pp60~67](https://proj.ftis.org.tw/isdn/Download/FileDownLoad?fileid=210))

![](https://github.com/sinotec2/FAQ/raw/main//attachments/2023-08-15-15-29-36.png)

![](https://github.com/sinotec2/FAQ/raw/main//attachments/2023-08-15-15-25-02.png)

|![](https://github.com/sinotec2/FAQ/raw/main//attachments/2023-08-15-15-19-07.png)|
|:-:|
|染整廠廢水於化學混凝系統AI 精準加藥實際案例與成效。導電度由 7,500降低至 3,000 µs/cm，目前精準加藥應用包含化學混凝系統、冷卻水塔系統、管末水處理與回收、UF/RO 薄膜系統，MBR，A2O，活性污泥等加藥系統。[謝等(2021)][pdf1]|

## 中水系統

- 臺中市政府研究發展成果網[台中市水資源回收中心水回收再利用之潛勢探討](https://rdnet.taichung.gov.tw/media/428208/2122514262486.pdf)
  - 工業用水標的：需監測設備150套
  - 冷卻用水標的：約需53套
  - 為澆灌/學校沖廁用水：亦為53套
  - 灌溉用水：約1套
- 臺中市水利局2017[臺中市福田水資源回收中心放流水回收再利用統包工程(含營運及維護) 招商說明](http://www.hydraulic.org.tw/new/upfile/file/20170802/2017080210520876876.pdf)
  - 水質水量即時監測系統：配合營運管理提出輸水管即時監測系統之配置需求
- 桃園市政府2021[桃園北區再生水BTO計畫先期暨建設及財務計畫(定稿本)](https://ws.tycg.gov.tw/Download.ashx)
  - 文中有即時監測系統之規劃與經費
- 再生水多元運用─產業園區應用實例[林志墩等2017](https://www.ceci.org.tw/Upload/Download/6FE352A4-F8BA-4CBB-A3D1-FBF8A4EAB771.pdf)

## 廢水處理

### 桃園北區污水廠鏡檢自動化及智慧化

直擊！AI人才Show 微生物是污水處理的關鍵，AI助攻讓水廠淨化更有效率！([關鍵評論THE NEWS LENS 2022/11/23](https://www.thenewslens.com/feature/aishow/177007))

> 顯微影像專家*祥泰綠色科技*，用一滴水的樣本，即可在顯微鏡下辨識微生物狀態；但這樣的knowhow希望擴大規模，若能以AI來判讀廢水處理各單位的顯微影像資料，對於水廠的現場運作及遠端監控，很有幫助。

> AI新創*智悠科技*接下這個難題之後，設計協定讓微生物的顯微影像可被AI模型判讀，並在3個月的概念驗證期間，不斷輸入資料來訓練AI，再與負責桃園北區污水廠建置的*日鼎水務*，進行實際場域測試，產出的結果讓水廠有更精準的依據，來決定投藥量或採取其他對策。未來，這套AI判視微生物系統，還將與更多水廠合作，甚至推向國際。
- 2015/12/11 - 發明廢水診斷系統、廢水診斷裝置與廢水資料處理辦法([祥泰綠色科技](http://www.awg.com.tw/about-us/patent-license.html))

- 智悠科技公司發展重點在強化1.自動化系統整合、2.機器人設備、3.節能系統整合現有領域([公司組織](http://www.mutek-dus.com/about.php))

### 電鍍業之應用

- 高季安(2022)人工智慧於精準電鍍之應用([先知科技股份有限公司-綠色數位轉型文章分享](https://fs-technology.com/post_20230106.html))

### 研華+AI整合

- 研华精准加药&精确曝气解决方案([ADVANTECH Home->Support->Resources 5/17/2023](https://www.advantech.com/en/resources/news/精准加药精确曝气解决方案))

[^1]: 謝文彬、林庭瑋、張力夫、范煥榮(2021)智慧水處理與水回收數位轉型新契機([工業局永續產業發展特刊91期pp60~67](https://proj.ftis.org.tw/isdn/Download/FileDownLoad?fileid=210))

[pdf1]: https://proj.ftis.org.tw/isdn/Download/FileDownLoad?fileid=210 "謝文彬、林庭瑋、張力夫、范煥榮(2021)智慧水處理與水回收數位轉型新契機(工業局永續產業發展特刊91期pp60~67)"
