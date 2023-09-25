---
layout: default
title: 數值模擬、數位對映與環工設計
parent: 計算機輔助工程
nav_order: 99
date: 2023-08-16
last_modified_date: 2023-08-16 11:46:27
tags: AI
---

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

- 此處彙總了數位對映（Digital Twins, DT）的相關書籍、報章及文獻，以及一些工作上的反思。
- 早期做的環境模擬總覺得是靜態的回顧、成因探討，即使做到了「半」模式預報（氣象引用GFS預報結果、排放援引3年前的數據，所計算而得的空氣品質），卻也不能控制什麼來達到防制、保護的效果。畢竟環境的基本定義就是我們不能做什麼來控制的部分，能夠控制的我們稱之為程序。
- 這是為什麼環工的主流價值觀會集中在程序，淨水廠、污水廠站、管線、焚化爐、現地處理、AQCS，因為這些程序、系統等著工程師們、主管們決定可以做些什麼、調控參數，來改變系統的產出、就是產品或服務。
- 早期(Gassó et al., 1992)的環工互動式設計是用Fortran, AUTOLisp, C等語言來撰寫[^7]。
- 現代大量計算資源、顯示器資源均集中在個人電腦上，以虛擬型態來進行模擬、建立數位對映，有其教育意義及優勢[^8]：
  1. 減少模廠之花費與時間
  2. 避免時廠操作錯誤的風險
  3. 運用本地資源進行計算流體力學之計算
  4. 仿真渲染、VR等技術之應用，可以得到最大之臨場感受

## digital twins

### 維基百科的定義

