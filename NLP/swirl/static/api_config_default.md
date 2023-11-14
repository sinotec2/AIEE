---
layout: default
title: default
nav_order: 99
layout: default
grand_parent: swirl搜尋引擎
parent: static
date: 2023-11-04
last_modified_date: 2023-11-04 20:37:49
tags: AI chat report
---


# static/api/config/default

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

這個[ JSON 數據](./api_config_default.json)看起來描述了一個表格的結構，其中包括列的信息，結果的佈局，過濾器等等。

這個 JSON 中包含以下信息：

0. "type": "swirl",  "resultType": "hybrid",

1. `resultColumns`: 列的定義，包括 Provider、Title、Author 和 Body。

2. `resultLayout`: 結果的佈局，其中包括標題和主體。

3. `facetLayout`: 過濾器的佈局，這裡只有一個過濾器 "Source"。

4. `jsonFacet`: JSON 過濾器的配置。

5. `defaultFilters`: 默認過濾器的配置。

6. `cart`: 購物車的配置。

7. `msalConfig` 和 `oauthConfig`: 認證配置。

8. `webSocketConfig`: [WebSocket](#websocket) 的配置。

## websocket secure server

- 原始內設
  - `"webSocketConfig": {"url": "ws://localhost:8000/chatgpt-data"}`
- PRODUCTION 建議將ws設為安全連結wss
  - `"webSocketConfig": {"url": "wss://localhost:8000/chatgpt-data"}`
- 如果服務設為對外的ip，則須將localhost改成該ip
  - `"webSocketConfig": {"url": "ws://200.200.32.195:8000/chatgpt-data"}`

## 名詞解釋

### WebSocket

WebSocket（網絡套接字）是一種通信協議，用於實現雙向通信，允許客戶端和伺服器之間建立持久性連接，以便在任何時候進行實時數據傳輸。WebSocket協議的主要特點包括：

1. **雙向通信：** WebSocket允許客戶端和伺服器之間進行雙向通信，而不僅僅是傳統的單向請求-響應模式。這意味著伺服器可以主動向客戶端推送數據，而不需要等待客戶端的請求。

2. **持久性連接：** 一旦建立WebSocket連接，它可以持久存在，無需在每次通信後重新建立。這減少了建立和拆除連接所需的時間和資源。

3. **低延遲：** 由於WebSocket是一個持久性連接，它可以實現低延遲的實時通信，適用於即時聊天、在線遊戲、股票市場報價等場景。

4. **輕量級協議：** WebSocket協議相對輕量級，不像HTTP協議那樣需要在每個請求和響應中包含大量的標頭信息，這降低了通信的開銷。

5. **跨平台支援：** WebSocket協議被現代瀏覽器廣泛支援，並且可以在不同的平台和語言中實現伺服器端。

6. **安全性：** WebSocket可以透過TLS/SSL加密來實現安全通信，保護數據的隱私和完整性。

WebSocket通常用於實現實時應用程序，其中伺服器需要主動向客戶端推送數據，例如在線聊天、實時通知、遊戲多人對戰等。它提供了一種高效、低延遲的方式來實現這些應用程序的要求。

### WebSocketConfig

WebSocketConfig通常是指在使用[WebSocket](#websocket)協議時所需的配置設置。WebSocket是一個用於實現雙向通信的協議，通常用於實時應用程序，例如即時聊天、實時通知和多人遊戲。

WebSocketConfig可能包括以下設置：

1. **WebSocket URL：** 設定WebSocket的URL，這是用於建立WebSocket連接的端點。

2. **通信協議：** WebSocket可以使用不同的通信協議，例如ws（WebSocket）或wss（WebSocket Secure，使用TLS/SSL加密）。根據需要選擇適當的協議。

3. **超時設置：** 設置WebSocket連接的超時時間，以確保在一段時間內未建立連接時不會一直等待。

4. **許可的來源（CORS）：** 如果您的WebSocket服務位於不同的來源（域名）上，您需要設置跨來源資源共用（CORS）規則，以允許跨來源的WebSocket通信。

5. **心跳檢測：** 設置心跳檢測機制，以確保WebSocket連接保持活躍。通常，WebSocket連接會定期發送心跳消息，如果在一段時間內未收到回覆，則視為連接已斷開。

6. **其他自定義配置：** 根據您的應用程序需求，可能需要進一步自定義WebSocketConfig，例如設置消息協議、壓縮設置、驗證機制等。

WebSocketConfig的具體內容和配置方式取決於您的應用程序和使用的WebSocket庫或框架。不同的程式語言和框架可能有不同的方式來配置WebSocket。因此，您應該參考您使用的WebSocket庫的文檔或框架的官方文檔，以了解如何設置WebSocketConfig以滿足您的需求。

[WebSocketConfig](#WebSocketConfig)中的URL範例通常是指[WebSocket](#websocket)連接的端點URL。WebSocket URL的格式通常如下：

```
ws://example.com/socket
```

或者，如果使用WebSocket Secure（加密）：

```
wss://example.com/socket
```

這是一個簡單的WebSocket連接URL示例，其中：

- `ws`表示WebSocket協議，或者在使用安全連接時為`wss`。
- `example.com`是WebSocket服務的主機名或IP地址。
- `/socket`是WebSocket端點的路徑，用於建立WebSocket連接。

您可以根據您的實際應用程序需求和WebSocket服務的配置來調整這個URL。確保WebSocket URL正確指向您希望建立連接的WebSocket服務端點。

請注意，具體的WebSocket URL範例取決於您的應用程序和WebSocket服務的設定，因此請參考您的WebSocket服務提供商或您正在使用的WebSocket庫的文檔，以獲得更具體的URL示例和配置信息。

### 如何開啟wss服務

要建立一个 WebSocket 安全服务器，你可以按照以下步骤进行操作。WebSocket 安全通常使用 TLS/SSL 加密来保护数据传输。下面是一个使用 Python 的示例，使用 `websockets` 库来创建 WebSocket 安全服务器。

1. **安装 websockets 库**：

   在 Python 中，你可以使用 `websockets` 库来创建 WebSocket 服务器。首先，确保你已经安装了这个库：

   ```bash
   pip install websockets
   ```

2. **创建 WebSocket 服务器代码**：

   创建一个 Python 脚本，以设置 WebSocket 安全服务器。以下是一个示例代码：

   ```python
   import asyncio
   import websockets
   import ssl

   # 生成 SSL/TLS 上下文
   ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
   ssl_context.load_cert_chain('your_cert.pem', 'your_key.pem')

   async def echo(websocket, path):
       async for message in websocket:
           await websocket.send(message)

   start_server = websockets.serve(
       echo, "0.0.0.0", 8765, ssl=ssl_context
   )

   asyncio.get_event_loop().run_until_complete(start_server)
   asyncio.get_event_loop().run_forever()
   ```

   请将 `'your_cert.pem'` 和 `'your_key.pem'` 替换为你的 SSL/TLS 证书和私钥文件的路径。确保你已经获得了有效的证书，或者可以使用自签名证书进行测试。

3. **运行 WebSocket 服务器**：

   运行你的 WebSocket 安全服务器脚本：

   ```bash
   python your_server.py
   ```

   服务器将在指定的端口上启动，等待 WebSocket 连接。

4. **建立 WebSocket 客户端**：

   为了测试你的 WebSocket 服务器，你可以创建一个 WebSocket 客户端。可以使用 JavaScript、Python 或其他编程语言来创建客户端，以确保服务器正常运行并可以接受安全连接。

请注意，上述示例中的证书和密钥文件是必需的，以确保通信是安全的。在生产环境中，你应该获得有效的 SSL/TLS 证书以保护通信。此外，你可能需要在防火墙上打开相应的端口，以允许 WebSocket 流量进入服务器。

这只是一个简单的示例，你可以根据自己的需求扩展 WebSocket 服务器的功能和安全设置。WebSocket 安全通信对于需要保护数据隐私和安全性的应用程序非常重要。