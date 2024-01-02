---
layout: default
title: openai_api_server
parent: FastChat
grand_parent: 自然語言處理
nav_order: 99
date: 2024-01-02
last_modified_date: 2024-01-02 14:30:00
tags: AI chat API_server
---


# openai_api_server程式說明
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

## subroutines

```python
kuang@DEVP ~/MyPrograms/FastChat

$ py=./fastchat/serve/openai_api_server.py

$ grep 'class ' $py
class AppSettings(BaseSettings):

$ grep 'def ' $py
async def check_api_key(
def create_error_response(code: int, message: str) -> JSONResponse:
async def validation_exception_handler(request, exc):
async def check_model(request) -> Optional[JSONResponse]:
async def check_length(
def check_requests(request) -> Optional[JSONResponse]:
def process_input(model_name, inp):
async def get_gen_params(
async def get_worker_address(model_name: str, client: httpx.AsyncClient) -> str:
async def get_conv(model_name: str, worker_addr: str):
async def show_available_models():
async def create_chat_completion(request: ChatCompletionRequest):
async def chat_completion_stream_generator(
async def create_completion(request: CompletionRequest):
async def generate_completion_stream_generator(
async def generate_completion_stream(payload: Dict[str, Any], worker_addr: str):
async def generate_completion(payload: Dict[str, Any], worker_addr: str):
async def create_embeddings(request: EmbeddingsRequest, model_name: str = None):
async def get_embedding(payload: Dict[str, Any]):
async def count_tokens(request: APITokenCheckRequest):
async def create_chat_completion(request: APIChatCompletionRequest):
def create_openai_api_server():
```

函式名稱|input|output
-|-|-
check_api_key (API key 的有效性檢查)|`auth`: 一個由`HTTPAuthorizationCredentials` 決定的選項`Options`，預設值是由 `get_bearer_token` 函式提供的。|
create_error_response|`code`: 整數，代表錯誤的程式碼或類型。用來指示錯誤的種類。/`message`: 字串，包含有關錯誤的描述性訊息。用來解釋發生了什麼錯誤。| `JSONResponse` 物件，其中包含了一個符合特定格式的 JSON 格式的錯誤回應。/HTTP 狀態碼為 400（Bad Request）請求有誤|建立符合特定格式的 JSON 錯誤回應
validation_exception_handler|`request`: 代表發送請求的相關資 /`exc`: 是捕獲到的 `RequestValidationError` 例外情況的實例|
check_model(異步路由操作，主要用於檢查模型是否有效)|`request`: 包含模型資訊的請求對象|如果模型無效，返回建立的錯誤回應；否則返回 `None`，表示模型有效|
check_length(輸入長度 是否符合模型)|request,prompt,max_tokens,worker_addr,client|通過則返回 `None`、否則錯誤訊息|
check_requests|request、`max_tokens`、`n`、`temperature`、`top_p`、和 `stop`|通過則返回 `None`、否則錯誤訊息|

### check_api_key

這是一個用於建立錯誤回應的輔助函式，主要是為了方便建立符合特定格式的 JSON 錯誤回應。以下是這個函式的中文說明：

#### 輸入：

- `code`: 整數，代表錯誤的程式碼或類型。用來指示錯誤的種類。
- `message`: 字串，包含有關錯誤的描述性訊息。用來解釋發生了什麼錯誤。

#### 輸出：
- 返回一個 `JSONResponse` 物件，其中包含了一個符合特定格式（可能是定義的 `ErrorResponse` 類型）的 JSON 格式的錯誤回應。
- HTTP 狀態碼為 400（Bad Request），表示請求有誤。

#### 重要的程式邏輯：
1. 使用 `ErrorResponse` 類型建立一個包含錯誤訊息和程式碼的 JSON 物件。
2. 使用 `JSONResponse` 類型將 JSON 物件轉換為 HTTP 響應。
3. 設定 HTTP 狀態碼為 400，表示請求有誤。

簡而言之，這個函式的目的是提供一個統一的方式來建立錯誤回應，確保它們符合特定的 JSON 格式，並具有一致的 HTTP 狀態碼。

### create_error_response

這是一個用於建立錯誤回應的輔助函式，主要是為了方便建立符合特定格式的 JSON 錯誤回應。以下是這個函式的中文說明：

