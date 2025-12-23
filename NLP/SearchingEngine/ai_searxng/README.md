---
layout: default
title: 地端智慧搜尋引擎
parent: SearchingEngine
grand_parent: 自然語言處理
nav_order: 99
date: 2025-11-11
last_modified_date: 2025-11-11T11:59:00
has_children: true
permalink: /NLP/SearchingEngine/ai_searxng
tags:
  - AI
  - chat
  - searching
---

# 地端智慧搜尋引擎
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

## 特色

- ==SearXNG==是開源**高階**、**多來源**搜尋引擎領域中的佼佼者，目前營運中的[實例](https://searx.space/)就有72例之多，可以說是非常活躍的開源系統。
- 連結**外部**搜尋引擎：避開商業廣告干擾、注重隱私權(不會猜測使用者習慣)的搜尋引擎，
- 提供後台API讓別人串接、適合大量作業化、批次化研究性質之搜尋(**連出**)
- 串接地端資源(**連入**)：
	- 自設插件系統：連結自設功能，如地端AI API。
	- 自接搜尋引擎：連結地端企業資料庫、自設搜尋引擎等等。
	- 自設資訊欄：連結地端wiki系統

## 地端實例

==免帳密==
[https://l40.sinotech-eng.com/searxng/](https://l40.sinotech-eng.com/searxng/)

## 入口畫面

![](pngs/Pasted%20image%2020251111191711.png)

### 神奇符號(!)


- [地端OES](http://oes.sinotech-eng.com:7651/cgi-bin/search/qpage.cgi?act=simple) &rightarrow; `!oes` 
	- OES  = Openfind Enterprise Searching 
	- 資料存放後台：[需帳密網路磁碟機](\\172.20.32.158\Data)	
- [地端 mediawiki](https://eng06.sinotech-eng.com/wiki/index.php) &rightarrow; `!swiki`
	
- 啟用AI摘要 &rightarrow; `ai ...`

![](pngs/Pasted%20image%2020251111191559.png)
### 使用手冊

- [mediawilki中文版](https://eng06.sinotech-eng.com/wiki/index.php/SearXNG使用手冊)
- [VPH中文圖說版](./searxng_UG.md)
- [官網英文版](https://docs.searxng.org/user/search-syntax.html)