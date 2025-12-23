---
title: 在LibreChat執行檔案總管
tags: AI
layout: default
parent: LibreChat
grand_parent: Utilities
nav_odrer: 3
date: 2025-11-01
modify_date: 2025-11-24T16:08:00
---

# 在LibreChat執行檔案總管

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


![](https://avatars.githubusercontent.com/u/17607124?s=200&v=4)

![](https://raw.githubusercontent.com/filebrowser/filebrowser/master/branding/banner.png)

::: info

1️⃣**[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)**
指揮AI來處理我們的檔案是很令人興奮的一件事，因為提供了上下文，似乎AI真的懂我們的意思。但有的時候AI似乎不太受掌控，需要調整一個最好的狀態。
2️⃣**[filebrowser](https://filebrowser.org/)**
可以想像LibreChat本身就是一台網路上的主機，處理檔案會需要透過層層關卡、上載、下載。
Window系統上我們有所謂的"**檔案總管**"來處理不同網路磁碟機(??槽)的檔案交換，為了方便大家，我們提供了「filebrowser」的網頁app，來加速本機與LibreChat主機之間的檔案存取。

:::
## 步驟1️⃣登入filebrowser

- 雖然LibreChat提供了圖檔、文字檔等2種檔案的上傳，但卻沒有提供下載的方式，或者其他檔案的上載，因此filebrowser這類的app事有其存在的必要的。
- LibreChat的開放路徑`/app/logs`，可以在[filebrowser](http://172.20.31.6:8080/files/)中出現，目前採開放管理、每日清理政策。

| ![](pngs/Pasted%20image%2020251123210512.png) |
| :-------------------------------------------: |
|    在filebrowser中出現了各式便當.csv檔案，使用者可以下載、刪除。     |
| ![](pngs/Pasted%20image%2020251123211049.png) |
|     filebrowser介面點選檔案名稱(隨即下載)，右鍵也會出現其他功能。     |