#### 輸入：

- `code`: 整數，代表錯誤的程式碼或類型。用來指示錯誤的種類。
- `message`: 字串，包含有關錯誤的描述性訊息。用來解釋發生了什麼錯誤。

#### 輸出：

- 返回一個 `JSONResponse` 物件，其中包含了一個符合特定格式（可能是定義的 `ErrorResponse` 類型）的 JSON 格式的錯誤回應。
- HTTP 狀態碼為 400（Bad Request），表示請求有誤。

#### 重要的程式邏輯：

1. 使用 `ErrorResponse` 類型建立一個包含錯誤訊息和程式碼的 JSON 物件。
2. 使用 `JSONResponse` 類型將 JSON 物件轉換為 HTTP 響應。
3. 設定 HTTP 狀態碼為 400，表示請求有誤。

簡而言之，這個函式的目的是提供一個統一的方式來建立錯誤回應，確保它們符合特定的 JSON 格式，並具有一致的 HTTP 狀態碼。

### validation_exception_handler

這是一個 FastAPI 應用程式中用來處理 `RequestValidationError` 例外情況的異常處理程序。以下是這個異常處理程序的中文說明：

1. 當應用程式捕獲到 `RequestValidationError` 例外情況時，將呼叫這個異常處理程序。
2. `validation_exception_handler` 函式接受兩個參數：`request` 和 `exc`。
   - `request`: 代表發送請求的相關資訊。
   - `exc`: 是捕獲到的 `RequestValidationError` 例外情況的實例。
3. 使用 `create_error_response` 函式建立一個符合特定格式的 JSON 錯誤回應。
   - 傳遞 `ErrorCode.VALIDATION_TYPE_ERROR` 作為錯誤程式碼，表示這是一個與請求驗證相關的錯誤。
   - `str(exc)` 作為錯誤訊息，將 `RequestValidationError` 的詳細錯誤描述轉換為字串。
4. 返回建立的 JSON 錯誤回應。

簡而言之，這個異常處理程序的目的是在請求驗證錯誤時返回一個統一格式的錯誤回應，使客戶端能夠理解並處理錯誤。

### check_length

這是一個異步的 FastAPI 路由操作，用來。以下是這個函式的中文說明：

#### 輸入：

1. `request`: 包含請求資訊的對象。
2. `prompt`: 字串，代表模型的輸入提示。
3. `max_tokens`: 整數，代表模型的最大令牌數。
4. `worker_addr`: 字串，代表模型工作服務器的地址。
5. `client`: `httpx.AsyncClient` 實例，用於進行異步的 HTTP 請求。

#### 重要的程式邏輯：

1. 使用 `client` 向模型工作服務器發送 `model_details` 請求，以獲取模型的上下文長度（`context_len`）。
2. 使用 `client` 向模型工作服務器發送 `count_token` 請求，以獲取給定提示（`prompt`）的令牌數量（`token_num`）。
3. 檢查 `token_num + max_tokens` 是否超過模型的上下文長度（`context_len`）。
   - 如果超過，則建立一個錯誤回應，指示使用者減少輸入的長度。
   - 如果未超過，則返回 `None`，表示輸入長度驗證通過。

#### 輸出：

- 如果輸入長度驗證通過，則返回 `None`。
- 如果輸入長度超過模型限制，則返回一個符合特定格式的 JSON 錯誤回應，提供相應的錯誤訊息。

### check_requests

這是一個用於檢查請求參數的函式，主要用於確保參數的合法性。以下是這個函式的中文說明：

1. `check_requests` 函式接受一個 `request` 參數，代表應用程式的請求。
2. 函式檢查 `request` 中的各個參數，包括 `max_tokens`、`n`、`temperature`、`top_p`、和 `stop`。
3. 如果任何一個參數不符合特定的條件，函式將使用 `create_error_response` 函式建立一個錯誤回應，並返回該回應。
   - 例如，如果 `max_tokens` 小於等於 0，則會建立一個錯誤回應，表示該參數超出了合理範圍。
4. 如果所有參數都是合法的，函式將返回 `None`，表示沒有錯誤。

簡而言之，這個函式確保請求中的參數都在合法的範圍內，如果有不合法的情況，則返回一個符合特定格式的錯誤回應，以便客戶端能夠理解和處理錯誤。