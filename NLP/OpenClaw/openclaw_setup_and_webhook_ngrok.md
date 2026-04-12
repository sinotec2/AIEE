OpenClaw 安裝、設定與 LINE webhook (ngrok) 工作流程筆記

目的
- 在 4c / 8GB / 200GB VM 上部署 OpenClaw Gateway，並以 ngrok 暴露 HTTPS endpoint 以接受 LINE webhook（開發 / 測試模式）。
- 提供可執行步驟、範例程式、ngrok 使用方法、安全檢查與後續改進建議（轉 production 使用 Cloudflare Tunnel / 自有域名 + Caddy）。

架構概覽
- OpenClaw Gateway (container 或 systemd service)
- Reverse proxy: Caddy（生產建議）或開發可省略
- Webhook 暴露: ngrok（開發/測試）
- Message integrations: LINE (外)、Mattermost (內)
- Local model runtime: vLLM (小體量模型, 僅作 POC)
- Storage: /var/lib/openclaw 或 workspace（logs、uploads、vecdb）

先決條件
- 有一台可操作的 VM (4 cores, 8GB RAM, 200GB disk)
- 建議 OS: Ubuntu 22.04+（範例指令以 Linux 為主）
- 有 GitHub/registry 帳號（若要安裝或上傳 artifact）
- ngrok 帳號 (選用；免費可用但 URL 非固定)
- LINE developer account (channel secret, channel access token)

快速流程摘要（步驟概覽）
1) 在 VM 安裝必要套件 (docker, docker-compose, python3, pip)
2) 部署 OpenClaw (container 或 binary)
3) 寫一個簡單 webhook handler（Flask 範例在下方）並在本機啟動 (localhost:8080)
4) 安裝 ngrok 並啟動隧道：ngrok http 8080 → 取得 HTTPS URL
5) 在 LINE Developer Console 設定 webhook URL 為 ngrok 給的 https://.../line/webhook
6) 測試 webhook，確保 X-LINE-SIGNATURE 驗證通過
7) 將設定與腳本收整成部署筆記，未來轉 production 換成 Cloudflare Tunnel + Caddy

詳細步驟
A. 系統準備（Ubuntu 範例）
- 更新系統
  sudo apt update && sudo apt upgrade -y
- 安裝必要工具
  sudo apt install -y git curl unzip python3 python3-venv python3-pip
- 安裝 docker (若要用 container)
  curl -fsSL https://get.docker.com -o get-docker.sh
  sudo sh get-docker.sh
  sudo usermod -aG docker $USER
- 安裝 ngrok (CLI)
  # 下載後解壓並放到 /usr/local/bin
  curl -sSL https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -o ngrok.zip
  unzip ngrok.zip && sudo mv ngrok /usr/local/bin/
  # 登入（若有 account）
  ngrok authtoken <YOUR_NGROK_AUTH_TOKEN>

B. OpenClaw 部署（簡述）
- 若使用 docker-compose，建議把 openclaw 配置置於 docker-compose.yml 並啟動
- 參考本地 docs 與 openclaw 官方安裝文件完成 gateway 初始化與配置
- 把 gateway 的 webhook route 設定好（例如 /webhook/line 或 /line/webhook）

C. 實作 webhook handler (Flask 範例)
- requirements: flask
- app.py 範例：
```python
from flask import Flask, request, abort
import hmac, hashlib, base64, os

CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET", "<CHANNEL_SECRET>")

app = Flask(__name__)

def verify_signature(body, signature):
    hash = hmac.new(CHANNEL_SECRET.encode('utf-8'), body, hashlib.sha256).digest()
    expected = base64.b64encode(hash).decode()
    return hmac.compare_digest(expected, signature)

@app.route("/line/webhook", methods=["POST"])
def line_webhook():
    body = request.get_data()
    signature = request.headers.get('X-LINE-SIGNATURE', '')
    if not verify_signature(body, signature):
        abort(401)
    print("LINE event:", body.decode('utf-8'))
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```
- 啟動示範
  export LINE_CHANNEL_SECRET="..."
  python3 app.py

D. 啟動 ngrok 並取得公開 URL
- ngrok http 8080
- ngrok 介面會印出 Forwarding HTTPS URL，例如 https://abcd-1234.ngrok.io

E. 設定 LINE Developer Console
- Webhook URL: https://{ngrok_subdomain}/line/webhook
- 啟用 webhook，將 channel secret / access token 設入 OpenClaw 或您的 handler 環境變數

F. 測試與驗證
- 在 LINE console 使用「send test」或直接由 LINE app 觸發 event
- 查看 Flask log，確保簽章驗證通過，且事件內容被記錄

安全與運維注意事項
- 永遠驗證 X-LINE-SIGNATURE（不要只靠來源 IP）
- 限制 endpoint 只接受 POST，檢查 content-type
- log 控制：不要把 channel access token 或 secrets 打到公開 log
- 使用 basic auth 或臨時 header token 作第二道防護（開發時可用）
- ngrok 免費 URL 非固定；若需要長期穩定請升級或切換到 Cloudflare Tunnel
- 紀錄 provenance（每個 webhook 事件的 body hash、signature、處理結果與處理時間）以便稽核

從 ngrok 過渡到 production 的建議
- 更換為 Cloudflare Tunnel（free tier）或使用自有域名 + Caddy（自動 TLS）
- 使用 Cloudflare Access 做 identity 層保護，或在 edge 設 IP allowlist
- 對 webhook 程式增加 rate limit、replay protection（timestamp/nonce）、以及更完整的 observability (metrics, traces)

附錄：常用命令快速清單
- 啟動 Flask test server
  export LINE_CHANNEL_SECRET="..."
  python3 app.py
- 啟動 ngrok
  ngrok http 8080
- 檢視 ngrok web UI (流量/requests)
  http://127.0.0.1:4040

下一步建議
- 若您要我把這份筆記放到 repo（已完成），或在 VM 上直接部署實作（需要 SSH/sudo 權限），請告訴我哪一項要我執行：
  - 在 VM 上實際啟動 Flask + ngrok（需授權）
  - 產出一份可執行的 bash 腳本與 README（放在 repo）
  - 幫您把 ngrok 測試流程整合到 OpenClaw 的本地 dev config

