---
layout: default
title: 煙流影像來源資料庫
parent: 型態與辨識
nav_order: 99
date: 2023-04-18
last_modified_date: 2023-04-18 22:24:12
tags: YOLO EE AI
---

# 煙流影像來源資料庫

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

## 即時影像

- [](https://tw.live/)
  - [最新天氣觀測](https://tw.live/weather/)
  - 即時影像監視器網站提供台灣各地旅遊景點、市區道路、省道、國道高速公路等 CCTV 閉路電視攝影機即時影像，免費提供民眾隨時查看交通路況、天氣資訊以及旅遊景點人潮狀況以規劃旅行路線。本站影像來源由交通部、高公局、公路總局、各地縣市政府、國家公園風景區以及警廣即時路況等資料庫提供。© Copyright 2023 即時影像監視器 All rights reserved.
- 台灣即時影像監視器[twipcam](https://www.twipcam.com/cam/n5-s-28k+235)

```html
<div class="w3-content" style="max-width:100%;">
<img data-src="https://cctvp02.freeway.gov.tw/mjpeg/X01001612900101" 
src="https://cctvp02.freeway.gov.tw/mjpeg/X01001612900101?t=0.15996061836920883" 
onerror="this.src='/img/connect-error.jpg';" 
alt="國道5號 28K+235 坪林交控交流道到頭城交流道" class="video_obj" 
style="width:100%;max-height:600px;" 
onclick="open_full_image();">
```

### 觀光局4K影像
- 高雄觀光局4K及時影像[旗津海水浴場即時影像](https://youtu.be/ka7FV0sCvxQ)

![](https://github.com/sinotec2/Focus-on-Air-Quality/raw/main/attachments/2023-09-18-15-27-41.png)

[蓮池潭小龜山](https://www.youtube.com/watch?v=dCycHSYZBmg)
![](https://github.com/sinotec2/Focus-on-Air-Quality/raw/main/attachments/2023-09-18-15-51-56.png)

[高雄壽山情人觀景台](https://www.youtube.com/watch?v=C03Itx8iSC0)
![](https://github.com/sinotec2/Focus-on-Air-Quality/raw/main/attachments/2023-09-18-16-10-20.png)

- [台中高美濕地](https://www.youtube.com/watch?v=fjhg3gAnMFg)
![](https://github.com/sinotec2/Focus-on-Air-Quality/raw/main/attachments/2023-09-18-16-27-54.png)

## Youtube

- 工安空汙頻遭詬病 高雄林園、臨海工業區明年總體檢  [公視晚間新聞(20211029)](https://www.youtube.com/watch?v=QTAhFPTZd5U)
- 林園工業區夜間空拍縮時錄影 by [丞佳魚貨(2019年11月11日)](https://youtu.be/n9JAHc8fw_Q?si=Vtk38Fdz5q2U4Udk)

## 照片定位

- 李祈德及洪淑瑜(2010)利用數位照片定位系統建構地理資料庫應用於森林資源經營管理。[台灣林業 九十九年 六月號](https://www.forest.gov.tw/MagazineFile.aspx?fno=5748)
  - 林務局自2008年開始執行的第4次全國森林資源調查，利用調查人員每3公里系統間隔設立地面樣區之際，以GPS建立軌跡及以數位相機大量拍攝行經地點特殊林相、野生動物、水源地及崩塌地等照片。採用RoboGEO系統串聯GPS與數位照片，使照片具有空間資訊，再應用Opanda軟體編輯照片之EXIF（EXchangeable Image File Format），註記相關資料。此法雖可將照片定位，但過程需搭配多項軟體才能達到繳交資料標準。為此，林務局南投林區管理處於執行該調查之初即發展「數位照片定位系統」，以有效率的比對數位照片與GPS軌跡時間及編輯EXIF資訊，同時可迅速整理調查資料，並產製可供各項業務使用之圖資，作為建構轄區內地理資料庫之基礎。
- 林士哲()相片拍攝之位置、方位記錄與GIS的應用。[中央研究院計算中心通訊電子報](https://ndaip.sinica.edu.tw/content.jsp?option_id=2621&index_info_id=1544)
- 臺灣百年寫真／GIS資料庫(限制瀏覽) by [漢珍數位圖書股份有限公司](http://www.tbmc.com.tw/chinese_version/taiwandata/taiwan_20.html)
  - 漢珍數位圖書董事長朱小瑄表示，這套資料庫收集一八九五到一九四五年間兩萬五千張老照片。照片主要來源是日據時代出版的寫真帖（攝影集）、書籍配圖與風景明信片。
  - 照片蒐集完成後，再聘請專業編輯撰寫圖文詮釋、整理地圖，再與中央研究院地理資訊科學GIS研究中心團隊合作，將每一張照片內容查到其經緯度座標後，以軟體設計內嵌於GIS（地理資訊系統）上。讀者可在不同時期的地圖上點選，呈現圖文並茂的數位資源。
- 數位典藏與數位學習國家型科技計畫([2002~2013](https://teldap.tw/index.html))


- 台灣創新技術博覽會 by 國家科學及技術委員會(國科會)、中央研究院、教育部、衛生福利部
  - 空氣汙染快速分析儀及汙染來源分佈系統 by [國立臺灣師範大學](https://www.futuretech.org.tw/futuretech/index.php?action=product_detail&prod_no=P0008700005436)
