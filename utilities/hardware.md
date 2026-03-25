---
title: 硬體設備剪報
tags: AI
layout: default
parent: Utilities
date:  2023-09-26
modify_date: 2023-09-26 14:45:42
---

# 硬體設備剪報
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

## Dell 8-GPU伺服器

搭配輝達頂級資料中心GPU，Dell推首款8-GPU伺服器
[ithome(李宗翰 | 2023-04-22發表)](https://www.ithome.com.tw/review/156425)

Dell首度推出可搭配8個Nvidia H100或A100 GPU的伺服器，搶攻亟需強大運算效能的企業深度學習應用市場

文/李宗翰 | 2023-04-22發表

自從2022年3月Nvidia發表新一代資料中心GPU產品H100，我們一直很關心各家伺服器廠商何時會推出可搭配這款GPU的機型，在11月SC22大會期間，Nvidia宣布有十多個廠牌、數十款伺服器將採用H100，而這些伺服器機型當中，他們特別標榜Dell即將推出的PowerEdge XE9680，因為這款機型是該公司第一次基於Nvidia HGX平臺而成的8-GPU系統，可搭配8個Nvidia H100或A100，而在中央處理器的部分，則採用兩顆同樣即將問世的英特爾第四代Xeon Scalable系列，而在散熱方面，採用氣冷設計，是專為融合模擬、資料分析、人工智慧等用途所設計的伺服器機型，能針對人工智慧提供最大運算效能。

在此之前，Dell針對SXM外形的Nvidia資料中心GPU支援，僅提供4-GPU組態的機型，而且伺服器配置均由該公司設計，例如，2021年3月發表的XE8545，搭配4個A100；2017年11月發表的C4140，可搭配P100和V100的NVLink版本GPU。

發表XE9680的同時，Dell也預告將推出搭配4個SXM外形Nvidia H100 GPU的4U氣冷伺服器，機型名稱是XE8640，以及搭配4張OAM外形的Intel Data Center GPU Max系列的2U液冷伺服器，機型名稱是XE9640。而關於這三款機型的上市時程，當時的規畫是在2023年上半。

2022年12月，Dell釋出XE9680技術規格文件，揭露更多硬體基本配置，例如，機箱尺寸是6U高度，DDR5-4800記憶體插槽有32個，機箱前緣可安裝10張全高半長尺寸的PCIe 5.0介面卡，電源供應器為2800瓦；硬碟目前能搭配8臺2.5吋NVMe SSD，未來能搭配到16臺；搭配2顆英特爾第四代Xeon Scalable處理器，每顆核心最多為56個；若以整臺伺服器機箱而言，會有6個高效能金級風扇設置在中間，協助處理器散熱，以及10個高效能金級風扇設置在尾端，協助GPU與PCIe介面卡散熱。

今年1月，英特爾正式發表第四代Xeon Scalable伺服器處理器，3月Dell在臺灣舉辦全新一代PowerEdge伺服器發表記者會時，首度公開展出上述三款GPU伺服器，

其中的XE9680，根據Dell在新加坡舉行的PowerEdge .Next之Power Innovation Anywhere大會發布的消息，已於3月底正式出貨，也是市面上能買到的第一款搭載Nvidia H100的伺服器，而此款機型的技術指南、安裝與服務手冊等文件，也在3月出爐，當中更明確交代了硬體規格細節。

例如，可搭配的處理器熱設計功耗（TDP）最高為350瓦，這也是第四代Xeon Scalable處理器的TDP上限，並且搭配2U高度的CPU高效能散熱座與CPU高效能金級風扇。

關於GPU的設置，若採用預載8個Nvidia A100的HGX基板／Nvidia Delta Board，可搭配4U高度GPU散熱座與NVLink散熱座，以及GPU高效能金級風扇；若採用預載8個Nvidia H100的Nvidia Delta Board，只需搭配GPU高效能金級風扇。而在伺服器可運作的溫度範圍，則是介於攝氏10度到35度之間。

先前Dell預告XE9680可搭配到16臺硬碟，而根據最新發布的技術規格文件指出，這是指E3.S外形的NVMe固態硬碟；

而在電源供應器的部分，可搭配到6臺。

產品資訊：Dell EMC PowerEdge XE9680

- 原廠：Dell
- 建議售價：廠商未提供
- 機箱尺寸：6U
- 處理器：2顆，第四代Xeon Scalable系列（最高搭配56核心機型）
- 記憶體：32個DDR5-4800插槽，最大可擴充至**4 TB**
- 儲存配置：8臺2.5吋NVMe固態硬碟+2臺M.2 NVMe固態硬碟(10x1.9=19T)
- 搭配GPU：
  - Nvidia HGX H100 8-GPU，8個SXM5形式GPU，或是
  - Nvidia HGX A100 8-GPU，8個SXM4形式GPU
- I/O擴充介面：10個PCIe 5.0 x16全高半長介面卡
- 電源供應器：6臺2800瓦

【註：規格與價格由廠商提供，因時有異動，正確資訊請洽廠商】

## NVIDIA GPU Drivers

- [NVIDIA Driver Downloads](https://www.nvidia.com/download/index.aspx)
- L40
  - version: 535.129.03(2024/3),  550.54.15(2024/4/17)
  - 下載550的安裝檔在`L40:/home/kuang/MyPrograms`
  ```bash
  Product Type:	Data Center / Tesla
  Product Series:	L-Series
  Product:	L40
  OSystem:	Linux 64-bit
  CUDA Toolkit:	Any
  Language:	Chinese (Traditional)
  ```
- RTX 4090
  ```bash
  Product Type:	GeForce
  Product Series:	GeForce RTX 40 Series
  Product:	NVIDIA GeForce RTX 4090
  O System:	Linux 64-bit
  Download Type:	Production Branch
  Language:	Chinese (Traditional)
  ```

### 550之重啟

- 550無法由`apt-get install`，原因不明，必須由`.run`重新安裝驅動程式，重啟電腦(還有可能需要關電源重開)
```bash
 1997  sudo sh NVIDIA-Linux-x86_64-550.54.15.run
 1998  sudo reboot
```

- 重啟後重新安裝`nvidia-container-toolkit`，`docker` 才能抓得到 `nvidia` 的 `runtime`
- 先登記`key`
- 下載指定版本的安裝檔
	- 注意複製`$..$..`時，因為是markdown約定的格式(斜體)，要記得還原成bash的變數約定。
- `apt-get`安裝

``` bash
 2016  sudo nvidia-ctk runtime configure --runtime=docker
 2019  sudo mkdir -p /usr/share/keyrings
 2020  curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
 2028  curl -fsSL https://nvidia.github.io/libnvidia-container/$(. /etc/os-release; echo $ID$VERSION_ID)/libnvidia-container.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
 2029  sudo apt-get update
 2030  sudo apt-get install -y nvidia-container-toolkit
```

- 啟動`docker`的`runtime`
- 重啟`docker`

```bash
 2031  sudo nvidia-ctk runtime configure --runtime=docker
 2032  sudo systemctl restart docker
```

- docker指令 `docker run --runtime nvidia`

```bash
docker run --runtime nvidia -d \
    --gpus "device=${g}" \
    -v /data/llm:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=$secret" \
    -p 800${i}:8000 \
    ...
``
