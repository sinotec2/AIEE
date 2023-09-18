---
layout: default
title: 目測判煙、影像分析之自動及智慧化
parent: 型態與辨識
nav_order: 99
date: 2023-07-06
last_modified_date: 2023-07-16 19:26:55
tags: python matplotlib AI
---

# 目測判煙、影像分析之自動及智慧化

## 背景

### 研究著眼點

- 雖然台灣地區煙囪或車輛排冒大量煙流的情況已經不多了，然而也正是因為如此，仍然存在著下列的問題與契機:
  - 因污染源、污染行為已經越來越少，如何建立有效的監管制度、穩定之實時監測系統、可避免費時費工之人工監看，同時又能掌握污染源之不定期排放?
  - 除了管道排放之外，還存在著逸散性之污染活動、零星短暫之排放行為，還需要持續強化管制。
  - 如何將自動化系統納入工安管理制度
  - 世界上還是有其他開發中國家需要這項低成本的管制技術
  - 從被動之接受陳情才出動管制，轉成積極性之污染輔導與究查。
  - 火災之智慧化偵測及管理已漸趨成型，有許多的軟件可供參考應用。個別方法在特定個案中表現如何?如何選擇?

### 回顧性文章

- [Chaturvedi et al.(2022)][doi1][^1]這篇宣稱最先驅的文獻回顧，將271篇有關煙流的智慧化監測文獻分成：煙流分類、切割、以及框線範圍訂定等3個段落程序進行分析討論。
  - 分析方式：包括了傳統的畫面分析處理、機器學習、以及深度學習等3大類。
  - 影像來源：則包括無人飛機、衛星影像、森林定點攝影、以及一般的風景攝影等等。
- [(Grant-Jacob and Mills, 2022)][doi13]將所有粒狀物偵測、辨識、預報、以及推論等等AI應用，做了下圖之整合說明。除了視覺的偵測之外，文中也整合了目前所有粒狀物的其他偵測方式，甚至包括了鏡檢之智慧辨識。[^13]

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-07-15-23-28-20.png)

- 中國蘇州大學團隊[Khan et al., 2022][doi2][^2]認為目前的火災偵防仍然須面臨降低誤報、提高靈敏度與反應性、對高價且複雜的設施提共更加保護等等難題。該回顧論文也針對最近的智慧化偵測提供了不少的解析。

## 工廠煙流偵測

