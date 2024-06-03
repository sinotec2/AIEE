---
layout: default
title: PPLx API
parent: PPLx Interface and API
grand_parent: 自然語言處理
nav_order: 99
date: 2024-01-20
last_modified_date: 2024-01-20 13:12:57
tags: AI chat
---


# PPLx API
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

## Pricing

pplx-api implements a usage-based pricing model. Perplexity Pro users get $5 of free credit every month.

### Suggest Edits

Usage is priced on tokens based on the size of the model.

模型參數|$/1M tokens
-|:-:
7B|$0.20
8B|$0.20
8x7B|$0.60
34B|$0.80
8x22B|$1.00
70B|$1.00

For -online models, in addition to the token charges, a flat $5 is charged per thousand requests (or half a cent per request、6個請求1元台幣).

Online Model|$/1000 requests
-|:-:
llama-3-sonar-small-32k-online|$5
llama-3-sonar-large-32k-online|$5
Updated 26 days ago