---
layout: default
title: GCN+LSTM
parent: 時空數據之解析及訓練
nav_order: 99
date: 2023-05-26
last_modified_date: 2023-05-26 15:11:27
tags: ML DL EE CMAQ WRF
---

# GCN+LSTM

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

## METR_LA analogue ressults

- Forecasting using spatio-temporal data with combined Graph Convolution + LSTM model, [ StellarGraph demos](https://stellargraph.readthedocs.io/en/stable/demos/time-series/gcn-lstm-time-series.html)
- [ipynb](https://github.com/sinotec2/FAQ/raw/main/_posts/2019ncHrGrid.ipynb)

### 數據特性之比較(Graph components)

- 圖形(節點、邊緣、加權等)為靜態、節點特徵值則為動態
- 單一特徵

項目|METRO_LA|2019.nc_NO2|說明
-|:-:|:-:|-
|data source|LA交通局數據|2019.nc CMAQ公版模式背景濃度模擬結果|
節點|速度監測站點|島內各網格點|前者較少、後者較多
特徵值|交通速度|空氣污染濃度值|分部有顯著差異(詳下)
時間頻率特徵|每5分鐘一筆|每小時一筆
邊緣加權|站點間的距離(作為邊緣的加權量)|網格點間距離<sup>-0.25</sup>|

### parameters

項目|METRO_LA|2019.nc_NO2|說明
-|:-:|:-:|-
seq_len|10|72|
pre_len|12|24|
gc_layer_sizes|[16, 10]|[16, 72]|
gc_activations|relu|relu|
lstm_layer_sizes|[20, 10]|[20, 72]|
lstm_activations|tanh|tanh|
epochs|100|200|
batch_size|60|60|
MASE|0.698|0.650|同一數量級

### Loss/MSE during training

|![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-05-26-14-29-42.png)|![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-05-26-14-30-33.png)|
|:-:|:-:|
|<b>METR_LA速度預報訓練</b>|<b>2019.nc_NO2</b>|

### Distribution over segments

- speed training and testing results
  - training及testing都是扁胖形分布、訓練組更胖一些。表示原始數據可以符合高斯分布，並沒有顯著的極端值。訓練組的符合度更好一些。
  - 測試組之模擬誤差略為偏低

|![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-05-26-13-46-53.png)|![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-05-26-13-46-00.png)|
|:-:|:-:|
|<b>METR_LA速度預報測試結果</b>|<b>2019.nc_NO2</b>|

- NO2
  - 原始數據與高斯模式的符合度不高。訓練及測試組皆然。(空氣品質的分布特性為對數高斯分布。)
  - training及testing都有強烈的趨中性質
  - 二者的平均絕對誤差值還蠻接近的
  - 測試組之誤差略為偏低

### all test result visualization

- speed predictoins

|![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-05-26-13-37-22.png)|![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-05-26-13-40-59.png)|
|:-:|:-:|
|<b>METR_LA速度預報測試結果</b>|<b>2019.nc_NO2(部分值)</b>|

- NO2 predictions
  - 可以抓到日變化的趨勢
  - 對高值毫無預測能力。還需借助於其他模型、如
    1. 預先分類再予訓練

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-05-26-13-43-21.png)

## 程式設計重點說明

### 台灣島多邊形之讀取

- 使用[Voronoi](https://sinotec2.github.io/Focus-on-Air-Quality/utilities/GIS/Voronoi/)作業過程中的半成品

```python
import geopandas as gpd
root='/nas2/cmaqruns/2022fcst/fusion/Voronoi/'
boundary=gpd.read_file(root+'boundary_shape.shp')
boundary_shape = boundary.geometry[0]
```

### 島內格點的篩選

- 此處使用shapely.geometry.Polygon.within函數
- 先篩出符合的點的名稱標籤(`name`)
- DataFrame.loc中設定boolean將原來資料表篩減，減省至少2/3。

```python
x1d=[nc.XORIG+nc.XCELL*(i+0.5) for i in range(ncol)]
y1d=[nc.YORIG+nc.YCELL*(i+0.5) for i in range(nrow)]
X,Y=np.meshgrid(x1d,y1d)
X,Y=X.flatten(),Y.flatten()
lons, lats= pnyc(X,Y, inverse=True)
pnts=[Point(lon,lat) for lon,lat in zip(lons,lats)]
dfNod=pd.DataFrame({'geometry':pnts,'name':[str(i) for i in range(NM)]})

name_inside=dfNod.loc[dfNod.geometry.map(lambda p:p.within(boundary_shape)),'name']
...
s=set(name_inside)
n=len(s)
dfNod2=dfNod.loc[dfNod.name.map(lambda x:x in s)].reset_index(drop=True)"
```

### 網格點兩兩距離之計算

- 這個問題如果用迴圈來設計，將會是一個災難。
  - 用shapely.geometry.Point.distance函數、完全沒有幫助
  - 即使計算對角線上(或下)一半，在映射到另一半，可以減省一半的計算時間，還是沒有太大的幫助。
- 可以利用**None維度的技巧**，來重複2維矩陣中特定的一個部分。(參[矩陣階層numpy.newaxis(None)的用法](https://sinotec2.github.io/Focus-on-Air-Quality/utilities/netCDF/MatrixRankNone/))
- 下列程式段落中的n即為網格點個數，因為是計算兩兩距離(d)，因此d的維度是2維，大小都是n。
  - 預先將網格點X、Y值處理成1維向量，其長度為n
  - `X,Y=np.array(dfNod2.X),np.array(dfNod2.Y)`
- 設定終點為第0個維度、起點則為第1個(另一個)維度
- 用矩陣標示法直接計算這個d[n,n]的方法，就是定義相對應的終點(X1,Y1)與起點(X2,Y2)，進行差值計算、取平方、相加、再取根號。
  - `d[:,:]=np.sqrt((X1-X2)**2+(Y1-Y2)**2)`
  - 因此X1、X2、Y1、Y2的形狀，也必須完全與d相同
  - 先予以填充0值，預留記憶體(空的容器)。
- 起點為第0個維度，因此X1、Y1第0個維度的內容必須完全與X,Y相同，另一個維度則複製即可。此處以None將向量複製擴張成矩陣。
- 同理應用在終點(X2、Y2)，維度設定與起點(X1、Y1)相反即可。
- 交錯寫法，是因為複製、貼上、將X改成Y，是最快的編輯方式

```python
d=np.zeros(shape=(n,n))
X1=np.zeros(shape=(n,n))
Y1=np.zeros(shape=(n,n))
X2=np.zeros(shape=(n,n))
Y2=np.zeros(shape=(n,n))
X,Y=np.array(dfNod2.X),np.array(dfNod2.Y)
X1[:,:],X2[:,:]=X[:,None],X[None,:]
Y1[:,:],Y2[:,:]=Y[:,None],Y[None,:]
d[:,:]=np.sqrt((X1-X2)**2+(Y1-Y2)**2) #dfNod2.geometry[j].distance(dfNod2.geometry[i])        
#for j in range(n):
#    for i in range(0,j):
#        d[j,i]=d[i,j]
```

### 加權的計算

- 原範例是用交通速度測點間的距離來加權，距離越大的路段速度會越快，加權越重。通過2個測點的速度比較容易相近(車輛運動的慣性物理性質)，越近的測點，車速會降低，加減速的敏感性就越高(作者認定的模型)。
- 此處空氣品質則相反，距離越遠的點差異可能就越大，越相近的點差異會越小。因此使用距離的倒數來加權
- 同一點的距離為0，倒數無意義，且不能參與取極值過程。因此取倒數後直接令其為1(足夠小的暫定值)。
- 取極值之後，再將對角線值全都設為最大值，再除以此最大值，以使最大值為1。
- 取0.25次方的用意是讓空間上的漸變過程趨緩一些

```python
d=1/d*1000.
for j in range(n):
    d[j,j]=1.
dmax=d.max()   
for j in range(n):
    d[j,j]=dmax
d=np.sqrt(np.sqrt(d/dmax))
```
