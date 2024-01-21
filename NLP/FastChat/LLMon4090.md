---
layout: default
title: Nvidia RTX 4090
parent: FastChat
grand_parent: 自然語言處理
nav_order: 99
date: 2023-09-05
last_modified_date: 2023-09-05 13:44:37
tags: AI chat
---


# RTX 4090 上執行LLM推論
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

### Modules and Accelerators

如果您想要使用 NVIDIA 4090 進行大型語言模型推論，您可以使用 TensorFlow 或 PyTorch 這兩個框架。這兩個框架都支持 NVIDIA GPU，並且都可以使用 CUDA 和 cuDNN 來加速模型訓練和推論¹。

如果您使用 TensorFlow，您需要安裝 TensorFlow-GPU 版本，並且需要安裝 CUDA 和 cuDNN。TensorFlow 的官方網站提供了 CUDA 和 cuDNN 的安裝指南²。如果您使用 PyTorch，您需要安裝 PyTorch-GPU 版本，並且需要安裝 CUDA。PyTorch 的官方網站提供了 CUDA 的安裝指南¹。

希望這些信息對您有所幫助！

來源: 與 Bing 的交談， 2024/1/21
(1) Win11 RTX 4090显卡深度学习环境配置（Nvidia显卡驱动、CUDA11.7.0）_4090对应的cuda版本-CSDN博客. https://blog.csdn.net/wokaowokaowokao12345/article/details/131134993.
(2) 请问4060ti该如何选择tensorflow版本和对应的cuda,cudnn。? - 知乎. https://www.zhihu.com/question/633490166.
(3) 4090显卡安装什么cuda来使用pytorch或者tensorflow？ - CSDN博客. https://blog.csdn.net/qq_42769818/article/details/128049381.
(4) ubuntu22.04 RTX4090搭建cuda11.8+cudnn8.9+tensorflow-gpu2.4 - CSDN博客. https://blog.csdn.net/qq_43765984/article/details/134215864.
(5) Ubuntu 20.04 RTX 4090显卡 深度学习环境配置（Nvidia显卡驱动、CUDA11.6.0、cuDNN8.5）_4090 cuda版本-CSDN博客. https://blog.csdn.net/chen20170325/article/details/130294270.
(6) undefined. https://www.anaconda.com/download/.
(7) undefined. https://www.jetbrains.com/pycharm/download/.
(8) undefined. https://developer.nvidia.com/cuda-toolkit-archive.
(9) undefined. https://pypi.tuna.tsinghua.edu.cn/simple.
(10) undefined. https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local.


