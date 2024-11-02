---
layout: default
title: 辨識講者的會議轉錄
parent: 語音辨識
nav_order: 99
grand_parent: 型態與辨識
date: 2024-11-02
last_modified_date: 2024-11-02 13:13:04
tags: EE AI
---

# 辨識講者的會議轉錄

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

- 會議中使用語音辨識技術能提高效率，減少手動紀錄時間，並且在辨識多講者的環境中，提供自動轉錄服務。
- 隨著 AI 進步，不同 ASR 模型與整合方案逐漸應運而生，為使用者提供更多選擇。

這篇筆記建議從各項方案的特點與應用情境著手，依照會議需求選擇適合的 ASR 模型或整合方案。
希望這些資訊能幫助您在進行會議轉錄時找到最佳解決方案。

## 開源方案

### Transcripy 與 pyannote-speaker-diarization
- source：[github:Haschtl/transcripy](https://github.com/Haschtl/transcripy/tree/main)
  - 使用[pyannote speaker dairiation 2020 技術](https://github.com/Haschtl/transcripy/tree/main)
  - Transcripy 利用 pyannote 技術辨識講者，能有效分辨會議中不同講者的語音訊息，適用於開源環境下對多講者辨識需求的情境。

### 2024年5款常用開源的轉錄模型

Whisper、DeepSpeech、Kaldi、Wav2vec、SpeechBrain。每款 ASR 模型各有特點：

- Whisper 專注於多語言辨識、
- DeepSpeech 對資源需求較低、
- Kaldi 開放度高但學習曲線較陡、
- Wav2vec 擅長於低資源語音辨識，而 
- SpeechBrain 則提供多功能模組以供自訂。
- source：Whisper, DeepSpeech, Kaldi, Wav2vec, or SpeechBrain: key factors to consider when choosing an open-source ASR model for your apps and projects. [gladia 2024/9](https://search.app/3qeTmo6sdr7fT3rT7)

## 雲端ASR模型

- [Amazon Transcribe 2023/11](https://aws.amazon.com/tw/blogs/machine-learning/amazon-transcribe-announces-a-new-speech-foundation-model-powered-asr-system-that-expands-support-to-over-100-languages/)
  - 支援超過 100 種語言的辨識，適合國際化的多語言會議。
  - 其最新的語音模型能自動識別語者並進行精準轉錄。
- [google speech-to-text of multiple persons](https://cloud.google.com/speech-to-text/docs/multiple-voices)
  - 具有多人聲音辨識能力，能辨識會議中的不同講者，
  - 特別適合需要自動分段和標註的會議情境。

## 商業整合方案

### 經理人部落格

- 再也不用輪流寫會議記錄！3 個即時記錄、產出摘要的 AI 小工具，讓你專心開會[經理人2024/5](https://www.managertoday.com.tw/articles/view/68542)
  - 經理人網站所提及的多款工具如 Flags、Vocol.ai 和 Goodtape，專注於即時會議紀錄與摘要生成，讓用戶能專注於會議本身而無需分心紀錄。
    - 會議夥伴[creative.ai Flags by 4149](https://creati.ai/tw/ai-tools/flags-by-4149/)
    - [vocal.ai 犀動智能@內湖](https://www.vocol.ai/tw/home)
    - [goodtape](https://blog.goodtape.io/zh/?gad_source=1&gclid=CjwKCAjw-JG5BhBZEiwAt7JR6zNorIOpIWK3-MHYqILElNbMruvSf6KIiXrNoWqG-hpSCDOjkMbl5xoC9zIQAvD_BwE)

### 其他

- 在地化多語系環境設計，精準辨識每一段對話[uni-ai@內湖](https://uni-ai.ai/2024/08/%E9%95%B7%E5%95%8F%E7%A7%91%E6%8A%80-ai%E6%99%BA%E8%83%BD%E8%AA%9E%E9%9F%B3%E6%9C%83%E8%AD%B0%E7%B4%80%E9%8C%84%E7%B3%BB%E7%B5%B1/)
  - 特別針對多語環境的語音辨識需求而設計，
  - 適合在多文化、多語系的商務或政府會議中使用。
- AI多人語音辨識會議紀錄​[Qmeeting@板橋](https://qmeeting.qshop.net.tw/qmeeting_ai/)
  - line好友156人
  - 支援多人語音辨識
- cyberlink [MyEdit](https://tw.cyberlink.com/blog/audio-editing/3248/ai-meeting-minutes)
  - 提供簡單的會議記錄功能；
- METAMatch 會議記錄AI助手 (企業雲端版)[@內湖](https://www.metamatch.market/products/detail/METAMatch-MeetingAI)
  - 會議記錄助手適合企業用戶，
  - 提供雲端存取和安全性保障。