- [呂承恩, 2022][url5]除了用YOLO4進行影像的辨識、分框，分框後的煙流影像則以kmeans法進行叢集，以建立與林格曼色盤之間的關聯性。[^5]
- [**分水嶺分割法**](#wssa)是連續分布影響數位化的重要方式之一，常用在光學檢測、圖像分析、醫學像處理等領域，鄭州技術學院團隊[(Ju and Wang, 2022)][doi6]將其應用在工業煤煙之FCN (fully convolutional network)機械辨識系統之中。[^6]
- 影像分析
  - 煙流辨識的目的在取代目測判煙，因此除了標示煙流之外，還必須要能夠較林格曼色盤更佳的定量鑑別能力。這篇來自西班牙阿斯圖里亞斯奧維多大學團隊[(Pedrayes et al., 2023)][doi7]的研究，建立了背景藍光百分比法(SBPB，Sky and Building Percentiles in the Blue channel.)，除了透光度，也將煙流與背景的**色度**應用在影像定量分析，特別對逸散源煙流的解析有其穩定、客觀之優點。這篇雖然沒有應用神經學習方法，但其影像分析技術可供未來自動化監測的重要參考。[^7]
  - 中國科學院大氣物理研究所大氣邊界層物理與大氣化學國家重點實驗室[Feng et al., (2020)][doi11]這篇研究不是將人工智慧應用在煙流辨識，而是應用在地面PM<sub>2.5</sub>空品濃度對煙流形狀特徵關係的機械學習。除了數位光學相機之外，團隊還應用了光達進行煙流垂直面的影像掃描。經樹狀邏輯解析之後，篩選出煙流長度與地面PM<sub>2.5</sub>濃度有最高的相關性。[^11]
- **煙流上升高度**一般只是個煙囪條件、出口處的氣溫風速相對濕度等等氣項因素的函數推估值，如高斯煙流及網格模式中的計算模組，但對於敏感族群的呼吸健康防護、地面污染成因複雜、或鄰近濱海、複雜地形中的空氣品質監測、預警預報等等，即時監測有其必要性。對於發展更新煙流上升計算模組，也是重要的數據來源。為此，來自多倫多大學[Koushafar et al.(2023)][doi8]所提出的深度學習會是一項有效的解析工具。[^8]
- 鄭州科技大學團隊[(Li et al., 2023)][doi9]將"Generative adversarial network"(生成對抗網絡、GAN、見[ChatGPT說明](#GAN))應用在工業**煙流複雜情況**之辨識，包括背景雲量干擾、大小差異煙流、低濃度煙流、同時多煙流等地辨識解析[^9]

## 車輛煙流排放偵測

- 一般的煙流辨識軟件應用在車輛尾器與執法上，還有很大的鴻溝：
  1. 要能夠排除背景雜訊(霧氣、車輛本身的陰影、背景道路人孔蓋、水塘、污漬等等)、並建立明確且客觀的定量方式。不能只是辨識。
  2. 計算速度必須夠快，才能執行線上執法
  3. 車輛出力(速度與荷重)與煙流有密切的關連，執法上需有一定的標準，還需要校正。

- [洪詮盛, 2021][url4]這篇論文雖然來自於資工所，對影像的除霧、辨識有所貢獻，文中也對煙流的色度進行解析與記錄，可供進一步建立模型與執法使用。[^4]
- 深圳技術大學大數據與互聯網學院
  - [Peng et al.(2022)][doi10]使用3DCNN(YOLO5tiny)分別辨識車輛與煙流，按照最近距離將此二者配對，[^10]
  - [Chen and Peng(2023)][doi3]匯集了3962個已標車輛註煙流之圖檔資料庫，並公開在[google drive](https://drive.google.com/file/d/1Rt3IEKkriDNQ9wRtpsK5fylvfRlTjjK3/view?usp=share_link)。該文也將過去圖框型態提升到網格化多邊形標示，除了標示作用，也具有發展半定量排放推估模型的潛力。 [^3]
- 實作:[Abonia Sojasingarayar(2023)](https://github.com/Abonia1/YOLOv8-Fire-and-Smoke-Detection)

- ![](https://github.com/sinotec2/FAQ/raw/main/attachments/yt5s.io.mp4)

## 夜間或IR影像之辨識

基本上路徑有2
1. IR或夜視影像直接用以訓練、既有資料庫轉標籤、再用以訓練
2. 直接用夜間可見光照片、以特殊方式來訓練

### IR或夜視影像之訓練

- 4 classes(car, bicycle, person, dog) by **NIGHT OBJECT DETECTOR, PyTorch and YOLOv5, FLIR THERMAL IMAGES dataset**[(youtube)](https://www.youtube.com/watch?v=yo_ryIS_XYQ)
- 11 classes by [ax2mazhr/FLIR2YOLO](https://github.com/ax2mazhr/FLIR2YOLO)
  - convert the labels of FLIR dataset (https://www.flir.eu/oem/adas/adas-dataset-form/) to YOLO
  -  ['person','bike','car','motor','bus','train','truck','light','dog','scooter','other vehicle']
- 北大團隊Jiang et al., (2022)使用地面紅外線影像進行訓練，並將模型運用在UAV上，最小化模型為YOLOv5s、人與車辨識準確率可達 88.69%。[^27]
- [Human Detection in Heavy Smoke Scenarios](https://encyclopedia.pub/entry/25832)這篇發展在火場或其他災難現場煙霧中的人員辨識系統(動態深度傳感器、夜視、IR、FLIR、LIDAR、雷達、聲納等等之訊號)。作者來自陽明交大資科系(Tsai et al., 2022)[^28]
- 弗吉尼亞理工大學(Kim and Lattimer, 2015)發展了火場中自走搜尋機械設備上的火苗與煙氣辨識系統，並以IR影像進行類神經網路訓練。[^29]
- 香港理工大學及北京石油大學團隊(Shi et al., 2020)以Faster R-CNN發展出實時洩漏監測系統，應用在乙烷裂解工場，所建立之模型經證實較[多框單次檢測](#SSD)為優秀。文中發現加深物件萃取器的深度及參數並不會大幅增加正確率，反而會降低分辨速率。[^33]理工大學團隊也參與在海下氣管洩漏的偵測[^34]，證實Faster R-CNN比YOLOv4更能辨識水下洩漏之氣團。

### 一般影像之特殊訓練

- 約旦扎爾卡大學資訊學院團隊(Al-Smadi et al., 2023)將影像區分為日間及夜間(並沒有使用夜視或IR影像)、按照不同遠近程度先行分類再與訓練，對於野火初期煙流有較佳的辨識。[^30]
- 韓國啟明大學團隊(Park and Ko, 2020)發展了火災發生過程的時序影像(fire-tube)的訓練方式，除了靜態的YOLO之外也使用了LSTM來進行訓練，針對夜間視線不佳條件下的都市火災有較佳的辨識效果。[^31]
- 來自廣西大學團隊(Sun and Feng, 2023)建立了移動注意力焦點與自由錨定機制，來規避夜間錯誤的辨識結果，提高夜間煙流及火災的成功辨識機率。[^32] 

### 商用案例

- Real-time Pipeline Leak Detection & Perimeter Intrusion Detection System by [IntelliView](https://youtu.be/YZ0d5n_dsHo)


## 不特定對象影像分析之智慧化

### 香港中文大學

2021～2022這3篇來自中文大學地理資源管理系的論文，先建立手機影像與衛星影像粒狀物的散光特性以及濃度的特性後，再從公開爬取的網路照片中，建立更廣泛的對照資料庫，應用機器學習來推估粒狀物的即時空氣品質。[^16] [^17] [^18]。

### 西北師範大學資科工系

這2篇論文以特定點、特定景物的連續照片與粒狀物濃度對照資料庫，訓練人工神經網路，用於其他沒有測站位置（廣大鄉村範圍）、即時空氣品質的監測。[^14]  [^24] 

### 台大團隊

生工系張斐章教授團隊以林園工業區的煙流影像與地面測站粒狀物空氣品質、AQI等3549組逐時數據庫進行機械學習與類別回歸。[^23]

### 其他

- 赫爾辛基大學理學院[Su et al., 2022][doi15]宣稱他們發展的技術可以同時從數值影像中提取粒狀物（包括PM2.5及PM10）、相對濕度、溫度、能見度等等環境參數資訊，並且不因為影像的對象、範圍尺度而造成很大的差異，表現優於傳統CNN方法如AlexNet, [ResNet-50](#resnet-50), 及DenseNet-121，數據庫、程式以及測試結果公開在[github](https://github.com/cvvsu/RMEP)。[^15]
- 南京師範大學地理學院[Wang et al., 2022][doi19]這篇也使用多參數的影像學習，包括PM2.5及相對濕度、偵測月份等等，影像來自上海地區不同時間、不同位置的影像。[^19]
- 這2篇中國地質大學與巴基斯坦奎德-埃-阿瓦姆工程、科學與技術大學合作的論文以巴基斯坦卡拉奇市的影像與AQI進行深度學習，發展出AQE-Net方法，應用在第三世界監測站設施不足地區。 [^20] [^22]
- [^21]這一篇印度的文章以北京的影像來進行訓練與實驗。
- 孟加拉達卡布拉克大學這篇研討會海報宣稱他們的方法達到較傳統[ResNet-50](#restnet-50),VGG19更快速的辨識時間與更高的準確率。[^26]

## Notes from ChatGPT

### WSSA

> 人工智能領域中"watershed segmentation algorithm "所指為何?

在人工智能领域中，"watershed segmentation algorithm" 指的是分水岭分割算法。这是一种基于图像处理的分割方法，用于将图像中的目标或区域分离出来。

分水岭算法基于图像的灰度或颜色信息，将图像看作地势表面，其中亮度或颜色较高的区域对应于山峰，亮度或颜色较低的区域对应于山谷。算法的目标是在图像中找到这些山峰和山谷，然后通过在山谷之间建立分割边界来将图像分割成不同的区域。

分水岭算法的步骤通常包括以下几个阶段：

1. 预处理：对图像进行必要的预处理，例如平滑、滤波、梯度计算等，以便提取有用的特征。
2. 确定标记：通过对图像进行阈值分割或使用其他分割算法，确定前景和背景区域，并对其进行标记。
3. 计算距离变换：基于标记的位置和强度信息，计算图像的距离变换，得到表示图像区域与标记之间距离的图像。
4. 寻找分水岭：通过计算图像的梯度或变换，确定图像中的潜在分水岭位置，这些位置是山峰和山谷的边界。
5. 分割图像：基于找到的分水岭位置，通过建立边界来分割图像，将图像分成不同的区域。

分水岭分割算法在图像分割和计算机视觉任务中广泛应用，可以用于对象检测、图像分析、医学图像处理等领域。它能够有效地分割具有复杂形状和不规则边界的目标，并具有一定的鲁棒性和灵活性。然而，分水岭算法也存在一些挑战，例如对噪声和边缘连接的敏感性，以及在某些情况下可能产生过分分割的问题。因此，根据具体应用场景和图像特点，需要进行适当的参数调整和后处理来改善算法的效果。

### RestNet-50

> 介紹AI領域的ResNet-50方法

ResNet-50 是深度学习中一种经典的卷积神经网络（Convolutional Neural Network，CNN）架构，它属于 ResNet（Residual Network）系列模型的其中一种。

ResNet-50 的主要贡献是引入了残差连接（residual connections）的概念，以解决深层神经网络训练中的梯度消失和梯度爆炸问题。这种残差连接允许信息直接跳过某些层级，从而使网络能够更轻松地学习和优化深层网络结构。

以下是 ResNet-50 的一些关键特点和结构：

1. 残差块（Residual Block）：ResNet-50 由多个残差块组成。每个残差块中包含了多个卷积层、批归一化层和激活函数。残差块中引入了跳跃连接，将输入的特征映射直接加到输出中，使得神经网络能够更好地优化和训练深层结构。
2. 卷积层和池化层：ResNet-50 使用了一系列的卷积层和池化层，以提取输入图像的特征。其中卷积层使用了不同的卷积核尺寸和通道数，以捕捉不同尺度和抽象层次的特征。
3. 全局平均池化层：在最后的残差块之后，ResNet-50 使用全局平均池化层将特征图转换为向量。这样可以减少参数数量，并将特征表示压缩成固定长度的向量。
4. 全连接层和分类器：在全局平均池化层之后，ResNet-50 通过一个或多个全连接层来实现最终的分类器。通常，最后一层是一个具有预定义类别数的 softmax 层，用于进行图像分类任务。

ResNet-50 在计算机视觉任务中表现出色，特别是在图像分类和目标识别方面。它可以处理具有大量类别的复杂数据集，并具有较低的过拟合风险。由于其深层结构和残差连接的引入，ResNet-50 在准确性和特征表示方面具有优势，使其成为许多视觉任务中的首选模型之一。

对于使用 ResNet-50 进行图像分类任务，你可以使用预训练的模型权重，并根据你的数据集进行微调（fine-tuning）或迁移学习（transfer learning）。

### GAN

> "Generative adversarial network"在資料科學中的原理與應用為何？

生成对抗网络（Generative Adversarial Network，GAN）是一种深度学习模型，由生成器（Generator）和判别器（Discriminator）组成。GAN 的原理是通过生成器和判别器之间的对抗训练来生成逼真的样本数据。GAN 的工作原理如下：
- 生成器（Generator）接受一个随机噪声向量作为输入，并尝试生成与训练数据相似的样本数据。
- 判别器（Discriminator）接受样本数据（来自训练数据或生成器生成的数据）作为输入，并尝试区分出真实样本和生成样本。
- 生成器和判别器通过对抗训练相互竞争。生成器的目标是生成尽可能逼真的样本以欺骗判别器，而判别器的目标是准确地识别真实样本和生成样本。

在训练过程中，生成器和判别器通过反复迭代来提高性能。生成器通过学习从随机噪声向量到逼真样本的映射，而判别器通过学习区分真实样本和生成样本。
通过这种对抗性的训练过程，生成器逐渐改进生成的样本，使其更接近真实样本的分布。最终，生成器可以生成具有高度逼真性质的样本数据。
GAN 在数据科学中有许多应用，包括：
- 图像生成：GAN 可以生成逼真的图像样本，例如生成人脸、动物图像、艺术作品等。它可以用于图像增强、数据增强、虚拟现实等领域。
- 数据合成：GAN 可以生成合成的数据样本，用于数据集的扩充和增强。这对于数据稀缺的情况下进行训练非常有用。
- 超分辨率图像重建：GAN 可以通过学习低分辨率图像与高分辨率图像之间的关系，实现图像的超分辨率重建。
- 生成文本和音频：GAN 可以生成逼真的文本段落、对话和音频样本，用于自然语言处理和语音识别等任务。
- 强化学习：GAN 可以与强化学习结合，用于生成与环境交互的智能体的样本数据，以提高强化学习模型的性能。

尽管 GAN 在生成逼真样本方面取得了重要进展，但训练 GAN 模型仍然具有挑战性，例如模式崩溃、模式塌陷和训练不稳定等问题。然而，随着技术的不断发展，GAN 在数据科学中的应用前景仍然非常广阔。

### SSD

> Single Shot Detection為何?

Single Shot Detection (SSD) 是一种用于目标检测的深度学习模型，它是一种基于单一网络的端到端目标检测算法。SSD 的主要特点是能够实现实时的目标检测，并且在保持高准确率的同时具有较快的速度。

SSD 的核心思想是将目标检测问题转化为一个回归问题和一个分类问题。SSD 使用卷积神经网络来同时预测图像中目标的边界框（Bounding Box）和对应的类别概率。

SSD 的主要步骤如下：

特征提取：首先，SSD 使用一个预训练的卷积神经网络（通常是 VGG 或 ResNet）来提取输入图像的特征。这些特征图通常包含了不同尺度和抽象层次的信息。

多尺度特征图：SSD 在多个不同层级的特征图上进行检测。通过在不同层级的特征图上应用不同尺寸的卷积核，可以在不同尺度下检测目标。

预测边界框和类别：在每个特征图上，SSD 使用卷积层来同时预测每个位置的目标边界框的位置（回归问题）和每个目标类别的概率（分类问题）。

Non-Maximum Suppression (NMS)：为了避免多个重叠的边界框预测，SSD 使用 NMS 过滤掉高度重叠的边界框，只保留置信度最高的边界框。

SSD 的优势在于它在单一网络中同时进行目标检测和分类，避免了传统目标检测方法中复杂的候选框生成和筛选过程，从而实现了实时目标检测。它可以应用于各种应用场景，如车辆检测、行人检测、物体检测等。

由于 SSD 的设计简单、轻量，并且在速度和准确率上都有良好的表现，因此在计算机视觉领域得到了广泛的应用。随着深度学习技术的不断发展，SSD 的改进版本也在不断涌现，使得目标检测在实际应用中取得了更加出色的效果。

[^1]: Chaturvedi, S., Khanna, P., Ojha, A. (2022). **A survey on vision-based outdoor smoke detection techniques for environmental safety**. ISPRS Journal of Photogrammetry and Remote Sensing 185, 158–187. [doi][doi1]
[^2]: Khan, Fawad, Xu, Z., Sun, J., Khan, Fazal, Ahmed, A., Zhao, Y. (2022). Recent Advances in Sensors for Fire Detection. Sensors 22, 3310. [doi][doi2]
[^3]: Chen, J., Peng, X. (2023). **DB-Net: Detecting Vehicle Smoke with Deep Block Networks**. Applied Sciences 13. [doi][doi3]
[^4]: 洪詮盛 (2021). **結合YOLOv4煙霧偵測與AOD-Net影像除霧之深度學習技術於車輛廢氣排放檢測系統實作**. 指導教授陳璽煌。資訊工程系碩士班. 樹德科技大學, 高雄市.[url][url4]
[^5]: 呂承恩 (2022). **利用人工智慧建立煙霧不透光率辨識系統**. 環境科學與工程學系. 東海大學, 台中市.[url][url5]
[^6]: Ju, A., Wang, Z. (2022).**A novel fully convolutional network based on marker-controlled watershed segmentation algorithm for industrial soot robot target segmentation**. Evolutionary Intelligence 16, 1–18. [doi][doi6]
[^7]: Pedrayes, O.D., Usamentiaga, R., García, D.F. (2023). **Fully automated method to estimate opacity in stack and fugitive emissions: A case study in industrial environments**. Process Safety and Environmental Protection 170, 479–490. [doi][doi7]
[^8]: Koushafar, M., Sohn, G., Gordon, M. (2023). **Deep Convolutional Neural Network for Plume Rise Measurements in Industrial Environments.** Remote Sensing 15, 3083. [doi][doi8]
[^9]: Li, D., Yang, R., Su, C. (2023). **Generative adversarial network based on LSTM and convolutional block attention module for industrial smoke image recognition.** Computer Science and Information Systems 27–27. [doi][doi9]
[^10]: Peng, X., Fan, X., Wu, Q., Zhao, J., Gao, P. (2022). **Video-based Smoky Vehicle Detection with A Coarse-to-Fine Framework.** arXiv:2207.03708.[doi][doi10]
[^11]: Feng, L., Yang, T., Wang, D., Wang, Z., Pan, Y., Matsui, I., Chen, Y., Xin, J., Huang, H. (2020). **Identify the contribution of elevated industrial plume to ground air quality by optical and machine learning methods**. Environ. Res. Commun. 2, 021005. [doi][doi11]
[^12]: 
[^13]: Grant-Jacob, J., Mills, B. (2022). **Deep learning in airborne particulate matter sensing: a review.** Journal of Physics Communications 6, 122001. [doi][doi13]
[^15]: Su, P., Liu, Y., Tarkoma, S., Rebeiro-Hargrave, A., Petaja, T., Kulmala, M., Pellikka, P. (2022). **Retrieval of Multiple Atmospheric Environmental Parameters From Images With Deep Learning**. IEEE Geoscience and Remote Sensing Letters 19, 1–1. [doi][doi15]
[^16]: Yao, S., Huang, B. (2021). **Extraction of Aerosol Optical Extinction Properties From a Smartphone Photograph to Measure Visibility.** IEEE Transactions on Geoscience and Remote Sensing PP, 1–1. [doi](https://doi.org/10.1109/TGRS.2021.3132431)
[^17]: Yao, S., Wang, F., Huang, B. (2022). **Measuring PM2.5 Concentrations from a Single Smartphone Photograph.** Remote Sensing 14, 2572. [doi](https://doi.org/10.3390/rs14112572)
[^18]: Wang, F., Yao, S., Luo, H., Huang, B. (2022). **Estimating High-Resolution PM2.5 Concentrations by Fusing Satellite AOD and Smartphone Photographs Using a Convolutional Neural Network and Ensemble Learning**. Remote Sensing 14, 1515. [doi](https://doi.org/10.3390/rs14061515)
[^19]: Wang, X., Wang, M., Liu, X., Zhang, X., Li, R. (2022). **A PM2.5 concentration estimation method based on multi-feature combination of image patches**. Environmental Research 211, 113051. [doi][doi19]
[^20]: Ahmed, Maqsood, Shen, Y., Ahmed, Mansoor, Xiao, Z., Cheng, P., Nafees, A., Ghaffar, A., Ali, S. (2022). **AQE-Net: A Deep Learning Model for Estimating Air Quality of Karachi City from Mobile Images**. Remote Sensing 14, 5732. [doi](https://doi.org/10.3390/rs14225732)
[^21]: Mohan, A., Abraham, L. (2023). **Particulate Matter Concentration Estimation from Images Based on Convolutional Neural Network**. [doi](https://doi.org/10.1007/978-981-19-7513-4_5)
[^22]: Ahmed, M., Xiao, Z., Shen, Y. (2022). **Estimation of Ground PM2.5 Concentrations in Pakistan Using Convolutional Neural Network and Multi-Pollutant Satellite Images.** Remote Sensing 14, 1735. [doi](https://doi.org/10.3390/rs14071735)
[^23]: Pu Yun, K., Hsia, I.-W., Chang, L.-C., Chang, F.-J. (2022). **Real-time image-based air quality estimation by deep learning neural networks.** Journal of Environmental Management 307, 114560. [doi](https://doi.org/10.1016/j.jenvman.2022.114560)
[^14]: Zhang, Q., Fu, F., Tian, R. (2020). **A deep learning and image-based model for air quality estimation.** Science of The Total Environment 724, 138178. [doi](https://doi.org/10.1016/j.scitotenv.2020.138178)
[^24]: Zhang, Q., Tian, L., Fu, F., Wu, H., Wei, W., Liu, X. (2022). **Real‐Time and Image‐Based AQI Estimation Based on Deep Learning**. Advanced Theory and Simulations 5. [doi](https://doi.org/10.1002/adts.202100628)
[^25]: Sheikh, S., Raut, S., Rane, S., Raut, P. (2022). **Air Quality Detection using Land Coverage Machine Learning Techniques- CNN.** International Journal of Advanced Research in Science, Communication and Technology 475–482. [doi](https://ijarsct.co.in/Paper3957.pdf)
[^26]: Mondal, J.J., Islam, M., Islam, R., Rhidi, N., Manab, M.A., Islam, A.B.M.A.A., Noor, J. (2022). **Unmasking the Invisible: Finding Location-Specific Aggregated Air Quality Index with Smartphone Images**, Presented at the 9th International Conference on Networking, Systems and Security (NSysS 2022), Cox’s Bazar, Bangladesh. [doi](https://doi.org/10.13140/RG.2.2.12552.08968)
[^27]: Jiang, C., Ye, X., Zhu, J., Zeng, H., Nan, Y., Sun, M., Ren, X., Huo, H.-T. (2022). **Object detection from UAV thermal infrared images and videos using YOLO models**. International Journal of Applied Earth Observation and Geoinformation 112, 102912. [doi](https://doi.org/10.1016/j.jag.2022.102912)
[^28]: Tsai, P.-F., Liao, C.-H., Yuan, S.-M. (2022). **Using Deep Learning with Thermal Imaging for Human Detection in Heavy Smoke Scenarios**. Sensors 22. [doi](https://doi.org/10.3390/s22145351)
[^29]: Kim, J.-H., Lattimer, B.Y. (2015). **Real-time probabilistic classification of fire and smoke using thermal imagery for intelligent firefighting robot**. Fire Safety Journal 72, 40–49. [doi](https://doi.org/10.1016/j.firesaf.2015.02.007)
[^30]: Al-Smadi, Y., Alauthman, M., Al-Qerem, A., Aldweesh, A., Quaddoura, R., Aburub, F., Mansour, K., Alhmiedat, T. (2023). **Early Wildfire Smoke Detection Using Different YOLO Models**. Machines 11, 246. [doi](https://doi.org/10.3390/machines11020246)
[^31]: Park, M., Ko, B.C. (2020). **Two-Step Real-Time Night-Time Fire Detection in an Urban Environment Using Static ELASTIC-YOLOv3 and Temporal Fire-Tube**. Sensors (Basel) 20, 2202. [doi](https://doi.org/10.3390/s20082202)
[^32]: Sun, Y., Feng, J. (2023). **Fire and smoke precise detection method based on the attention mechanism and anchor-free mechanism**. Complex Intell. Syst. [doi](https://doi.org/10.1007/s40747-023-00999-4)
[^33]: Shi, J., Chang, Y., Xu, C., Khan, F., Chen, G., Li, C. (2020). **Real-time leak detection using an infrared camera and Faster R-CNN technique**. Computers & Chemical Engineering 135, 106780. [doi](https://doi.org/10.1016/j.compchemeng.2020.106780)
[^34]: Zhu, H., Xie, W., Li, J., Shi, J., Fu, M., Qian, X., Zhang, H., Wang, K., Chen, G. (2023). **Advanced Computer Vision-Based Subsea Gas Leaks Monitoring: A Comparison of Two Approaches**. Sensors 23. [doi](https://doi.org/10.3390/s23052566)


[doi19]: https://doi.org/10.1016/j.envres.2022.113051 "(Wang et al., 2022)"
[doi15]: https://doi.org/10.1109/LGRS.2022.3149045 "(Su et al., 2022)"
[doi13]: https://doi.org/10.1088/2399-6528/aca45e "(Grant-Jacob and Mills, 2022)"
[doi11]: https://doi.org/10.1088/2515-7620/ab7634 "(Feng et al., 2020)"
[doi10]: https://doi.org/10.48550/arXiv.2207.03708
[doi9]: https://doi.org/10.2298/CSIS221125027L "(Li et al., 2023)"
[doi8]: https://doi.org/10.3390/rs15123083 "(Koushafar et al., 2023)"
[doi7]: https://doi.org/10.1016/j.psep.2022.12.023 "'"
[doi6]: https://doi.org/10.1007/s12065-022-00708-z
[url5]: https://hdl.handle.net/11296/43b7s4 "呂承恩, 2022"
[url4]: https://hdl.handle.net/11296/364pzk "洪詮盛, 2021"
[doi3]: https://doi.org/10.3390/app13084941 "(Chen and Peng, 2023)"
[doi2]: https://doi.org/10.3390/s22093310 "(Khan et al., 2022)"
[doi1]: https://doi.org/10.1016/j.isprsjprs.2022.01.013 "(Chaturvedi et al., 2022)"
