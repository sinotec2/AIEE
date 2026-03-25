---
epoch: 1773637491059
modelKey: "gpt-5-mini|github-copilot"
topic: "Vault Keycloak OpenClaw 流程圖"



tags:
  - copilot-conversation
---

**user**: 從資訊流的角度給這篇一個流程圖，說明vault、keycloak以及openclaw的關係
[Context: Notes: utilities/OpsChatUI/OpenClawVerChain.md]
[Timestamp: 2026/03/16 13:04:51]

**ai**: 根據你在 [[OpenClawVerChain]] 的設計，下面給出一個從「資訊流」角度的流程圖（Mermaid）與簡要說明。你可以把這段 Mermaid 放進 Obsidian note 直接渲染，或複製成圖嵌入文件。

Mermaid 流程圖
```mermaid
flowchart LR
  U[使用者 (桌機/同仁)] -->|1. 啟動登入 (browser)| OC[OpenClaw / local agent]
  OC -->|2. 導向 Keycloak (Auth Code + PKCE)| KB[Keycloak (IdP, AD/LDAP + MFA)]
  KB -->|3. 完成驗證並回傳 OIDC tokens| OC
  OC -->|4. 用 OIDC token 呼叫 Vault OIDC auth| V[Vault (Auth & Secrets)]
  V -->|5. 驗證 token & claims → 發放短效 Vault token| OC
  OC -->|6a. 用 Vault token 取 KV secrets| V
  OC -->|6b. 用 Vault token 取短效 PKI / 證書| V
  OC -->|6c. 用 Vault transit 做簽章/加解密| V
  OC -->|7. 使用 secrets/憑證 呼叫內部系統| S[內部系統 / Third-party (MIS, Files, Gateway)]
  V -->|audit logs| AL[SIEM / 集中日誌]
  V -->|token revoke / TTL expire| OC
  KB -->|group/claims -> mapped into token| V
```

對應步驟說明（對應圖中編號）
- 1. 使用者在桌機啟動 OpenClaw（或 sidecar agent）。OpenClaw 觸發瀏覽器導向 Keycloak 進行 OIDC Authorization Code + PKCE 流程。  
- 2–3. 使用者在 Keycloak 完成公司帳號驗證（AD/LDAP）與 MFA（TOTP/Push/WebAuthn），Keycloak 回傳短效 OIDC tokens（ID token / access token），token 內應含 groups/claims。  
- 4. OpenClaw 將 OIDC token 送到 Vault 的 OIDC auth endpoint，請求換取 Vault token。  
- 5. Vault 驗證 OIDC token（簽名、audience、到期、claims/groups），根據對映關係（Keycloak groups -> Vault role/policy）簽發短效、可撤銷的 Vault token（例如 TTL 15–60 分鐘）。  
- 6. OpenClaw 使用 Vault token 取所需資源：  
  - KV v2：讀取 API keys、第三方憑證（只在記憶體使用，不落地）；  
  - PKI：簽發短效 mTLS 憑證（若採用）；  
  - Transit：要求 Vault 進行簽章或加解密（私鑰不落地）。  
- 7. OpenClaw 用取得的 secrets/證書去存取內部系統（MIS、檔案系統、gateway、第三方 API）。整個過程中不把長效 secrets 存在本機檔案。  
- 補充：所有 Vault 的存取與失敗都寫入 audit log，送到 SIEM/集中日誌；若 Vault token 到期或被撤銷，OpenClaw 要麼向 Vault renew（若 policy 允許），要麼回到 Keycloak 重新驗證（步驟 1）。

重點與註記（設計上的關鍵）
- Token 流向：Keycloak → OpenClaw（OIDC token）→ Vault → OpenClaw（Vault token）→ Secrets → 內部系統。  
- 最小權限：Vault role/policy 依專案/環境切分，OpenClaw 只能讀自身需要的路徑，無 list 全庫權限。  
- 短效 & 不落地：Vault token 與 secrets 都短效、只放記憶體或受控快取（TTL），避免長效憑證留在 endpoint。  
- 可稽核／可撤銷：Vault 的 audit 與 revoke 機制是關鍵；若被入侵能快速撤銷 Vault token 或撤銷 PKI 證書。  
- 可替換 agent 模式：OpenClaw 可直接內建 OIDC 加換 token，也可用本機 sidecar/agent 負責 auth 與 secrets 保管。

如果你想要我把這張流程圖擴充成：
- 序列圖（顯示時間軸、request/response 與錯誤處理），或
- 權限對照表（Keycloak claims → Vault role/policy → KV 路徑），

告訴我你偏好哪一種，我會根據 [[OpenClawVerChain]] 裡的細節產出對應圖表或表格。
[Timestamp: 2026/03/16 13:05:31]

**user**: 哈哈，你犯了典型的錯誤，mermail的半形括弧是保留給內部使用的。請重作。
[Context: Notes: utilities/OpsChatUI/OpenClawVerChain.md]
[Timestamp: 2026/03/16 13:06:50]

**ai**: 抱歉，弄錯了。已把所有半形括弧換成全形括弧並重作流程圖（依據 [[OpenClawVerChain]] 內容），直接貼到 Obsidian 的 Mermaid 區塊可渲染：

Mermaid 流程圖
```mermaid
flowchart LR
  U[使用者（桌機／同仁）] -->|1. 啟動登入（browser）| OC[OpenClaw／local agent]
  OC -->|2. 導向 Keycloak（Auth Code ＋ PKCE）| KB[Keycloak（IdP、AD／LDAP ＋ MFA）]
  KB -->|3. 完成驗證並回傳 OIDC tokens| OC
  OC -->|4. 用 OIDC token 呼叫 Vault OIDC auth| V[Vault（Auth ＆ Secrets）]
  V -->|5. 驗證 token 與 claims → 發放短效 Vault token| OC
  OC -->|6a. 用 Vault token 取 KV secrets| V
  OC -->|6b. 用 Vault token 取短效 PKI／證書| V
  OC -->|6c. 用 Vault transit 做簽章／加解密| V
  OC -->|7. 使用 secrets／憑證 呼叫內部系統| S[內部系統／第三方（MIS、Files、Gateway）]
  V -->|寫入 audit logs| AL[SIEM ／ 集中日誌]
  V -->|token 被撤銷 或 TTL 到期| OC
  KB -->|groups／claims 映射 → Vault role／policy| V
```

簡要說明（對應圖中步驟）
- 1：使用者啟動 OpenClaw（或 local agent），觸發瀏覽器登入流程。  
- 2–3：Keycloak（連 AD／LDAP 並強制 MFA）完成 OIDC Authorization Code ＋ PKCE，回傳短效 OIDC token（含 groups/claims）。  
- 4–5：OpenClaw 用 OIDC token 向 Vault 的 OIDC auth 端點換取短效、可撤銷的 Vault token（Vault 驗證簽章、audience、claims）。  
- 6：OpenClaw 使用 Vault token 取需要的資源：KV（API key 等）、PKI（短效憑證）、Transit（簽章／加解密）。  
- 7：OpenClaw 用取到的 secrets／憑證去呼叫內部系統或第三方服務，全程避免長效 secrets 寫到磁碟。  
- 補充：Vault 的所有存取會寫入 audit logs（送 SIEM），若 token 被撤銷或 TTL 到期，OpenClaw 要 renew（若允許）或重新走 Keycloak 流程。

要我接著產出哪一種擴充視覺化？
- 序列圖（顯示 request／response 與錯誤處理）  
- 權限對照表（Keycloak claims → Vault role／policy → KV 路徑）

選一個我就幫你做。
[Timestamp: 2026/03/16 13:07:21]