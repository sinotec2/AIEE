---
title: OpenClaw Authentication Flow
tags: AI
layout: default
parent: OpsChatUI
grand_parent: Utilities
date:  2026-03-03 
modify_date: 2026-03-03 08:37
---

# 因應 OpenClaw 的認證串流（Authentication Flow）技術筆記（討論稿）
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

> 目標：在「暴露性高、桌機跑容器、網路常重整」的環境下，讓 **身分驗證可反覆、可稽核、可撤銷**，並把 **token/secrets 不落地、短效化**，降低被植入程式後的爆炸半徑。  
> 核心選擇：**不自寫 broker**；改用 **Keycloak 當身分入口（含 MFA）**，**Vault 當 secrets/憑證與授權中心**。

---

## 1. 背景與威脅模型（對齊共識用）
### 現況假設
- OpenClaw 在同仁桌機上以容器方式運行（單機、非 K8s 為主）。
- 裝置/內部服務之間有輪轉 JWT（既有機制）。
- Gateway 對外/對內仍有部分靜態憑證或固定連線憑證。
- 需要串接：內部檔案系統、專案系統、MIS 系統等 API，並管理大量 token / key / secret。
- 公司網路一天重整 3–4 次（可接受重新登入/重新取票的使用習慣）。

### 最擔心的風險
- 桌機或容器環境被植入程式（malware) 後，竊取本機檔案中的 secrets 或攔截 token。
- 因此要做到：
  - **不把長效 secrets 放在檔案**
  - **憑證/令牌短效化 + 可撤銷**
  - **最小權限 + 可稽核**

---

## 2. 設計原則（本筆記的「不變」）
1) **身分與 secrets 分層**  
- Keycloak：處理「人是誰」「是否完成 MFA」「群組/角色」  
- Vault：處理「可拿哪些 secrets」「短效 token」「審計」「輪替/撤銷」

2) **短效、可續期、可撤銷（Short-lived & Revocable）**  
- 網路重整 = 自然觸發重新驗證，反而是優勢（縮短攻擊者可用時間窗）。

3) **Secrets 不落地（No secrets at rest on endpoints）**  
- 不寫進 repo、image、env 檔、共享資料夾。
- 容器拿到 secrets 後只放記憶體；必要時用本機 OS keychain/受控快取（有 TTL）。

4) **最小權限（Least privilege）與分區（Project/Env segmentation）**  
- 以「專案、環境（dev/stg/prod）、角色（read/deploy/admin）」切 policy。

---

## 3. 元件與責任分工（建議藍圖）
### 3.1 Keycloak（Identity Broker / IdP）
- 對接公司帳密系統（AD/LDAP）作為權威身份來源。
- 提供 OIDC/OAuth2 登入流程。
- 強制 MFA（例如 TOTP/Push/WebAuthn，視公司現況）。
- 將 AD 群組/屬性映射成 Keycloak 的 claims（例如 `groups`, `dept`, `role`）。

### 3.2 Vault（Secrets & Credential Authority）
- **KV v2**：集中儲存靜態 secrets（第三方 API key、MIS token、gateway client secret 等）。
- （可選）**PKI**：簽發短效服務憑證（mTLS），取代長效憑證散落。
- （可選）**Transit**：集中保管簽章/加解密金鑰（例如 JWT signing key 不落地）。
- **OIDC Auth Method**：接受 Keycloak 簽發的 token 來換取 Vault token。
- **Audit log**：所有讀取/簽發/失敗都留痕，送 SIEM 或集中日誌。

### 3.3 OpenClaw（桌機容器端）
- 不保存長效 token。
- 透過「互動式登入」或「device flow」取得 Keycloak 身分，再向 Vault 換短效 Vault token。
- 使用 Vault token 取得必要 secrets/憑證後啟動工作；token 到期需續期或重新登入。

---

## 4. 建議的「認證串流」主流程（人→Keycloak→Vault→Secrets）
以下是一個可討論、可落地的標準流程（最推薦先做這條）：

### Flow A：互動式（同仁桌機操作、可接受常登入）
1. **使用者啟動 OpenClaw 容器/CLI**
2. OpenClaw 觸發登入：
   - 開 browser 導向 Keycloak（OIDC Authorization Code + PKCE）
   - 使用者輸入公司帳密並完成 MFA
