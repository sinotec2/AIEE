---
layout: default
title: openAI API
parent: openAI
grand_parent: 自然語言處理
nav_order: 99
date: 2024-01-20
last_modified_date: 2024-01-20 13:12:57
tags: AI chat
---


# openAI API
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

## Limits

Usage tier 1

Rate limits
API usage is subject to rate limits applied on tokens per minute (TPM), requests per minute or day (RPM/RPD), and other model-specific limits. Your organization's rate limits are listed below.

Visit our [rate limits guide](https://platform.openai.com/docs/guides/rate-limits) to learn more about how rate limits work.

Note: Limits for specific model versions may vary, expand the table to see all models.

### CHAT

MODEL|TOKEN LIMITS|REQUEST AND OTHER LIMITS
:-|:-:|:-:
gpt-3.5-turbo|60,000 TPM|500 RPM/10,000 RPD
gpt-3.5-turbo-0301|60,000 TPM|500 RPM/10,000 RPD
gpt-3.5-turbo-0613|60,000 TPM|500 RPM/10,000 RPD
gpt-3.5-turbo-1106|60,000 TPM|500 RPM/10,000 RPD
gpt-3.5-turbo-16k|60,000 TPM|500 RPM/10,000 RPD
gpt-3.5-turbo-16k-0613|60,000 TPM|500 RPM/10,000 RPD
**gpt-3.5-turbo-instruct**|250,000 TPM|3,000 RPM
**gpt-3.5-turbo-instruct-0914**|250,000 TPM|3,000 RPM
gpt-4|10,000 TPM|500 RPM/10,000 RPD
gpt-4-0613|10,000 TPM|500 RPM/10,000 RPD
gpt-4-1106-preview|150,000 TPM/500,000 TPD500| RPM/10,000 RPD
gpt-4-vision-preview|10,000 TPM|80 RPM/500 RPD

### TEXT

MODEL|TOKEN LIMITS|REQUEST AND OTHER LIMITS
:-|:-:|:-:
ada-code-search-code|250,000 TPM|3,000 RPM
ada-code-search-text|250,000 TPM|3,000 RPM
ada-search-document|250,000 TPM|3,000 RPM
ada-search-query|250,000 TPM|3,000 RPM
babbage-002|250,000 TPM|3,000 RPM
babbage-search-document|250,000 TPM|3,000 RPM
babbage-search-query|250,000 TPM|3,000 RPM
curie-search-document|250,000 TPM|3,000 RPM
curie-search-query|250,000 TPM|3,000 RPM
davinci-002|250,000 TPM|3,000 RPM
davinci-search-document|250,000 TPM|3,000 RPM
davinci-search-query|250,000 TPM|3,000 RPM
text-embedding-ada-002|1,000,000 TPM|3,000 RPM
tts-1||50 RPM
tts-1-1106||50 RPM
tts-1-hd||3 RPM
tts-1-hd-1106||3 RPM