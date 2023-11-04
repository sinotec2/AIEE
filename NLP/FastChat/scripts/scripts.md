---
layout: default
title: scripts
parent: FastChat
grand_parent: 自然語言處理
nav_order: 99
permalink: /NLP/FastChat/scripts/
date: 2023-11-04
last_modified_date: 2023-11-04 10:18:34
tags: AI fastchat
---

# scripts
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

- [test_readme_train.sh](./test_readme_train.sh)
  - 以ata/dummy_conversation.json測試lamma7b訓練模型
- [train_lora.sh](./train_lora.sh)
  - 測試`--lora_r 8 \    --lora_alpha 16 \    --lora_dropout 0.05 \`
- [train_vicuna_7b.sh](./train_vicuna_7b.sh)
- [train_vicuna_13b.sh](./train_vicuna_13b.sh)
- [upload_pypi.sh](./upload_pypi.sh)