3. Keycloak 回傳短效 OIDC token（ID token / access token）
4. OpenClaw（或本機 sidecar/agent）拿 token 呼叫 Vault 的 **OIDC auth** 端點
5. Vault 驗證 token（簽章、audience、到期、groups/claims），簽發 **短效 Vault token**（TTL 例如 15–60 分鐘，視情境）
6. OpenClaw 用 Vault token 取得：
   - KV secrets（API keys / tokens）
   - 或短效憑證（PKI）
   - 或進行簽章/加密（Transit）
7. OpenClaw 執行任務；網路重整或 TTL 到期：
   - 優先嘗試 token renew（若允許）
   - 不可 renew 或失敗就回到步驟 2 重新登入

**你們公司一天 3–4 次網路重整**，此 flow 剛好把「重新驗證」變成常態安全習慣。

---

## 5. 路徑規劃與授權模型（同仁好討論的部分）
### 5.1 Vault KV 命名建議（示例）
- `kv/openclaw/{env}/{project}/integrations/{system}`  
  例：  
  - `kv/openclaw/prod/projA/integrations/mis`  
  - `kv/openclaw/stg/projA/integrations/filesvc`

### 5.2 Policy 原則
- 同一個容器/專案身分只能讀自己的路徑（不能 list 全庫）。
- 將「讀 secrets」「寫/輪替 secrets」「管理 policy」拆成不同角色。
- 生產環境（prod）與其他環境隔離：不同 role、不同 policy、最好不同 mount 或不同 namespace（若有）。

### 5.3 Keycloak → Vault 群組映射
- Keycloak token 內含 `groups`（從 AD 群組映射而來）
- Vault OIDC role 依 `groups` 綁定 policy  
  - `openclaw-projA-read` → 只讀 projA 所需 secrets  
  - `openclaw-admin` → 管理類權限（嚴格控管）

---

## 6. 針對你們特定議題的對應策略
### 6.1 「Gateway 仍是靜態」怎麼過渡
- Phase 1：先把 gateway 靜態 secret 收進 KV，由 Vault 管控讀取與稽核
- Phase 2：把 gateway 認證改為短效：
  - 能做 mTLS 就上 PKI（短效憑證、可撤銷）
  - 或改成由內部頒發短效 access token（由 IdP/授權服務發）

### 6.2 「內部 devices 輪轉 JWT」怎麼銜接
- 若 JWT 是你們自簽：考慮把 signing key 交給 Vault Transit，服務用 API 請 Vault 簽章（私鑰不落地）
- 若 JWT 是由 Keycloak/IdP 發：可直接用 OIDC/JWT 當身分，再換 Vault token（同上 Flow A）

---

## 7. 推行策略（避免一開始就變大工程）
### Phase 1（2–4 週目標）：先把「檔案 secrets」消滅
- 上 Vault（含 TLS + audit）
- KV v2 收納現有 secrets
- Keycloak/OIDC auth 打通（最小角色與 policy）
- OpenClaw 改為啟動時從 Vault 取 secrets（不落地）

### Phase 2：短效化與最小權限深化
- Vault token TTL/renew 策略定稿
- policy 依專案/環境切細
- 將高權限操作改成必須互動 MFA（透過 Keycloak 的強制策略）

### Phase 3：動態憑證/PKI/Transit（視需求上）
- mTLS/PKI、Transit、（若需）資料庫動態帳密等

---

## 8. 需同仁一起決策的「參數表」（會影響落地）
1) Vault token TTL：15/30/60 分鐘？是否允許 renew？  
2) secrets 取得方式：OpenClaw 內建 OIDC 登入？或外掛本機 agent？  
3) Keycloak MFA 方式：TOTP/Push/WebAuthn 哪個可行？  
4) 專案/環境切分規則：命名、路徑、群組對應

---

## 9. 一句話總結（方便會議開場）
用 **Keycloak + MFA** 統一「人」的身分入口，再用 **Vault** 統一管理所有系統 token/secrets（短效、可稽核、最小權限），讓 OpenClaw 在桌機容器上也能做到「不存檔、不長效、可重登」的安全串流。

---
## TODO
- 把上面 Flow A 具體化成「序列圖 + 權限對照表」（Keycloak claims → Vault role/policy → KV 路徑），
- 規劃預計環境分層（dev/stg/prod 有沒有）以及大概有哪些系統（MIS/檔案/專案/第三方）要接。
