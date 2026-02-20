---
layout: default
title: 會議紀錄 ETL 指南
parent: 會議記錄小幫手
grand_parent: 自然語言處理
nav_order: 99
date: 2026-02-20
last_modified_date: 2026-02-20 23:11:00
has_children: false
tags:
  - AI
  - meetings
---

# 會議紀錄 ETL 指南
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

> 目標：將「會議紀錄原文」轉成乾淨的 `{委員姓名, affiliation, 意見}` 結構，並妥善處理重複姓名與引用發言。

## 1. 全體流程概覽

1. **資料前處理**：解碼、去除頁首/頁尾、標準化編碼（UTF-8）與換行。
2. **段落切分**：沿用原始段落，並視需要加入「發言 cue」規則切得更細。
3. **發言者偵測**：使用規則 + 斷詞（結巴＋自訂詞庫）找出主發言者。
4. **引用偵測**：同段落中若出現「引用別人意見」的語句，額外產生 `quoted_from` 事件。
5. **姓名消歧**：將偵測到的姓名對應到官方名錄（含別名、頭銜、affiliation）。
6. **結構化輸出**：輸出 JSON / CSV，欄位包含 `speaker`, `affiliation`, `content`, `type`（direct/quoted）、`source_meta` 等。
7. **品質檢查**：統計未匹配的人名、重複姓名、空內容，提供人工覆核。

## 2. 段落切分

### 2.1 基礎策略
- 先依原始檔案的空行或 bullet 進行切分。
- 移除頁碼、章節號碼等噪音，保留段落內行內換行。

### 2.2 精細切分規則
- **Cue-based split**：遇到 `○○委員：`、`○○委員表示`、`主席○○說` 等 pattern 就視為新段落。
- **主持人/部會官員**：加入頭銜詞典（主席、召集人、部長等），避免被誤判為委員。
- - **多發言段**：若段內出現多個 `○○委員`，可再切成子段，或延後到「引用偵測」處理。

## 3. 發言者偵測

### 3.1 結巴自訂詞庫
- 建立 `userdict.txt`：內容為 `姓名 詞頻 TAG`，詞頻可設 100000 以確保優先斷詞。
- 常見頭銜、機構（例如「經濟部」）也可加入對應詞性，防止被視為人名。

### 3.2 規則樣式
| 類型 | Regex / 範例 | 備註 |
|------|--------------|------|
| 冒號格式 | `(?P<name>[^\s：]{2,6})(委員|主席|召集人)?：` | 最常見，冒號前為發言者 |
| 動詞格式 | `(?P<name>[^\s\d，。、]{2,6})(委員)?(表示|說明|發言|提到)` | 需排除句中引用 |
| 轉述格式 | `(?P<speaker>[^\s：]{2,6})(委員)?指出(?P<quoted>[^：]{2,10})(委員)` | 可同時抓主語與引用 |

- 辨識到 `name` 後，標記段落的 `speaker`，同時記錄觸發規則以供調試。
- 若段落沒有標準 cue，保留為 `unknown` 待後續人工或模型補標。

## 4. 引用偵測（Quoted Opinions）

即使主段是某委員，也可能引用他人意見；建議在段落文字上做第二輪 pattern matching：

- `「(?P<quoted_text>.*?)」, (?P<ref>[^\s]{2,6})(委員|部長)`
- `…轉述(?P<quoted>[^\s]{2,6})委員之意見…`

產生資料列：
```json
{
  "type": "quoted",
  "speaker": "王小明",     // 正在發言的人
  "quoted_from": "李大華",
  "content": "引述的內容",
  "source_paragraph": 45
}
```

## 5. 姓名消歧 / 實體鏈結

1. **名錄建立**：整理 `{canonical_name, variants, affiliation, 職稱}`。
2. **匹配策略**：
   - 完整匹配：`name` or `name + 委員`。
   - 變體匹配：對照 `variants`（別名、舊姓、英文名）。
   - 限制候選：僅在該次會議參與名單中搜尋，降低重名干擾。
3. **語意匹配（可選）**：
   - 若 `rule-based` 匹配多於一人，可將段落文字向量化（如 `uer/sbert-base-chinese-nli`），與候選人「個人資料描述」比較，選擇相似度最高者。
4. **結果紀錄**：
   - 存 `speaker_id`（唯一），並於 output 裡保留 `matched_by`（exact/variant/embedding）。

## 6. 結構化輸出

建議欄位：

| 欄位 | 說明 |
|------|------|
| `paragraph_id` | 原始段落編號或 hash |
| `type` | `direct` / `quoted` |
| `speaker_id` | 內部唯一 ID（對應名錄） |
| `speaker_name` | 匹配後名稱 |
| `affiliation` | 從名錄帶出 |
| `quoted_from` | 若 type=quoted，標示來源人 |
| `content` | 段落文字或引用文字 |
| `source_meta` | 會議名稱、日期、頁碼等 |

輸出格式可用 JSON Lines、CSV、Parquet，視後續分析管道而定。

## 7. 品質檢查與回饋

- **統計指標**：
  - 未匹配姓名數、`unknown` 段落比率；
  - 每位委員的發言次數（檢查是否不合理）。
- **錯誤樣本收集**：將 `unknown` 或 `multi-match` 的段落匯出，人工補標後再更新詞庫/規則。
- **LLM 輔助**：對於難以規則化的段落，可在已有 metadata 的情況下呼叫 LLM 進行整理，結果再回寫名錄。

## 8. 參考資源（可搜尋關鍵字）

- GitHub：`meeting minutes nlp`, `議事錄 斷詞`, `會議紀錄 實體抽取`。
- 學術/部門報告：立法院、地方議會的 NLP 專題，常分享發言者抽取方法。
- 中文實體鏈結：搜尋 `Chinese name disambiguation`, `中文 姓名 實體鏈結`。

---

> Tips：維持「規則 + 名錄 + 語意匹配」的分層架構，遇到資料特例時可以針對某一層調整，而不用整個 pipeline 重寫。需要樣本程式碼時，再把原始段落貼給我，我可以補上實作範例。