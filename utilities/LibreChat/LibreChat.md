---
title: LibreChat使用手冊
icon: dove
lastUpdated: 2025-11-01T13:08:00
contributors: '[{"name":"kuang"}]'
order: 1
---
::: note
這一份以「==LibreChat== [官方文件](https://www.librechat.ai/docs)」為基礎的使用手冊範例，專門針對本公司同仁使用。  <br>
==LibreChat==服務位址✨✨[https://librechat.sinotech-eng.com/](https://librechat.sinotech-eng.com/)✨✨
:::
---

## LibreChat 使用手冊（內部版）

### 目錄
1. 什麼是 LibreChat？
2. 快速啟動指南
3. 檔案RAG
4. 深入探索 LibreChat 功能
5. 故障排除（Troubleshooting）
6. 聯絡方式

---

![](pngs/Pasted%20image%2020251030121003.png)
### 1. 什麼是 LibreChat？

==LibreChat== 是一個開源、可自訂的聊天機器人平台，允許使用者快速建立、訓練並部署對話式 AI。官方文件首頁（[https://www.librechat.ai/docs](https://www.librechat.ai/docs)）提供了完整的概念說明與使用說明。

---

### 2. 快速啟動指南

> 參考官方文件首頁的「Quick Start Guides」區塊，以下為常見的快速啟動步驟概覽。

#### 2.1 進入 LibreChat
1. 打開瀏覽器，輸入 ==LibreChat== 服務的公司內部網址(✨✨[https://librechat.sinotech-eng.com/](https://librechat.sinotech-eng.com/)✨✨)。
2. 若為首次使用，請自行**註冊**：
	- 請使用公司email作為帳號登入，便於管理。
	- 密碼：至少需8碼英數。🎱

| ![](pngs/Pasted%20image%2020251030121437.png) | ![](pngs/Pasted%20image%2020251030121641.png) |
| --------------------------------------------- | --------------------------------------------- |
| 第一次請自行**註冊**🤩                                | 請用公司電子郵件註冊。密碼至少8碼。🎱                          |

#### 2.2 建立第一個對話
1. 更改個人設定：語言(選擇**繁體中文**)、主題(隨系統、淺色或深色)、帳號->個人頭像(標示不同登入帳號)
	![](pngs/Pasted%20image%2020251030125459.png)
2. 在主頁面點擊「New Chat」或「建立新對話」按鈕。
3. 輸入對話主題或直接開始對話。

| ![](pngs/Pasted%20image%2020251030123842.png) | ![](pngs/Pasted%20image%2020251030123909.png) |
| --------------------------------------------- | --------------------------------------------- |
| 設定語言、開始新對話、選擇模型、輸入問題、提交                       | 選擇：地端語言模型==gpt-oss==。推!!!👍                   |

#### 2.3 基本功能快速說明
- **提問**：在輸入框輸入文字並送出，系統即回覆。
- **設定**：在右上角可調整語言、輸出長度等參數。
![](pngs/Pasted%20image%2020251030125718.png)
- **紀錄**：所有對話會自動儲存於左側欄「歷史紀錄」區塊，可以進行**主題**搜尋。🔎

> 以上步驟與官方「Quick Start Guides」相符，具體細節請參考官方文件。

---
### 3. 檔案RAG

- 對話框下可新增檔案、用以精準回答。
- 也可以在右側選取。重新另啟新的問答。
- ==gpt-oss==的提示是可接受10萬個token，同時多個檔案是允許的。

![](pngs/Pasted%20image%2020251030130156.png)

---

### 4. 深入探索 LibreChat 功能

> 官方文件中有「Explore our Documentation」區塊，列出多項進階功能與設定。以下列出主要內容，實際操作請依官方文件逐項閱讀：

- **自訂模型**：上傳或選擇不同的 AI 模型。
- **API 集成**：使用 REST 或 GraphQL API 與內部系統連結。
- **多語言支援**：切換不同語言模式，提升使用者體驗。
- **安全性設定**：設定權限、加密、審計日誌等。

> 這些功能皆在官方文件中有詳細說明，使用時請依照該文件指示。

---

### 5. 故障排除（Troubleshooting）

想知道公司GPU的運轉情況🏃‍♂️🏃‍♀️：
- 每5秒鐘更新 ~ 全年運轉紀錄 &rightarrow; [ganglia](http://master.sinotech-eng.com/graph_all_periods.php?title=gpu_utils&vl=%25&x=&n=&hreg%5B%5D=%5Beng06%2Cl40%5D&mreg%5B%5D=%5Bgpu%5B0%2C1%5D_util&gtype=stack&glegend=show&aggregate=1)
- 每1秒更新之即時狀況(L40) &rightarrow; [nvtop](http://l40.sinotech-eng.com:7681/)
<iframe
src="https://eng06.sinotech-eng.com/ttyd/"
style="width: 100%; min-height: 300px"
frameborder="0">
</iframe>

| 問題       | 可能原因                   | 解決方式                  | 備註  |
| -------- | ---------------------- | --------------------- | --- |
| 無法登入     | 帳號或密碼錯誤                | 重新確認帳號資訊，必要時請 IT 重設密碼 |     |
| 回覆速度慢    | 伺服器負載過高<br>請先看看GPU運轉情況 | 暫停部分功能，或聯繫系統管理員調整資源   |     |
| 對話回覆錯誤   | 模型設定不正確                | 重新設定模型參數或使用預設設定       |     |
| API 呼叫失敗 | 權限不足或網址錯誤              | 檢查 API Key、Endpoint   |     |


::: info
 若上述方式仍無法解決，請撥打內線電話 **08503**，聯絡 **謝天霖**（系統技術支援）以取得即時協助。
:::

---

### 6. 聯絡方式

- 📞**API Key**與**技術支援**：08503（**謝天霖**）  、新增模型：04139(**曠永銓**)
- 🌏**文件與說明**：<https://www.librechat.ai/docs>  
- 🔧**IT 部門**：內部 IT 報修專線(  09025 **王子齊**) 
- 🤝**社群交流**：LibreChat 官方 GitHub 頁面（<https://github.com/LibreChat-AI/librechat.ai>）
- 📚**手冊位址**：[https://eng06.sinotech-eng.com/GiteaTeam.shared/zh/faq/LibreChat](https://eng06.sinotech-eng.com/GiteaTeam.shared/zh/faq/LibreChat/)(陸續發展中🚧)

---

> **注意**：此手冊僅為內部參考，任何具體操作步驟請以官方文件為準。若文件更新，請同步查看官方網站以確保資訊正確。