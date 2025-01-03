---
layout: default
title: Redis 的應用
parent: RAG Methodologies
grand_parent: SearchingEngine
nav_order: 99
date: 2024-10-12 
last_modified_date: 2024-10-12 20:32:31
tags: AI chat report
---

# Redis 的應用
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

- 雖然非結構內存資料庫有快速、不精準的強項特性、RAG對語言的精度倒是不如金融資料庫、可以考慮使用。
- 如果能夠同時有個關聯資料庫作為跨session 的資料背景也是很重要。
- 這2類資料庫，前者方案以最簡單的Redis、而後者的方案則以最常見的MySQL作為長期管理。
- 整合搭配起來就如下圖所示。

![Redis and MySQL join service](https://hackmd.io/@cynote/BkobMykLw)
source: [hackmd](https://hackmd.io/@cynote/BkobMykLw)

## Redis 的鍵與值

{% include question.html content="作為RAG系統中的Redis緩存資料庫，其鍵與值會是什麼內容？" %}
- 在 Retrieval-Augmented Generation (RAG) 系統中，Redis 通常作為快取資料庫，用來加速向量檢索和減少對後端資料庫的查詢頻率。在這樣的場景下，Redis 的 鍵（key）和 值（value）會包含以下內容：

### 鍵（Key）

	•	查詢文本或查詢向量的哈希值：RAG 系統中的查詢可能是來自用戶輸入的文本，這些文本會經過向量化後生成一個向量。為了避免存儲過多的冗餘數據，通常會對這個查詢向量進行哈希運算，並將哈希值作為 Redis 的鍵。
	•	例子：query_hash:<query_text_hash> 或 query_vec_hash:<query_vector_hash>

### 值（Value）

	•	檢索結果的編號或 ID：當一個查詢對應於多個文檔檢索結果時，這些文檔的 ID 可以作為查詢的結果儲存在 Redis 中，避免再次向後端資料庫查詢。
	•	例子：一個查詢向量的值可以是相關文檔的 ID 列表，如 [doc_id_1, doc_id_2, doc_id_3]。
	•	相關文檔的向量：在某些情況下，RAG 系統會將向量化的文檔預先緩存，當查詢來臨時，直接從 Redis 中取回相關的文檔向量，而無需重新向量化或檢索。
	•	例子：doc_vec:<doc_id> 可以是文檔的嵌入向量。
	•	檢索結果的具體內容：為了加速生成的速度，RAG 系統也可以緩存檢索出的具體文檔片段或答案，從而省去在每次查詢時重新檢索和組合生成步驟。
	•	例子：response:<query_text_hash> 可能包含之前已生成的完整回答。

### Redis 使用的特性

	•	TTL（Time-to-Live）：Redis 支持設置鍵的過期時間，因此可以設定每個查詢結果的有效期，在這段時間內重複相同查詢可以直接從快取中獲取結果，而無需重新進行檢索和生成。
	•	LRU（Least Recently Used）策略：對於緩存較多內容時，Redis 的 LRU 策略可以幫助釋放空間，確保最常用的數據保持在快取中，提升系統性能。

### 具體應用場景

	1.	加速查詢檢索：如果查詢文本之前已被處理過，系統可以直接從 Redis 中調取結果，避免進行向量化和檢索，縮短響應時間。
	2.	減少向量計算：查詢向量和文檔向量的比對是計算密集型操作，將這些結果緩存在 Redis 中，可以避免頻繁的重複計算。
	3.	優化語義搜索結果：針對某些高頻查詢或重複查詢，預先緩存語義檢索結果，提升搜索系統的整體效能。

總結來說，Redis 在 RAG 系統中用作查詢結果快取，通過存儲查詢向量的哈希、檢索結果的 ID、文檔向量及其他必要資訊，減少了實時計算負荷，顯著提升了系統的查詢效率。

## 鍵的長度

{% include question.html content="Redis 鍵的長度、與內嵌的Token大小有什麼關係？" %}

Redis 鍵的長度與內嵌的 Token 數量之間沒有直接的技術關聯，但其設計仍會受到某些工程實踐和效能需求的影響。以下是相關的探討：

### 1. Redis 鍵的長度

Redis 鍵的長度理論上可以任意長，但實際應用中建議保持鍵的長度在合理範圍內，通常為幾十字元到一百字元。過長的鍵會：

	•	增加內存佔用：Redis 是基於內存運行的系統，長鍵會佔用更多的內存資源。
	•	降低查詢效率：雖然 Redis 是 O(1) 的查找操作，但過長的鍵在內存中會導致更多的比對開銷，特別是大量鍵的情況下。

### 2. 內嵌 Token 的大小

內嵌的 Token 數量主要影響的是文本向量化的結果，而不是直接與 Redis 鍵的長度相關。Token 是模型用來處理文本的最小單位，當你將一個文本向量化時，這些 Token 被模型轉換成一個固定維度的向量。向量的大小與模型的設計有關，而不是與 Redis 的鍵長度直接掛鉤。

### 3. 關鍵影響因素

	•	Hash 或 Key 設計：當我們將文本或其向量儲存在 Redis 中時，通常不會將整個文本作為鍵，而是會生成一個哈希值（如 SHA256）作為鍵。哈希值的長度固定，一般為 32 或 64 字元，這樣可以確保鍵的長度不會因文本長度而顯著增長。
	•	Token 與 Redis Value：向量化後的結果（即值）是多維數據，與 Token 數量有關。例如，更多 Token 會生成更長的向量，這可能導致存入 Redis 的值變得更大。這主要影響到 Redis 的儲存空間和網路傳輸時間，但與鍵的長度無關。

### 4. 實踐建議

	•	鍵長度控制：保持鍵簡潔，例如通過文本哈希或固定長度的唯一識別碼（UUID）作為鍵。
	•	Token 與向量化結果：確保使用有效的向量化方法和壓縮技術，避免生成過大的向量，減少 Redis 的存儲壓力。
	•	頻繁查詢的文本：可以考慮提前向量化並快取結果，以減少每次重新計算的開銷。

總結來說，Redis 鍵的長度與內嵌 Token 的大小之間並無直接聯繫，但在設計時應考慮內存效率、向量化過程中的結果大小，以及如何設計最佳的快取策略來提升查詢性能。

## 官網資訊

- [source](https://redis.io/docs/latest/develop/get-started/rag/)

### Redis 在 RAG 系統中的角色
Redis 提供了強大的即時數據管理平台，能夠支持向量的存儲與檢索，這對於處理大規模的非結構化數據和進行相似性搜索至關重要。Redis 在 RAG 中的主要功能與特點包括：

	1.	向量資料庫：存儲並索引向量嵌入，這些向量語義上代表了非結構化數據的含義。
	2.	語義快取：在 RAG 流程中快取常見問題（FAQ）。透過向量搜索，Redis 能檢索到之前回答過的類似問題，從而降低大型語言模型推理的成本與延遲。
	3.	大型語言模型會話管理器：儲存用戶與大型語言模型之間的對話歷史。Redis 能提取出最近且相關的聊天記錄，為模型提供上下文，進而提高回應的準確性和質量。
	4.	高效能與可擴展性：Redis 以低延遲和高吞吐量著稱，特別適合需要快速數據檢索與生成的 RAG 系統及 AI 代理。

### 使用 Redis 構建 RAG 應用
要使用 Redis 构建 RAG 应用程序，可以按照以下一般步骤進行：

	1.	設定 Redis：首先，設置 Redis 實例並配置它以處理向量數據。
	2.	使用框架：
    	1.	Redis 向量庫 (RedisVL)：RedisVL 強化了生成式 AI 應用程序的開發，能夠有效管理向量和元數據。它允許存儲向量嵌入，並能快速進行相似性搜索，這對於在 RAG 中檢索相關信息非常重要。
    	2.	流行的 AI 框架：Redis 可無縫整合多種 AI 框架和工具。例如，將 Redis 與 LangChain 或 LlamaIndex（構建語言模型的庫）結合，能幫助開發者構建複雜的 RAG 流程。這些整合支持高效的數據管理，並構建實時的 LLM 流程鏈。
    	3.	Spring AI 與 Redis：使用 Spring AI 和 Redis 可以簡化 RAG 應用的構建。Spring AI 提供了結構化的方法來將 AI 能力整合到應用中，而 Redis 則負責數據管理，確保 RAG 流程的高效與可擴展性。
	3.	嵌入並存儲數據：使用合適的模型（如 BERT、GPT）將數據轉換為向量嵌入，並將這些嵌入存儲在 Redis 中，以便基於向量搜索快速檢索。
	4.	整合生成模型：使用生成式 AI 模型，該模型能夠利用檢索到的數據。模型會使用存儲在 Redis 中的向量來增強其生成過程，確保輸出信息與最新的相關數據一致。
	5.	查詢與生成：實現查詢邏輯，根據輸入的提示從 Redis 中檢索相關向量，並將這些向量輸入到生成模型中，生成增強的輸出結果。

### 使用 Redis 構建 RAG 的好處

	•	效率：Redis 的內存數據存儲確保檢索操作能夠以最低的延遲執行。
	•	可擴展性：Redis 可以橫向擴展，無縫處理不斷增長的數據量和查詢需求。
	•	靈活性：Redis 支援多種數據結構，並能與 AI 框架進行整合。

總結來說，Redis 提供了一個強大且高效的平台來實現 RAG。其向量管理能力、高效能和與 AI 框架的無縫整合，使其成為增強生成式 AI 應用並實現實時數據檢索的理想選擇。

## Redis的擴展

Redis的Kubernetes相容性如何？

Redis 與 Kubernetes 具有良好的相容性，尤其是在分佈式環境下進行高效的數據處理時，這種整合被廣泛應用。Redis 可以輕鬆地在 Kubernetes 上部署和管理，幫助應用程序在多個容器中運行，並能充分利用 Kubernetes 的自動擴展、恢復能力和資源管理。以下是 Redis 與 Kubernetes 相容性的一些關鍵點：

	1.	[Redis Operator](https://operatorhub.io/operator/redis-operator):為了簡化 Redis 在 Kubernetes 中的部署與管理，Redis Operator 提供了自動化工具，能夠輕鬆地安裝、擴展、升級和管理 Redis 集群。這些 Operators 可處理 Redis 的高可用性配置，包括主從模式、自動故障轉移等。
	2.	可擴展性：Redis 在 Kubernetes 上具備水平擴展能力，尤其適合處理大規模資料流。Kubernetes 的自動擴展功能允許 Redis 隨著負載的增加或減少動態調整資源分配。
	3.	高可用性與持久性：透過 Kubernetes 的持久性卷（Persistent Volume，PV）和持久性卷聲明（Persistent Volume Claims，PVC），Redis 的數據即使在 Pod 崩潰或重新部署時也能得到保存。這確保了 Redis 的資料持久性，並可以在多個容器間共享數據。
	4.	自動恢復：Kubernetes 提供的自動重啟和重新調度功能，使得 Redis 的部署更具彈性。在容器失敗或意外關閉時，Kubernetes 可以自動恢復 Redis，確保服務不中斷。
	5.	資源隔離和管理：Kubernetes 可以很好地管理 Redis 的 CPU、內存和其他資源，確保每個 Redis 實例能夠獲得足夠的資源，同時避免資源浪費。

這些特性使得 Redis 非常適合在 Kubernetes 環境中運行，無論是高效處理即時數據還是作為快取和數據存儲服務，Redis 都可以在 Kubernetes 上穩定、靈活地運行。

## Terminology

### Spring AI 工程應用框架

- 目前雖然還沒有一個被廣泛採用且明確定義的「Spring AI」框架或工具。但因著各大AI公司介面習慣逐步通用化與標準化，SpringAI也成為Spring框架中最重要的一個專案。
- 早期這個名稱可能來源於與 Spring Framework 整合的 AI 解決方案或自訂的 AI 工具包。
- Spring Framework 是一個常用的 Java 應用開發框架，常與微服務架構結合，適合用來構建大規模應用程式。而在某些場景下，開發者可能使用 Spring 框架來整合 AI 模型與應用邏輯。

如果將「Spring AI」理解為與 Spring Framework 相關的 AI 功能，那麼它所指的是：

	•	在 Spring 應用中整合 AI 模型：將生成式 AI 模型（如 GPT、BERT 等）整合到基於 Spring 的後端服務中，為應用提供智能化功能。
	•	通過 Spring Cloud 或其他微服務技術 將 AI 能力以 API 形式暴露給前端或其他系統。
	•	AI 管道的構建與調用：在 Spring 框架中實現一個完整的 AI 管道，從數據處理、模型推理到結果生成，確保 AI 模型能夠高效運行並與應用其他部分協同工作。

如果「Spring AI」的名稱來源於某些特定的項目或工具包，它可能是某個團隊或社區針對 Spring 框架所開發的 AI 解決方案。

- ref: [AI 趨勢報－科技愛好者的產地,知識貓星球 喵星人  2024/09/22如何使用 Spring AI 打造企業專屬 RAG 知識庫，提升資料管理與查詢效率@104學習精靈](https://nabi.104.com.tw/posts/nabi_post_3cfbd253-f10c-410b-b636-9839d79e0e7f)
- [Spring by VMWare Tanzu](https://spring.io/projects/spring-ai/)