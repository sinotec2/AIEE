---
layout: default
title: CFD在水務工程中的應用與AI發展
parent: 計算機輔助工程
nav_order: 99
date: 2023-08-17
last_modified_date: 2023-08-21 10:02:26
tags: AI CFD
aside:
  toc: true
sidebar:
  nav: layouts
---

# CFD在水務工程中的應用與AI發展
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

### IWA(The International Water Association)

- 水廠的模式模擬是結合機械、化工、資訊等專業長期耕耘的一個領域，國際間的設計顧問公司雖然不多，但也持續發展中。協會平台以IWA為主，在IWA架構下設有IMA(IWA Specialist Group Modelling and Integrated Assessment (MIA)原自行辦理研討會[^23])，目前委員
  - 學界：比利時Ghent、法國 Engees Strasbourg[^24]、[瑞典Lund][ulf]等大學
  - 顧問公司：比利時AM-Team、[Ibis Group][ibis]、Ed Wicklein
([Carollo Engineers](https://carollo.com/))[^22]、Javier Climent ([Grupo Gimeno](https://www.grupogimeno.com/en/))

### IWA 短文

- [Wim Audenaert (November 16, 2020)](https://iwa-network.org/computational-fluid-dynamics-cfd-a-revolutionary-tool-for-the-water-industry/) Computational fluid dynamics (CFD): a revolutionary tool for the water industry.
  - 這篇刊登在IWA的短文針對氣候變遷、流行病肆虐的當代環境，作者認為需要建立數位對映(Digital Twins, DT)來強化水廠的因應能力，其中的核心內涵即為水廠的CFD數值模型。CFD甚至可以在模廠興建之前就能提供足夠的設計數據，並且在現地放樣的過程，快速達到預期的穩定成果。
  - 作者是比利時公司[AM-TEAM](https://www.am-team.com/)(Advanced modelling services for process optimisation and design)的總裁，該公司是一家水處理單元CFD及動力模擬與設計服務的全球性公司。實績詳見官網[customer](https://www.am-team.com/en/customer-stories/index.html)。
  - 評論：
    - CFD公司非常努力拉近當代市場需要與IT產業熱門話題。即使是3年前的短文，仍然感覺很遙遠。
    - 然而DT的特性強項在於即時性、操作性。CFD要加入在DT的框架，除了計算速度必須有很大的突破，介面也必須大幅的模組化、簡化。前者可以透過模擬結果的機械學習，後者則會因為設計主題而異。
    - CFD最費工的程序在3D建模。基設階段、細設、或者修繕階段的建模方式都不太相同。或許這是AI可以協助補足的地方。

### IWA研討(習)會

- 2023/1/18-22水回收模擬研討會(IWA Water Resource Recovery Modelling Seminar)針對模式校驗證與數位對映等主題，發表論文討論，也舉行青年工程師的研習培訓，以及共同發表了未來願景。
  - 研習會主題支援：[Dynamita公司](https://dynamita.com)的SUMO軟體

### 廢水處理CFD設計之回顧

- Samstag et al., (2016)這篇較早期的回顧文章[^25]有廣泛的涉獵，並對當時粒子膠結與分散、生物與水力耦合等模擬過程提出建言。

### 教學輔助APP

- 弘光科技大學副校長蘇弘毅(2023)向教育部提出一項創新教學實踐方案，用DesignSolver來教授傳統環工單元操作課程，就是參考了英國利物浦約翰摩爾斯大學海事與機械工程系Seddighi教授的作法[^32]。蘇教授的原文：

> 在機械工程領域的教學上，Seddighi 等學者探討使用 IPython 筆記型電腦結合工業標準軟體教導機械系學生 CFD (Computational Fluid Dynamics) 電腦模擬流體動力學課程，這個研究採用混成學習模式並強調在做中學的精神，結合講授、助教、作業等高度互動方式。結果顯示，學生對於 CFD 理論與基礎觀念有良好的了解，使用這樣的電腦輔助設施可以增進 CFD 主題的教學效能 [^31]
- 蘇教授的教學內容現階段雖未包括環工單元操作的CFD，但也隱含了未來可以發展的潛質方向。
- 經了解Seddighi教授的做法就是規避深入艱澀的流體力學控制方程式與紊流模式，而是以Jupyter Notebook逐條計算的方式，以1小時講解完畢，而以另外的2小時讓學生自行操作CFD已完成指定的作業。這個作法基本上也是將複雜的CFD予以模組化、以更高階的管理方式予以封包。

## 入流工之CFD

- Scum Buster For Water Treatment Animation(vertical drop) by [Porter McGuffie, Inc(2013)](https://www.youtube.com/watch?v=kkEh-rGmxhM)
- Tank Bottom Sludge & Grit Mixing - Vertical Wetwell (CFD) by [Vaughan Company Pump](https://www.youtube.com/watch?v=IJOYY1t9pWQ)
  > CFD animation demonstrating how a 6 inch layer of grit buildup on a tank floor is suspended, mixed, and homogenized in minutes.
  
  > Streamlines indicate fluid paths, demonstrating complete tank mixing using a Vertical Wet Well Recirculating CHOPPER Pump (tank size: 12x12x9'). 
 
## 膠凝池之CFD模擬

### 回顧

- Bridgeman et al., (2009)這篇早期針對膠凝池的CFD回顧文章，對多相流、蘭氏軌跡、以及母數平衡公式等等作法都提出了批判性的評論。[^20]不過就後續相關膠凝池CFD的發展而言，這篇文章可以說近乎絕響。

### CFD of mixer

- The Art of Mixing by [xylem/Flygt(2023)](https://www.xylem.com/en-ai/about-xylem/newsroom/events/webinar-the-art-of-mixing/)

### 近年相關論文

- Zouboulis et al.(2010)簡化了膠羽尺寸的流體行為來降低計算負荷，模式應用在低濃度進流之混凝過程，並用希臘帖撒羅尼加市的淨水場實場數據來模擬。研究發現因入流濃度太低，無法形成大到足以沉降的膠羽，必須回流污泥以增加顆粒數量。[^26]
- Shi et al.(2019)與[Wang et. al 2022][doi29]同樣使用了CFD與PBM偶和模擬的方式，來進行混凝槽的模擬。經由變動入流SS的顆粒大小，研究膠凝池中的非線性過程，並進行可視覺化及定性之比較。[^30]
- Chatila and Danageuzian, (2022)使用Ansy EFFLUENT及實驗室尺寸混凝槽之PIV(Particle Image Velocimetry )測速結果進行低轉速膠羽形成過程的模擬，藉此定量滑動係數&kappa;。經由模擬協助在相同速度梯度條件下，可以降低&kappa;自0.25至0.18，有效減少膠凝池的用電量。[^28]
- 國內學位論文：[自來水淨水廠高速膠凝澄清池之操作與結構改進]()

### 模擬動畫

- [THINK Fluid Dynamix](https://www.youtube.com/watch?v=hzr2DjqAuHw)

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-08-21-15-59-19.png)

## 氣泡質傳、熱交換等相關學術文獻

### 法國圖盧茲大學團隊

- 法國圖盧茲大學團隊Cockx et al., (2001)這篇較早期的文章使用了該國電力公司(Electricité de France EDF)所發展的二相氣泡流CFD商業程式ASTRID-Tri_CFD，研究廢水處理程序中氣泡的全域及局部質傳現象及系數[^1]。
  - 本研究居於同作者先前有關氣升式內部環流反應器研究[^3]、以及臭氧反應塔研究[^4]，都是使用ASTRID之CFD程式。
  - ASTRID(Advanced Sodium Technological Reactor for Industrial Demonstration)先進鈉技術反應堆工業示範計畫是CEA自2006年開始的項目。目前該計畫中的CFD是用以預測反應槽中鈉金屬的熱流行為。[Bieder et al., (2019)][2]也將其應用在ASTRID反應器1/6比例尺模廠之熱水模擬及驗證。[^2]
  - CEA(Commissariat à l'énergie atomique et aux énergies alternatives)法國原子能和替代能源委員會
- 團隊(Ngu et al., 2022)持續發展二氧化碳化學吸附反應塔質傳現象的CFD[^14]，以及生物產氫的質傳數值與模場模擬研究(Ngu et al., 2023)[^15]，不再使用商用軟體，改由自行研發。

### 中國石油大學重質油國家重點實驗室

- 團隊建立了一個4.4m高對向流的氣泡塔模型廠、並建立數值模式來預測氣泡塔的流場與質傳[^16]

### OpenFOAM

- 這篇由中國科學院上海高等研究院團隊(Zhao et al., 2023)的應用研究，將泛用行CFD模式OpenFOAM應用在臭氧接觸槽中質傳的計算，最大的貢獻在於建立了視覺氣泡量測，以律定CFD中的介面力學模式(阻力、氣泡上升及紊流模式)與多尺寸氣泡模式(氣泡數平衡方程式及界面面積傳輸方程式)。[^5]
  - 大多數人是用OpenFOAM中的volume of fluid (VoF) 方法進行模擬，如[^6]用OpenFOAM和Fluent兩個模式來計算氣泡柱的質傳。
- 在核能廠熱水系統中熱傳與質傳的OpenFOAM應用，如阿根廷國立海岸大學團隊([Corzo et al., 2023][7])[^7]，該研究中使用0維與3維耦合的動態邊界條件，來模擬管線、加壓站、熱交換器、與開放冷卻水塘的冷卻現象。
  > To overcome the above mentioned issues, the nuclear engineering community has invested immense efforts to couple system codes with CFD codes [4] [5] [6]. 
  > There are few publications addressing this topic through semi-implicit or implicit techniques while most such papers are based on explicit coupling. In the later, the system codes and 3D CFD codes run in a staggered way, communicating the necessary data through temporary files and flags. 
  
  > One of the first attempts was done by Martin et al. [7], who coupled RELAP5 with other codes transferring data through a Parallel Virtual Machine (PVM) protocol. In the same way, Aumiller et al. [8] did so using RELAP5-3D with a CFD code showing good results while finding some numerical instability. 

  > More recent developments also using explicit methods, coupled RELAP with **ANSYS-CFX** [9], ATHLET with **OpenFOAM**Ⓡ [10], and TRACE with **Star-CCM** [11]. In all cases the system codes assumed the master role, sending the necessary information such as mass flow, pressure, and temperature, amongst others, to the CFD code. These mass-flow/pressure couplings are relatively simple because the pressure in the coupled domains remains constant until the end of the time step, but they could lead to stability problems under large time steps or fast transient simulations [12]. 

  > In order to eliminate numerical instabilities Weaver et al. [13] proposed a generic semi-implicit coupling technique, which uses the master/slave communication roles but update both the velocity and pressure in each communication step. This coupling methodology showed good performance in several flow conditions [14] [15]. Bandini et al. [16] presented a detailed compilation of the publications concerning code-coupling tools to simulate new-generation reactors focusing on the validation of these tools against experimental facilities.
  - (Corzo et al., 2023)也應用OpenFOAM在行進中巴士內流場的模擬，這經驗對場站內的通風設計也會有不少啟發。[^8]
- 印度霍米巴巴國家研究所團隊([Bhusare et al., 2017][12])發展出適用在氣泡塔質傳研究的OpenFOAM應用，他們主要的貢獻在於彙整了文獻中相關的試驗觀測數據，並用以驗證CFD模擬結果，除了OpenFOAM外，團隊以FLUENT進行同樣條件的模擬，藉此比較驗證模型的正確性，在實場的模擬中，作者以氣體停留時間、液體流速等等項目，來比較模擬結果與實測情形。[^12]

### ANSYS FLUENT

- 北京清大化工系綠色反應工程與技術重點實驗室研究團隊應用FLUENT在最新接觸槽的設計，模擬研究針對向下噴流及中央設置螺旋篩帶之接觸塔設計。[^13]
- Chen and Brooks(2021)使用顆粒速度量測與溶氧電荷法進行圓柱形氣泡塔模場試驗，並運用EFLUENT進行模擬，來預測未來實場的可能情形。[^17]

### 系統/CFD耦合模式

- 雖然這類的組合大多應用在核能反應器的熱傳/質傳模擬，其組合的功能性也提醒我們，CFD可以與任何模式搭配，來完成敏感性分析及預測的任務，也包括AI模型的Digital Twins系統。
- 法國鈉金屬冷卻之快速反應器在2009年除役，在進到下一階段先進鈉技術反應堆工業示範計畫(ASTRID)之前，依據歐洲共同體第七框架計畫之內容，法國展開所謂的熱水力創新系統(The thermal-hydraulics innovative system, THINS)過渡計畫，來驗證系統程式與系統/CFD耦合模式[^9]。選項包括：
  - RELAP(Reactor Excursion and Leak Analysis Program) with **ANSYS-CFX** (FLUENT)[^10]
  - ATHLET with **OpenFOAM**Ⓡ [^11]
  - TRACE with **Star-CCM**

### 氣化反應器

![](https://www.researchgate.net/profile/Jitendra-Carpenter/publication/311865301/figure/fig6/AS:877538121367554@1586232800945/Schematic-representation-of-hydrodynamic-cavitation-HC-reactor.ppm)

- ANSYS-Fluent Tutorial- Waste water treatment by Cavitation Reactor([Engineering Nature(2022)](https://www.youtube.com/watch?v=TYnUH6QrA9s))
- review paper[^33]

## 沉澱池之模擬

- Wang et al., (2022)將Ansys CFX及母數平衡公式耦合在一起，用來模擬實驗室尺寸的膠羽污泥濃縮池，入流速度雖會增加膠羽的持續形成，但也會因增加紊流而破壞重力沉澱，作者經由模式模擬取得最佳的入流速度設計值[^29]。
- 水泥的SPH模擬([Tran-Duc et al., 2021][url34])[^34]

## 消毒系統流場、質傳與反應之CFD相關文獻

### 回顧

- 南佛羅里達大學土木環工系團隊(Zhang et al., 2014)將過去20年來在消毒領域的所有CFD研究進行了回顧，團隊認為依序需要解決的問題是：紊流模式之精進、暫態流、二相或多相流模擬、非均質分布對化學反應機制的影響[^21]。

### 自撰模式

- Bas Anton Wols, (2010)這篇鹿特丹代爾夫特理工大學土木系的博士班畢業論文中，作者針對臭氧與紫外線消毒程序進行了模場與CFD模擬(RANS and LES model)。[^18]
- 英國蘭卡斯特大學團隊(Shah et al., 2021)提出UV系統的CFD模擬結果，研究接觸池幾何形狀與UV劑量的關係，並評估在實場中使用紫外線燈的消毒效果[^19]。

### 圓形噴射加氟混合槽

- CFD Solutions for Water Treatment with Free Surface and Fluorine Jets by [ LEAP Australia(2022)](https://www.youtube.com/watch?app=desktop&v=OOjmYbo--YY)

## 配水系統

### 分水工

- by THINK Fluid Dynamix(2019) [CFD in Water Treatment: distribution chamber(YouTube)](https://www.youtube.com/watch?v=ZI6fhrw8gQQ)
  > Unsteady analysis of flow distribution in distribution chamber in a wastewater treatment plant.
  > Multiphase Volume of Fluid (VOF) simulation.
  > Turbulence Model: SST-Scale Adaptative Simulation
  > ANSYS CFX 2019 R3
  - [公司簡介](https://think-fluid-dynamix.com/about-us/)
    - 德國Erlangen的一家顧問公司，專長在水處理廠的CFD模式模擬，舉凡混合、質傳、沈降分離、水力、變流、水工模型實驗等等。
    - 銷售套裝軟體為[MSTAR](https://think-fluid-dynamix.com/m-star/m-star-validation-and-papers/)。
- by INVENT Umwelt- und Verfahrenstechnik AG(2015)[CFD in water & wastewater treatment: Mixing tanks, tracer(youtube)](https://www.youtube.com/watch?v=IUxX_ksQ9B4)
  - distribution and vertical mixing with upper outflows
  - [公司簡介](https://invent-uv.com/company/history/)：THINK Fluid Dynamix之[控股公司](https://invent-uv.com/invent-worldwide/)，除了德國之外，在義大利、阿拉伯、美國、澳洲也都設有辦公室。主要業務在設計水廠及應用元件，以雙曲面混合器起家，1980年代自弗里德里希-亞歷山大大學之埃爾蘭根-紐倫堡流體力學研究所拆分創立。

## 商業CFD套裝軟體

### Ansys CFX/EFFLUENT

- 官網：[Turbomachinery CFD Software](https://www.ansys.com/products/fluids/ansys-cfx)
- Korpijärvi et al. (2000)[^27]

### MSTAR

- 官網：[THINK Fluid Dynamix](https://think-fluid-dynamix.com/m-star/m-star-validation-and-papers/)

### GPS-X

- 官網：[Hydromantis ESS, Inc.](https://www.hydromantis.com/GPSX-innovative.html)

### water -Gem

- 官網：[bentley.com](https://www.bentley.com/software/openflows-watergems/)

### EPANET

- 官網：[USEPA](https://www.epa.gov/water-research/epanet)

### FLOW - 3D

- 官網：[ FLOW SCIENCE, INC](https://www.flow3d.com/products/flow-3d-hydro/conveyance-infrastructure/)

### Simcenter

- 官網：[ STAR-CCM+ software](https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/)
- 加入SPH(smoothed particles hydrodynamics)=[FloEFD/Star-CCM+](https://www.megaflow.com.tw/simcenter-sph-flow/)

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-08-23-13-28-22.png)

### nanoFluidX

- 官網：[Altair nanoFluidX 2021.2](https://2021.help.altair.com/2021.2/hwsolvers/nfx/topics/getting_started/introduction_nanofluidx_r.htm)
  -  nanoFluidX only runs on Linux systems with CUDA-ready GPU’s. 

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-08-23-13-38-56.png)

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-08-23-13-43-09.png)

## Visualizer

### mixing and dissolve

- Multiphase Fluid Simulations [Two Minute Papers #113](https://www.youtube.com/watch?v=cUWDeDRet4c)

### realtime simulator on UnityHub

- IDE style platform
- [website]()
- Ajay 
  - Coding a Realtime Fluid Simulation in Unity [AJtech(2023)](https://www.youtube.com/watch?v=zbBwKMRyavE&t=24s)
  - Optimizing our Realtime Fluid Simulation in Unity by [AJtech(2023)](https://www.youtube.com/watch?v=9M72KrGhYuE&t=13s)

### visualized using Unity3D/Hololens

- (Berger and Cristie, 2015)[^35], [youtube](https://youtu.be/u35FuLWav3I)

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-08-24-11-49-14.png)

- Computational Fluid Dynamics (CFD) Data Visualization using Hololens by [Marco Losurdo(2016)@youtube](https://www.youtube.com/watch?v=HBYwnGITSEI)
- sersolmaz
  - CFD-CDN-UNITY: Interactive CFD simulations with Unity by [Serkan Solmaz(2022)@github](https://github.com/sersolmaz/CFD-CDN-UNITY)
  - Multiplatform processing of CFD simulations with AR/VR by [Serkan Solmaz(2023)@github](https://github.com/sersolmaz/CFD_AR_VR)
- UnityCFDviewer by [ImperialCollegeLondon(2018)@github](https://github.com/ImperialCollegeLondon/UnityCFDviewer)
- Smoke simulation using Navier-Stokes equations in Unity Engine(SmokeSimulationCFD) by [mwarzech(2020)](https://github.com/mwarzech/SmokeSimulationCFD)
- Simple Unity-fluid-simulation by [gkowash(2023)](https://github.com/gkowash/Unity-fluid-simulation)
- [chrislarkee/ParaView_CFD_To_VR](https://github.com/chrislarkee/ParaView_CFD_To_VR)

### Unity AI

- AI2-THOR: A virtual environment for training home assistant robots[Roozbeh Mottaghi(2021)@Youtube](https://resources.unity.com/ai-ml-content/ai2-thor-session)

### CAD元件

- Browse and download thousands of CAD Drawing files from [CADdetail](https://www.caddetails.com/cad-drawings/mf/water-treatment-equipment). Pollution and Waste Control Equipment -> Water Treatment Equipment
- 看這篇就夠！28 個免費 3D 模型下載、版權使用、資源網站整理 [Eagle 部落格->設計資源](https://tw.eagle.cool/blog/post/best-websites-to-download-free-3d-model-with-high-quality)

## smoothing particle hydrodynamics  

- Coding a Realtime Fluid Simulation in Unity by [AJTech(2023)](https://www.youtube.com/watch?v=zbBwKMRyavE)
  - SPH並不是新的想法，此處以c#介紹coding的過程
  - 2023/7月更新了、更優化的作法(Optimizing our Realtime Fluid Simulation in Unity)[AJTech2023](https://www.youtube.com/watch?v=9M72KrGhYuE&t=609s)

### open source codes on GitHub

uid(year)|repo|language|title
:-:|:-:|:-:|-
sanguinariojoe(2023)|[aquagpusph](https://github.com/sanguinariojoe/aquagpusph)|c++|Free CFD software based on SPH and accelerated with OpenCL
zoziha(2022)|[sph](https://github.com/zoziha/sph)|Fortran|A smoothed particle hydrodynamics (SPH) code
AhmedSalih3d(2023)|[SPHExample](https://github.com/AhmedSalih3d/SPHExample)|Julia|Simple SPH dam-break simulation
johng12(2014)|[cudaSPH](https://github.com/johng12/cudaSPH)|c++|Smoothed Particle Hydrodynamics CFD software parallelized using CUDA
vishalk2(2021)|[CFD-DEM-coupled-Simulations-of-Spherical-Particles](https://github.com/vishalk2/CFD-DEM-coupled-Simulations-of-Spherical-Particles)|C|CFD-DEM coupled simulations of Spherical-shaped particles in a Spouted Bed Dryer using OpenFOAM-5.x and LIGGGHTS.
abhaykamat(2012)|[GodunovSPH](https://github.com/abhaykamat/GodunovSPH)|c++|Integrating a Godunov/Riemann solver with Smoothed Particle Hydrodynamics for Aeronautical, Astronautical and Astrophysical CFD.
Plume-SPH(2020)|[Plume-SPH](https://github.com/Plume-SPH/plume-sph)|c++|A open source solver for modeling volano plume, the numerical method used for solving PDEs is smoothed particle hydrodynamics (SPH).
sim-oy(2022)|[fluid_simulation](https://github.com/sim-oy/fluid_simulation)|c#|CFD SPH
deeptavker(2019)|[shocktube_solver](https://github.com/deeptavker/shocktube_solver)|Python|Simulating the classic sod shocktube using SPH technique
martinjrobins(2014)|[paper_comparison](https://github.com/martinjrobins/paper_comparison/tree/master)|c++|some simulations for SPH-DEM and CFD_DEM comparison paper
jvormann(2018)|[Nek5000-Cubed-Sphere](https://github.com/jvormann/Nek5000-Cubed-Sphere)|Fortran|Create a cubed sphere grid for the Nek5000 CFD Code
farhan4995(2022)|[MovingMultiblock_Sedimentation_Sphere](https://github.com/farhan4995/MovingMultiblock_Sedimentation_Sphere)|C|Simulation of a Sedimentation of Sphere under gravity using Multidomain method of Lattice Boltzmann Method
j8asic(2022)|[isph](https://github.com/j8asic/isph)|c++|(2009-2012) First GPU implementation of Incompressible Smoothed Particle Hydrodynamics (ISPH)

[^1]: Cockx, A., Do-Quang, Z., Audic, J.M., Liné, A., Roustan, M. (2001). **Global and local mass transfer coefficients in waste water treatment process by computational fluid dynamics**. Chemical Engineering and Processing: Process Intensification 40, 187–194. [doi](https://doi.org/10.1016/S0255-2701(00)00138-0)
[^2]: Bieder, U., Maillard, J., Gorsse, Y., Guenadou, D. (2019). **CFD analysis of the flow in the MICAS experimental facility, a water model of the hot pool of a sodium cooled fast reactor.** Nuclear Engineering and Design 350, 67–77. [doi](https://doi.org/10.1016/j.nucengdes.2019.04.033)
[^3]: Cockx, A., Liné, A., Roustan, M., Do-Quang, Z., Lazarova, V. (1997). **Numerical simulation and physical modeling of the hydrodynamics in an air-lift internal loop reactor.** Chemical Engineering Science 52, 3787–3793. [doi](https://doi.org/10.1016/S0009-2509(97)00224-8)
[^4]: Cockx, A., Do-Quang, Z., Liné, A., Roustan, M. (1999). **Use of computational fluid dynamics for simulating hydrodynamics and mass transfer in industrial ozonation towers.** Chemical Engineering Science 54, 5085–5090. [doi](https://doi.org/10.1016/S0009-2509(99)00239-0)
[^5]: Zhao, L., Lu, Y., Lu, D., Tang, Z. (2023). **Modelling for gas-liquid bubbling flow and mass transfer with OpenFOAM.** International Journal of Multiphase Flow 163, 104441. [doi](https://doi.org/10.1016/j.ijmultiphaseflow.2023.104441)
[^6]: Horvath, A., Jordan, C., Lukasser, M., Kuttner, C., Makaruk, A., Harasek, M. (2009). **CFD SIMULATION OF BUBBLE COLUMNS USING THE VOF MODEL - COMPARISON OF COMMERCIAL AND OPEN SOURCE SOLVERS WITH AN EXPERIMENT.** Chemical Engineering Transactions 18, 605–610. [doi](https://doi.org/10.3303/CET0918098)
[^7]: Corzo, S.F., Godino, D.M., Sarache Piña, A.J., Nigro, N.M., Ramajo, D.E. (2023). **Thermal-hydraulic 0D/3D coupling in OpenFOAM: Validation and application in nuclear installations**. Nuclear Engineering and Technology 55, 1911–1923. [doi](https://doi.org/10.1016/j.net.2023.01.001)
[^8]: Corzo, S.F., Godino, D.M., Ramajo, D.E. (2023). **Air circulation study inside and outside of urban buses induced by the opening of windows**. Environ Sci Pollut Res 30, 20821–20832. [doi](https://doi.org/10.1007/s11356-022-23369-y)
[^9]: Pialla, D., Tenchine, D., Li, S., Gauthe, P., Vasile, A., Baviere, R., Tauveron, N., Perdu, F., Maas, L., Cocheme, F., Huber, K., Cheng, X. (2015). **Overview of the system alone and system/CFD coupled calculations of the PHENIX Natural Circulation Test within the THINS project**. Nuclear Engineering and Design 290, 78–86. [doi](https://doi.org/10.1016/j.nucengdes.2014.12.006)
[^10]: Li, W., Wu, X., Zhang, D., Su, G., Tian, W., Qiu, S. (2014). **Preliminary study of coupling CFD code FLUENT and system code RELAP5**. Annals of Nuclear Energy 73, 96–107. [doi](https://doi.org/10.1016/j.anucene.2014.06.042)
[^11]: Herb, J. (2014). **Coupling OpenFOAM with thermo-hydraulic simulation code ATHLET**, in: 9th OpenFOAM Workshop, Zagreb (Croatia).([url]())
[^12]: Bhusare, V.H., Dhiman, M.K., Kalaga, D.V., Roy, S., Joshi, J.B. (2017). **CFD simulations of a bubble column with and without internals by using OpenFOAM**. Chemical Engineering Journal 317, 157–174. [doi](https://doi.org/10.1016/j.cej.2017.01.128)
[^13]: Sayyar, A., Zhang, H., Wang, T. (2023). **Numerical simulation of the hydrodynamics in a novel jet loop bubble column with helical sieve tapes**. Chemical Engineering Science 270, 118491. [doi](https://doi.org/10.1016/j.ces.2023.118491)
[^14]: Ngu, V., Morchain, J., Cockx, A. (2022). **In-depth analysis of reactive bubbly flow using two-way coupled spatio-temporal 1D model.** Chemical Engineering Science 261, 117963. [doi](https://doi.org/10.1016/j.ces.2022.117963)
[^15]: Ngu, V., Fletcher, D.F., Kavanagh, J.M., Rafrafi, Y., Dumas, C., Morchain, J., Cockx, A. (2023). **H2 mass transfer – A key factor for efficient biological methanation: Comparison between pilot-scale experimental data, 1D and CFD models**. Chemical Engineering Science 268, 118382. [doi](https://doi.org/10.1016/j.ces.2022.118382)
[^16]: Li, C., Cui, Y., Shi, X., Gao, J., Lan, X. (2022). **CFD simulation of mass transfer in bubble columns: Detailed study of mass transfer models**. Chemical Engineering Science 264, 118173. [doi](https://doi.org/10.1016/j.ces.2022.118173)
[^17]: Chen, J., Brooks, C.S. (2021). **Experiments and CFD simulation of mass transfer and hydrodynamics in a cylindrical bubble column**. Chemical Engineering Science 234, 116435. [doi](https://doi.org/10.1016/j.ces.2020.116435)
[^18]: Bas Anton Wols (2010). **CFD in drinking water treatment. de Technische Universiteit Delft**, Rotterdam.([pdf](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=f15f95bc8133c72bb54c1d0f2f4466483a4224eb))
[^19]: Shah, J., Židonis, A., Aggidis, G. (2021). **State of the art of UV water treatment technologies and hydraulic design optimisation using computational modelling**. Journal of Water Process Engineering 41, 102099. [doi](https://doi.org/10.1016/j.jwpe.2021.102099)
[^20]: Bridgeman, J., Jefferson, B., Parsons, S.A. (2009). **Computational Fluid Dynamics Modelling of Flocculation in Water Treatment: A Review**. Engineering Applications of Computational Fluid Mechanics 3, 220–241. [doi](https://doi.org/10.1080/19942060.2009.11015267)
[^21]: Zhang, J., Tejada-Martínez, A.E., Zhang, Q. (2014). **Developments in computational fluid dynamics-based modeling for disinfection technologies over the last two decades: A review**. Environmental Modelling & Software 58, 71–85. [doi](https://doi.org/10.1016/j.envsoft.2014.04.003)
[^22]: Wicklein, E., Batstone, D., Ducoste, J., Laurent, J., Griborio, A., Wicks, J., Saunders, S., Samstag, R., Potier, O., Nopens, I. (2015). **Good modelling practice in applying computational fluid dynamics for WWTP modelling**. Water Science and Technology 73, wst2015565. [doi](https://doi.org/10.2166/wst.2015.565)
[^23]: Nopens, I., Laurent, J., Wicklein, E., Ducoste, J., Griborio, A., Batstone, D., Wicks, J., Saunders, S., Potier, O., Karpinska Portela, A., Samstag, R. (2015). **Computational Fluid Dynamics: an important modelling tool for the water sector**, Rotterdam.[pdf](https://www.researchgate.net/publication/301754532_Computational_Fluid_Dynamics_an_important_modelling_tool_for_the_water_sector)
[^24]: Laurent, J., Samstag, R., Ducoste, J., Griborio, A., Nopens, I., Batstone, D., Wicks, J., Saunders, S., Potier, O. (2014). **A protocol for the use of computational fluid dynamics as a supportive tool for wastewater treatment plant modelling**. Water science and technology : a journal of the International Association on Water Pollution Research 70, 1575–84. [doi](https://doi.org/10.2166/wst.2014.425)
[^25]: Samstag, R.W., Ducoste, J.J., Griborio, A., Nopens, I., Batstone, D.J., Wicks, J.D., Saunders, S., Wicklein, E.A., Kenny, G., Laurent, J. (2016). **CFD for wastewater treatment: an overview**. Water Science and Technology 74, 549.[doi](https://doi.org/10.2166/wst.2016.249)
[^26]: Zouboulis, A., Karapantsios, T., Kostoglou, M. (2010). **A CFD-based simulation study of a large scale flocculation tank for potable water treatment**. Chemical Engineering Journal 162, 208–216. [doi](https://doi.org/10.1016/j.cej.2010.05.032)
[^27]: Korpijärvi, J., Laine, E., Ahlstedt, H. (2000). **Using CFD in the Study of Mixing in Coagulation and Flocculation**, in: Hahn, H.H., Hoffmann, E., Ødegaard, H. (Eds.), Chemical Water and Wastewater Treatment VI, Springer, Berlin, Heidelberg, pp. 89–99. [doi](https://doi.org/10.1007/978-3-642-59791-6_9)
[^28]: Chatila, J.G., Danageuzian, H.R. (2022). **PIV and CFD investigation of paddle flocculation hydrodynamics at low rotational speeds**. Scientific Reports 12, 19742. [doi](https://doi.org/10.1038/s41598-022-23935-x)
[^29]: Wang, X., Cui, B., Wei, D., Song, Z., He, Y., Bayly, A.E. (2022). **CFD-PBM modelling of tailings flocculation in a lab-scale gravity thickener**. Powder Technology 396, 139–151. [doi](https://doi.org/10.1016/j.powtec.2021.10.054)
[^30]: Shi, Z., Zhang, G., Zhang, Y., He, T., Pei, G. (2019). **Modeling of Flocculation and Sedimentation Using Population Balance Equation**. Journal of Chemistry 2019, 9187204. [doi](https://doi.org/10.1155/2019/9187204)
[^31]: M Seddighi, D Allanson, G Rothwell, K Takrouri, **Study on the use of a combination of IPython Notebook and an industry-standard package in educating a CFD course**, Computational Applied Engineering Education, 28 (2019) 952-964.
[^32]: 蘇弘毅(2023)以擬 APP 網頁解題工具(DesignSolver)提升環工單元操作課程學生解決設計問題的興趣與能力」(配合課程名稱: 環境工程單元操作實驗)教育部教學實踐研究計畫成果報告PEE1100931([pdf](https://tpr.moe.edu.tw/achievement//upload/banner/20230208/47e86bd63fb74b7eb0fb4482bc553f80/47e86bd63fb74b7eb0fb4482bc553f80.pdf))
[^33]: Hong, F., Tian, H., Yuan, X., Liu, S., Peng, Q., Shi, Y., Jin, L., Ye, L., Jia, J., Ying, D., Ramsey, T.S., Huang, Y. (2022). **CFD-assisted modeling of the hydrodynamic cavitation reactors for wastewater treatment — A review**. Journal of Environmental Management 321, 115982. [doi](https://doi.org/10.1016/j.jenvman.2022.115982)
[^34]: Tran-Duc, T., Ho, T., Thamwattana, N. (2021). **A smoothed particle hydrodynamics study on effect of coarse aggregate on self-compacting concrete flows**. International Journal of Mechanical Sciences 190, 106046. [doi](https://doi.org/10.1016/j.ijmecsci.2020.106046)
[^35]: Berger, M., Cristie, V. (2015). **CFD Post-processing in Unity3D**. Procedia Computer Science 51, 2913–2922. [doi](https://doi.org/10.1016/j.procs.2015.05.476)


[url34]: https://doi.org/10.1016/j.ijmecsci.2020.106046 "Tran-Duc, T., Ho, T., Thamwattana, N. (2021). A smoothed particle hydrodynamics study on effect of coarse aggregate on self-compacting concrete flows. International Journal of Mechanical Sciences 190, 106046."
[doi29]: https://doi.org/10.1016/j.powtec.2021.10.054 "ang, X., Cui, B., Wei, D., Song, Z., He, Y., Bayly, A.E. (2022). **CFD-PBM modelling of tailings flocculation in a lab-scale gravity thickener**. Powder Technology 396, 139–151."
[2]: https://doi.org/10.1016/j.nucengdes.2019.04.033 "Bieder, U., Maillard, J., Gorsse, Y., Guenadou, D. (2019). CFD analysis of the flow in the MICAS experimental facility, a water model of the hot pool of a sodium cooled fast reactor. Nuclear Engineering and Design 350, 67–77. [doi](https://doi.org/10.1016/j.nucengdes.2019.04.033)"
[7]: https://doi.org/10.1016/j.net.2023.01.001 "Corzo, S.F., Godino, D.M., Sarache Piña, A.J., Nigro, N.M., Ramajo, D.E. (2023). **Thermal-hydraulic 0D/3D coupling in OpenFOAM: Validation and application in nuclear installations**. Nuclear Engineering and Technology 55, 1911–1923."
[12]: https://doi.org/10.1016/j.cej.2017.01.128 "Bhusare, V.H., Dhiman, M.K., Kalaga, D.V., Roy, S., Joshi, J.B. (2017). **CFD simulations of a bubble column with and without internals by using OpenFOAM**. Chemical Engineering Journal 317, 157–174. "
[ibis]: https://www.ibisworld.com/united-kingdom/market-research-reports/water-collection-treatment-supply-industry/ "Water Collection, Treatment & Supply in the UK"
[ulf]: https://www.researchgate.net/profile/Ulf-Jeppsson "Lund University->Department of Biomedical Engineering->Ulf Jeppsson"