- 數位對映、數位雙生、數位分身、中國翻譯成數字映射
- [wikipedia(2021)](https://zh.wikipedia.org/zh-tw/数字映射)
  > 數位對映（Digital twin），或譯作數位孿生、數位分身、數位雙生，指在資訊化平台內類比物理實體、流程或者系統，類似實體系統在資訊化平台中的雙胞胎。藉助於數位對映，可以在資訊化平台上了解物理實體的狀態，甚至可以對物理實體裡面預定義的介面元件進行控制。

  > 數位對映是物聯網裡面的概念，它指通過整合物理回饋資料，並輔以人工智慧、機器學習和軟體分析，在資訊化平台內建立一個數位化類比。這個類比會根據回饋，隨著物理實體的變化而自動做出相應的變化。理想狀態下，數位對映可以根據多重的回饋源資料進行自我學習，從而幾乎即時地在數位世界裡呈現物理實體的真實狀況。數位對映的回饋源主要依賴於各種感測器，如壓力、角度、速度感測器等。數位對映的自我學習（或稱機器學習）除了可以依賴於感測器的回饋資訊，也可以是通過歷史資料，或者是整合網路的資料學習。後者常指多個同批次的物理實體同時進行不同的操作，並將資料回饋到同一個資訊化平台，數位對映根據海量的資訊回饋，進行迅速的深度學習和精確類比。

  > 數位對映可以應用在各種行業（目前主要是工業）對核心裝置、流程的使用進行最佳化，並簡化維護工作，目前也有農漁業數位分身應用的嘗試。

### Gartner評論

- [Vivian Ku](https://vivian-ku.medium.com/連續三年被評為全球十大科技趨勢的-數位孿生-到底是什麼-上-419a34144529)[^1]部落格
  > 數位孿生(Digital Twin)已連續三年被資訊科技研究機構Gartner評為全球十大科技趨勢之一，簡單來說，數位孿生是指透過存在於虛擬世界的「雙胞胎」，來顯示現實世界中的物體可能的反應、狀況或是效能等。(Gartner最新的報導可以看[這邊](https://www.gartner.com/smarterwithgartner/gartner-top-10-strategic-technology-trends-for-2019)，有興趣的人可以去看看其他九項科技是什麼。)

  > 但是從google trends來看，在過去五年間，Digital Twin顯然沒有引起非常熱烈的討論，一直到2017年時才出現熱潮，可是比起同為十大科技的「區塊鍊」，網路搜尋熱度就差了一大截。這反應的是，數位孿生並非一個全新的技術，而是綜合多項科技與領域，並針對不同產業的痛點所提出的應用，因此，在技術層面涉及較廣泛，且重視Domain know-how的情況之下，發展速度不如預期快速。然而，隨著IOT、AI、AR、VR等技術的到位，數位孿生肯定是下一波工業4.0發展重點中的重點。

## 數值模擬 vs 數位對映

- 到底是人腦聰明還是電腦聰明？這類的主題總不會停止討論。《Engineering》是中国工程院于2015年创办的工程科技综合性期刊，在2019年第5卷第5期出版了關於水污染控制的專刊，其中也收錄了一篇Sean O’Neill(2019)《数学推理挑战人工智能》[^3]，對當代的AI不如人類數學推理的悲觀看法。但如果今天來看，恐怕作者要改寫短文的結論了。

### 環工程序的數值模擬

- 有關製程用水、冷卻水、飲用水、與廢水處理工場的計算流體力學模式模擬源自於1990年代，近年來有很大的突破，除了傳統化工反應槽或生物處理的開發應用之外，在核能發電廠的研究成果對環工實務也有很大的貢獻，包括商業CFD軟體、開源CFD軟體、以及研究單位開放的軟體等等，可以詳見[CFD在水務工程中的應用](https://sinotec2.github.io/AIEE/CAE/CFD/)
- 在台電最新的AQCS更新改建計畫中，就應用了CFD進行細部設計的敏感性分析，包括導流板、粗灰阻隔設備、SCR之注氨系統AIG、或混流器等流場設計調整。[^2]

### IBM官網之說明

- 依據[IBM ](https://www.ibm.com/topics/what-is-a-digital-twin)對數位對映與一般模擬仿真與同化差異的說明
  - 相同處：都是用數字將真實世界予以量化，以便進行診斷、解析、並作出預測及評估。二者對系統而言，都是不可或缺的數值方法。
  - 相異處
    1. 規模：數位對映本身除了專注在流程，還能加入邏輯上還不能解釋相關性的環境數據，甚或整併任意數量的數值模擬結果，來研究多程序間的交互作用。
    2. 即時性：數值模式對即時模擬的計算需求是非常龐大，少數應用在無法控制的程序或系統，如天氣、地震及火山活動的短期預報。但數位對映的設計目的原本就是用在即時監測與控制雙向信息流的決策機制，該信息流首先發生自傳感器即時傳送到系統處理器，而在處理器達成新的診斷、預測與決策後，資訊流又發生自系統處理器傳送到現場可控制物件，產生即時性的反應。
    3. 更廣泛的應用：數值模式的敏感性測試項目取決於模式基本的統御方程式、條件與參數，是預先決定的。但數位對映因納入非邏輯性的數據變數，對系統可能影響對變因將會保持更開放的態度，可以提供系統與產品更多改進的可能性。

### 水廠的智慧化

- 北京師範大學侯立安教授在工程期刊上發表對《建设生产健康饮水的智慧水厂》的看法[^4]，就壓力面而言，侯教授提出了水質安全、複合複雜、新污染新技術難融入、突發情況應急、管網更新與二次污染等5項問題，相應對策則有淨化單元模塊化、淨化過程綠色化、回收物質資源化、控制方式智能化等4個關鍵特質，建構低耗能、精準加藥、數位化與智能化融合共生的水廠。
- [^6]這篇浙江大學的研究雖然是針對工業用水模廠( Secure Water Treatment (SWaT) 測試床)的虛實系統(Cyber-Physical Systems, CPS)研究，但因為是針對網路攻擊的異常狀況的AI訓練，對靠網際網路連線的監測系統而言，其參考價值還是蠻高的。
- How Simulation Helps Clean and Manage Water by [Ansys blog(MARCH 22, 2023)](https://www.ansys.com/blog/how-simulation-cleans-and-conserves-water)

### 中德合作water4.0

- 這篇短文綜合了2個中國境內湖泊(巢湖及鄱陽湖)的水質管理計畫，應用最新的即時監測設備、GIS系統、VR(Unity)、以及遠端控制系統，來做到實場與實驗室的數位對映[^5]。其軟、硬體規格與功能構想值得參考。
- 不過當中還沒有加入數值模式(水質擴散模式、水廠CFD等等)、統計或任何形式的AI模型，水廠部分的自動(或智慧)控制也沒有著墨。畢竟是試驗性質的計畫，主要還是著重在環境資訊與最後的顯示決策系統展示，真正實場的控制涉及供水、廢水處理的實務與各單位的權責，應該是行政協調而不是研究計畫可以碰觸的決策。

## 水處理設計之套裝軟件

### top 5

From [SmartServ(2022)](https://smartserv.io/blog/top-water-treatment-software/) Top 5 Water Treatment Software In 2022

- DuPont [WAVE](https://www.dupont.com/water/resources/design-software.html)
  > Water Application Value Engine (WAVE) is the industry’s first fully integrated free modeling software program to integrate our leading technologies — ultrafiltration (UF), reverse osmosis (RO), ion exchange (IX), and now incorporates DesaliTec™ SOAR CCRO — into one comprehensive tool. Using a common interface, it simplifies the design process and ultimately helps reduce the time needed to manage your water-treatment system. 
- [SmartServ](https://smartserv.io/blog/top-water-treatment-software/)
  - Picture Notes/Custom equipment/Hide pricing using ACL/Create and show tiered pricing to your customers./Payment intermediate page/
  - 整體工程採購、全方位輔助軟體
  - 專人解說示範、無下載版。
- [Aqua Designer]()
- [Envirosuite](https://envirosuite.com/insights/news/evs-water-plant-designer): Water Simulation Software。提供30日試用版。
- Workever: Water Hygiene & Treatment Business Software

## books about digital twins(DT)

### 最新上架

- Ali Kashif Bashir， Balamurugan Balusamy， Pooja Malik， Rajasekar Vani， and Rajesh Kumar Dhanaraj(2023)**Digital Twin for Smart Manufacturing**([google books](https://www.google.com.tw/books/edition/Digital_Twin_for_Smart_Manufacturing/xC2gEAAAQBAJ?hl=zh-TW))
  > Digital Twin for Smart Manufacturing: Emerging Approaches and Applications provides detailed descriptions on how to integrate and optimize novel digital technologies for smart manufacturing. 
  
    > The book discusses digital twins, which combine the industrial internet of things, artificial intelligence, machine learning and software analytics with spatial network graphs to create living digital simulation models that update and change as their physical counterparts change. 
  
  > In addition, they provide an effective way to integrate technologies like cyber-physical systems into a smart manufacturing system, potentially optimizing the entire business process and operating procedure of the manufacturing firm.

- Noel Crespi, Adam T. Drobot, Roberto Minerva(2023)**The Digital Twin**([springer](https://link.springer.com/book/10.1007/978-3-031-21343-4))
  > Covers the origin and history of the “Digital Twin” and the path that leads to where we are today

  > Identifies the impacts of the technological evolution and transformation in the next 5-8 years on Digital Twins

  > Provides an in depth look at the basic and enabling technologies that are necessary for implementation

### 經典推薦

  - David Gelernter(1993)Mirror Worlds: or the Day Software Puts the Universe in a Shoebox...How It Will Happen and What It Will Mean([amazon](https://www.amazon.com/Mirror-Worlds-Software-Universe-Shoebox/dp/019507906X))
  > Technology doesn't flow smoothly; it's the big surprises that matter, and Yale computer expert David Gelernter sees one such giant leap right on the horizon. Today's small scale software programs are about to be joined by vast public software works that will revolutionize computing and transform society as a whole. One such vast program is the "Mirror World."

  > Imagine looking at your computer screen and seeing reality--an image of your city, for instance, complete with moving traffic patterns, or a picture that sketches the state of an entire far-flung corporation at this second. These representations are called Mirror Worlds, and according to Gelernter they will soon be available to everyone. Mirror Worlds are high-tech voodoo dolls: by interacting with the images, you interact with reality. Indeed, Mirror Worlds will revolutionize the use of computers, transforming them from (mere) handy tools to crystal balls which will allow us to see the world more vividly and see into it more deeply. Reality will be replaced gradually, piece-by-piece, by a software imitation; we will live inside the imitation; and the surprising thing is--this will be a great humanistic advance. We gain control over our world, plus a huge new measure of insight and vision.

  > In this fascinating book--part speculation, part explanation--Gelernter takes us on a tour of the computer technology of the near future. Mirror Worlds, he contends, will allow us to explore the world in unprecedented depth and detail without ever changing out of our pajamas. A hospital administrator might wander through an entire medical complex via a desktop computer. Any citizen might explore the performance of the local schools, chat electronically with teachers and other Mirror World visitors, plant software agents to report back on interesting topics; decide to run for the local school board, hire a campaign manager, and conduct the better part of the campaign itself--all by interacting with the Mirror World.

  > Gelernter doesn't just speculate about how this amazing new software will be used--he shows us how it will be made, explaining carefully and in detail how to build a Mirror World using technology already available. We learn about "disembodied machines," "trellises," "ensembles," and other computer components which sound obscure, but which Gelernter explains using familiar metaphors and terms. (He tells us that a Mirror World is a microcosm just like a Japanese garden or a Gothic cathedral, and that a computer program is translated by the computer in the same way a symphony is translated by a violinist into music.)
 
  > Mirror Worlds offers a lucid and humanistic account of the coming software revolution, told by a computer scientist at the cutting edge of his field.

- A.Y.C. Nee， S.K. Ong(2021)Digital Twins in Industry([google books](https://www.google.com.tw/books/edition/Digital_Twins_in_Industry/NWC_zgEACAAJ?hl=zh-TW))
  > Digital Twins in Industry is a compilation of works by authors with specific emphasis on industrial applications.

  > Much of the research on digital twins has been conducted by the academia in both theoretical considerations and laboratory-based prototypes. Industry, while taking the lead on larger scale implementations of Digital Twins (DT) using sophisticated software, is concentrating on dedicated solutions that are not within the reach of the average-sized industries.

  > This book covers 11 chapters of various implementations of DT. It provides an insight for companies who are contemplating the adaption of the DT technology, as well as researchers and senior students in exploring the potential of DT and its associated technologies.

[^1]: 連續三年被評為全球十大科技趨勢的「數位孿生」到底是什麼？(上)
[^2]: 劉源隆、吳政宏、王郁惠、陳廷博(2020)既有燃煤發電機組空污防制設備效能提升可行性評估工業污染防治 第 150 期 (Nov. 2020) pp80 ~ 101 ([pdf](https://proj.ftis.org.tw/eta/WebPhotos/2020/既有燃煤發電機組空污防制設備效能提升可行性評估.pdf))
[^3]:  Sean O’Neill. **Mathematical Reasoning Challenges Artificial Intelligence**. Engineering, [doi](https://doi.org/10.1016/j.eng.2019.08.009)
[^4]:  Li’an Hou. **Creating Smart Waterworks to Produce Healthy Drinking Water**. Engineering, [doi](https://doi.org/10.1016/j.eng.2019.07.017)
[^5]: Olaf Kolditz, Karsten Rink, Erik Nixdorf, Thomas Fischer, Lars Bilke, Dmitri Naumov, Zhenliang Liao, Tianxiang Yue. **Environmental Information Systems: Paving the Path for Digitally Facilitated Water Management (Water 4.0)**. Engineering, [doi](https://doi.org/10.1016/j.eng.2019.08.002).
[^6]: Macas, M., Wu, C. (2019). **An Unsupervised Framework for Anomaly Detection in a Water Treatment System**, Presented at the 2019 18th IEEE International Conference on Machine Learning and Applications (ICMLA), Athens, Greece, pp. 1298–1305. [doi](https://doi.org/10.1109/ICMLA.2019.00212)
[^7]: Gassó, S., Baldasano, J., Celades, C. (1992). **The SIMTAR CAD/CAE system for the interactive computer aided design of wastewater treatment facilities**. Environmental Software 7, 155–164.
[^8]: Roozbeh Mottaghi (2022) **AI2-THOR: A virtual environment for training home assistant robots** by [Unity@youtube](https://www.youtube.com/watch?v=w27UKcFXcmk&t=20s)
