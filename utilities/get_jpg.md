---
title: 環境部測站逐時照片之下載
tags: AI
layout: default
parent: Utilities
date:  2023-09-26
modify_date: 2023-09-26 14:45:42
---

# 環境部測站逐時照片之下載
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

## 背景說明

- 此處挑了環境部測站其中的8站，逐時(每10分鐘)下載其周邊照片。
- 測站的選擇、位置、照片的角度方向等等，詳[煙流影像來源資料庫](https://sinotec2.github.io/AIEE/Identify/FilmSources/)的說明。

## 腳本設計

### 8站的編號與站名

- 站別為第1迴圈。
- 站名為目錄`$stn`。
- 站號為前3碼(`$s`)，用在檔名的標示
- 先對該站目錄下所有檔案進行ls，因檔名按照時間編排，所以最後一個檔案的名稱會有最後一個時間(`$LASTHR`)的資訊。
- 在從其中讀取日期與小時

### 小時迴圈

- 為增加腳本的彈性，以適用在停機、斷線等等突發情況，此處不以固定時數為設計，而是一個永動的迴圈。
- bash的date指令只接受日期為基準的加減計算，因此殘餘的小時數(起始值)必須先加回去。而以如果存在即跳開作法來規避重複下載。
- 先計算年(`$y`)、日期(`$ymd`)以備開啟目錄。
- 年月日時(`$ymdh`)則為檔名的一部分。
- 如果時間到了目前時間(`$crnt`=current)，則跳開永動迴圈，進入下一測站之測試與下載。

### 分鐘迴圈

- 測站不見得有(每10)分鐘的拍攝，但此處仍設計有迴圈。
- 如果檔案不存在，即以`wget -T`方式減少無信息的停等(time out)。

## crontab

### 執行頻率

- 因程式設計如工作站磁碟機上不存在檔案，才會開始下載。因此即使以較高頻率來執行，也不會發生重複下載的情況。
- 可以日、時、或每10分鐘執行，皆可。

### 週間與周末差異頻率

- 週間工作時間:每10分鐘檢查下載
- 其他日與時間：每小時

```bash
# perform downloading the photgraphs from 8 EPA stations
# working day and hour
*/10 7-20      * * 1-5 /nas2/kuang/img_sources/EPA/get_jpgHourly.cs >& /nas2/kuang/img_sources/EPA/get_jpgHourly.out
0    0-6,21-23 * * 1-5 /nas2/kuang/img_sources/EPA/get_jpgHourly.cs >& /nas2/kuang/img_sources/EPA/get_jpgHourly.out
## weekend hourly
0 * * * 6-7 /nas2/kuang/img_sources/EPA/get_jpgHourly.cs >& /nas2/kuang/img_sources/EPA/get_jpgHourly.out
```

## Things TODO

- 以web形式提供歷史與即時影像的瀏覽
  - 環境部目前提供單一測站影像、因此同一主題的多站顯示應會是個好主意
  - 歷史圖片的選擇、播放
- 煙流的YOLO解析
- 解析結果與其他環境資訊的連結
  - 煙流走向與風向、煙流高度與混合層、
  - 煙流長度、顏色與PM2.5濃度、相對溼度、能見度等的關係
  - 蒸氣與flare活動、CEMS等的關聯
- 煙流活動與其他活動量如船運、卡車交通等等之關聯

## 程式碼

```bash
root=/nas2/kuang/img_sources/EPA
http="https://airtw.moenv.gov.tw/AirSitePic"
crnt=$(date +%Y%m%d%H)
stns=( "029shalu" "041taixi" "051daliao"  "052linyuan"  "054zuoying"  "058xiaogang"  "060chaozhou"  "085dacheng" )
for si in {0..7};do
  stn=${stns[$si]}
  s=$(echo $stn|cut -c-3)
  LASTY=$(ls  $root/$stn |tail -n1)
  fls="$root/$stn/$LASTY/*/*"
  LASTHR=$(ls  $fls |tail -n1|rev|cut -d'/' -f1|rev|cut -d'-' -f2|cut -c-10)
  LAST=$(echo $LASTHR|cut -c-8)
  h=$(echo $LASTHR|cut -c9-10)
  while true;do
    y=$(date -d "$LAST +${h}hour" +%Y)
    ymd=$(date -d "$LAST +${h}hour" +%Y%m%d)
    ymdh=$(date -d "$LAST +${h}hour" +%Y%m%d%H)
    for m in {0..5}0;do
      fn=${s}-$ymdh${m}.jpg
      path=$root/$stn/$y/$ymd
      mkdir -p $path;cd $path
      if ! [[ -e $fn  ]];then
        wget -T 10 -q $http/$ymd/$fn;fi;done
    if [[ $ymdh -ge $crnt ]];then
      break;fi
    h=$(( $h + 1 ));done;done
```

