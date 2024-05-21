---
layout: default
title: Celery
parent: Task Scheduler Server
grand_parent: Utilities
nav_order: 99
date:  2023-09-26
modify_date: 2023-09-26 14:45:42
tags: AI
---

# Celery
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

- 官網[celeryproject.org](https://docs.celeryproject.org/en/stable/index.html)
- 中文介紹與範例[IT Home](https://ithelp.ithome.com.tw/articles/10243148)
  - [code repo]( https://github.com/elleryq/ithome-iron-2020-django/tree/day-24)
- Celery 有以下優點：
  - 分散式，可以有多個 broker、worker ，換言之，在 broker / worker 不足時，可以增加；太多的時候可以減少。
  - 工作可以定期執行。
  - 工作可以串接，也可以並行，組合成流程工作。
  - 支援信號，可以在完成時通知傾聽訊號的函式。
  - Celery 排程的時間解析度最小可以到秒（seconds）。（crontab 的時間設定最小單位是分鐘）