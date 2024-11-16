
> RAPTOR （Recursive Abstractive Processing for Tree-Organized Retrieval）

- [RAPTOR 一种基于树的RAG方法，RAG的准确率提高 20%](https://www.cnblogs.com/xiaoqi/p/18060281/RAPTOR)
- [arxiv](https://arxiv.org/abs/2401.18059)
- [GitHub Official](https://github.com/parthsarthi03/raptor)

## LawDB Suggest

> 為了便於查詢法規、契約等文件的資料庫，設計時需要考慮文件的結構、查詢需求、版本控制、全文檢索等功能。以下是一個基本的設計思路：

1. 資料庫架構設計

(1) Document Table（文件表）

	•	用於儲存每份文件的基本資訊。
	•	欄位：
	•	document_id：主鍵，唯一識別每份文件
	•	title：文件標題（例如：法規名稱、契約名稱）
	•	type：文件類型（例如：法規、契約、備忘錄）
	•	description：文件描述或簡要說明
	•	status：文件狀態（如有效、廢止、草案）
	•	version：文件版本號
	•	created_date：文件建立日期
	•	last_updated：文件最後更新日期

(2) Section Table（段落表）

	•	法規或契約通常分為章節條款，因此需要將文件的章節條款分段存儲，以便快速定位與查詢。
	•	欄位：
	•	section_id：主鍵，唯一識別每個段落
	•	document_id：外鍵，指向 Document 表
	•	section_number：段落編號或標題（例如：第1章、第1條）
	•	content：段落內容（條款或章節文字）
	•	parent_id：指向父章節的段落 ID（便於形成層次結構）
	•	order：用於排序段落的順序

(3) Keyword Table（關鍵字表）

	•	針對常用關鍵字或法規條款中的關鍵術語進行存儲，便於查詢特定關鍵字的出現位置。
	•	欄位：
	•	keyword_id：主鍵
	•	keyword：關鍵字
	•	section_id：外鍵，指向段落表
	•	frequency：關鍵字在該段落中出現的次數

(4) Cross Reference Table（交叉引用表）

	•	法規和契約中經常有條文的交叉引用，因此需要記錄引用關係。
	•	欄位：
	•	reference_id：主鍵
	•	document_id：外鍵，指向 Document 表
	•	source_section_id：引用來源段落
	•	target_section_id：引用目標段落

2. 索引與全文檢索

為了提高查詢效率，應考慮為關鍵欄位建立索引：
	•	為 title、section_number 和 keyword 欄位建立索引。
	•	若資料庫支援全文檢索（如 MySQL 的 FULLTEXT 索引或 Elasticsearch），可以對 content 欄位應用全文索引，方便快速搜尋。

3. 版本控制

許多法規和契約都會有不同版本，因此需要有一套版本控制機制：
	•	Document 表中的 version 欄位用於標記版本號。
	•	可考慮在 Document 表中加入 is_current_version 欄位，以標記當前最新版本。
	•	當文件更新時，新增一條新紀錄並將舊版本標記為非當前版本。

4. 查詢範例

針對法規或契約文件資料庫，以下是一些常見的查詢需求：
	•	查詢特定法規或契約的所有條款。
	•	查詢包含特定關鍵字的法規段落。
	•	根據條款號快速查找該條款的具體內容。
	•	查詢條款之間的交叉引用，追溯相關條款。

5. 實施細節與使用建議

	•	使用文件類型的資料庫（如 MongoDB）對於存儲高度結構化的段落可能更合適，而關係型資料庫則更適合處理複雜查詢。
	•	若需要支援全文檢索，推薦使用 Elasticsearch 等專門的搜索引擎，並與主資料庫整合。

這樣的設計既能儲存文件的層次結構，又方便查詢與檢索，適用於需要高效查詢和變更追蹤的文件管理需求。
