---
layout: default
title:  BLEU
parent: Bilingual AI Processing
grand_parent: 自然語言處理
nav_order: 99
date: 2024-11-21
last_modified_date: 2024-11-22 05:28:34
tags: AI chat
---


# BLEU
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

- [python模組](https://search.app/y6ZP3Fa4gBNSfvxK6)
	- 用 Python 計算文本 BLEU 分數和 ROUGE 值
	- Python 的 NLTK 和 Rouge 库可以用來計算文本生成任務中的 BLEU 分數與 ROUGE 值，以評估生成文本與參考文本的差異程度。
	- NLTK 支援句子級與語料級的 BLEU 分數計算，並允許自定義 n 元組權重；
	- Rouge 庫則提供 ROUGE-1、ROUGE-2 和 ROUGE-L 的準確率、召回率和 F1 值計算。
	- 這些指標被廣泛用於機器翻譯與自動摘要生成評估中。

## NIST

NIST（National Institute of Standards and Technology）的計算，通常與其多種標準和工具相關。具體問題可能涉及不同領域，例如加密、性能測量或自然語言處理等。以下介紹幾個常見的 NIST 計算情境：

1. NIST BLEU 計算

在自然語言處理中，NIST 計算方法是 BLEU 的改進版，用於評估機器翻譯的準確性。
	•	BLEU（Bilingual Evaluation Understudy）注重 n-gram 匹配的次數，但 NIST 增加了 n-gram 的「資訊量權重」，更重視關鍵 n-gram 的匹配。

計算公式概述：

	•	n-gram 加權：
	•	BLEU 將 n-gram 視為同等重要，NIST 則根據 n-gram 的稀有性賦予不同權重，稀有的 n-gram 匹配將獲得更高的分數。
	•	使用資訊增益（Information Gain）衡量權重：
￼
	•	懲罰因子：
與 BLEU 相同，包含 brevity penalty（簡短懲罰），避免生成過於簡短的翻譯。

2. NIST SP 800 系列指導（如加密計算）

NIST 在資訊安全中的標準（如 AES 加密、密碼強度）提供了許多指南，例如：
	•	隨機數生成：
使用公式衡量隨機數的熵。熵越高，安全性越強。
	•	加密效率：
計算加密的吞吐量、延遲等。公式通常由實驗測得：
￼
3. NIST EER 計算（生物識別系統）

在生物識別系統中，NIST 定義了 EER（Equal Error Rate），用於衡量系統的準確性。
	•	定義： 當錯誤接受率（FAR）和錯誤拒絕率（FRR）相等時，系統的 EER 即為該值。
	•	公式：
通過調整閾值，找到以下相等的點：
￼

4. NIST 測試套件（隨機性測試）

在隨機性測試中，NIST 提供一系列統計方法來衡量隨機數生成器的質量。例如：
	•	頻率測試：
測試比特流中「1」和「0」的出現比例是否接近均勻。
￼

常見應用

	•	自然語言處理：NIST BLEU 分數用於翻譯評估。
	•	資訊安全：計算密碼強度、加密算法效能。
	•	生物識別：計算 EER 評估系統效能。
	•	隨機性測試：確保隨機數生成器的品質。

