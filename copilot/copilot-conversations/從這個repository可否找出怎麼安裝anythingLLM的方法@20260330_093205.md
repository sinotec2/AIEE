---
epoch: 1774834325311
modelKey: "gpt-5-mini|github-copilot"
topic: "anythingLLM 安裝方法"



tags:
  - copilot-conversation
---

**user**: 從這個repository可否找出怎麼安裝anythingLLM的方法?
[Context: Notes: NLP/OpenClaw/GroupLecture.md]
[Timestamp: 2026/03/30 09:32:05]

**ai**: 可以。根據庫中筆記，repo 提供了三種主要的部署/啟動方式（node server、docker 生產、desktop），我把重點與步驟摘要如下，並標示出要特別注意的設定與陷阱。

快速概覽（你可以依需求選擇一種方案）
- Node server（直接在主機上以 node 啟動）：適合測試與較簡單的生產部署，文件有完整步驟與啟動指令。[^1]
- Docker（容器化，多個平行實例/端口）：適合生產環境與多實例平行運行，repo 提供 docker-compose 與範例腳本。[^1]
- Desktop（桌面版）：桌面版架構不同、較適合個人使用，仍會有 storage 目錄。[^3]

一、Node server（步驟精要）
1. 取得原始碼：git clone https://github.com/Mintplex-Labs/anything-llm.git。[^1]  
2. 調整 server/.env（非常重要）：
   - 例：SERVER_PORT='https://eng06.sinotech-eng.com:3014'、STORAGE_DIR=/path/to/server/storage、ENABLE_HTTPS='true'、HTTPS_CERT_PATH、HTTPS_KEY_PATH、以及 LLM Provider 與 API keys（OPEN_AI_KEY / ANTHROPIC_API_KEY / LOCAL_AI_BASE_PATH 等）。注意 SERVER_PORT 內容會被伺服器修改掉，每次部署可能要確認/重新設定。[^1][^2]
3. 安裝與編譯：
   - 切換 Node 版本（筆記例子用 v18.20.2），pnpm install。前端要進入 frontend/build（pnpm build），然後把 dist 複製到 server/public。[^1]
   - 典型命令（筆記範例）：
     - nvm use v18.20.2
     - pnpm install (root)
     - cd frontend && pnpm install && pnpm build && cp -r dist ../server/public
     - export NODE_ENV=production
     - cd server && pnpm install && npx prisma generate && npx prisma migrate deploy && node ./index.js
     - cd collector && pnpm install && node index.js
     以上為同時啟動 server 與 collector 的示例流程。[^1][^2]
4. 啟動順序與注意事項：
   - server/index.js 與 collector/index.js 通常都要啟動，index.js 的路徑與啟停可能以絕對路徑管理，關閉時可用 pid 篩選方式處理。啟用 HTTPS 需在 .env 設定並確保憑證檔與 apache2 使用的憑證不同。[^2]

二、Docker / 生產容器（重點）
1. 使用 docker-compose 或多個 container，筆記示範如何透過模板或腳本產生 3001~3014 等端口，並把主機資料夾掛載到容器內的 /app/server/storage（STORAGE_DIR）。[^1]
2. 範例 docker run / docker-compose 片段已在筆記提供（包含 ports、volumes、user 與環境變數範例）。注意 docker 與 apache2 的 https 端口管理、以及 docker 映像內部的 storage 應對主機路徑映射妥當。[^1][^2]

三、Storage 與檔案權限（必讀）
- STORAGE_DIR（server/storage）存放設定、資料庫、模型、向量庫與 documents；第一次 node 執行會產生該目錄。務必設定好 STORAGE_DIR 並檢查檔權限（容器與主機 uid/gid 一致會較方便）。程式會把上傳檔案轉換並以 db 註記儲存，原始檔案不一定會完整保存。[^3]

四、HTTPS、證書與常見陷阱
- 若啟用 HTTPS：在 server/.env 設定 ENABLE_HTTPS='true'、HTTPS_CERT_PATH、HTTPS_KEY_PATH，並注意不能和 apache2 使用同一對證書/金鑰（筆記強調需不同）。另外 note 指出 SERVER_PORT 的格式與 https 前綴處理上要小心（有時伺服器會覆蓋此設定）。[^2]
- Docker + apache2 會有端口/https 衝突問題；在生產環境上常見的作法是讓 docker 在 http ，再由主機上的 apache/nginx 做反向代理及 TLS 終端。[^2]

五、常用運維/啟停腳本範例
- 笔记中有停止 node 的範例（透過 ps grep index.js 再 kill pid），以及 docker 啟停的簡單批次範例（docker run、docker stop 迴圈）。在自動化腳本中注意使用正確的 shell（#!/bin/bash）以支持花式迭代語法。[^1][^2]

補充與建議
- 若要批量新增使用者或做 API 操作，可使用系統提供的 swagger/API key 與 curl 介面（筆記中多處提到管理者產生 API keys 與用 curl 批次操作的做法）。[^1]
- 若要我，把可以自動填入範例 .env 的模板、或把上面 Node 啟動命令整理成可執行的 deploy.sh，我可以幫你產生（請告訴你要用 Node 還是 Docker，以及 STORAGE_DIR 與是否啟用 HTTPS）。

#### Sources
[^1]: [[product_yml]]  
[^2]: [[HttpsEmbChat]]  
[^3]: [[AnyChatStorage]]
[Timestamp: 2026/03/30 09:32:36]