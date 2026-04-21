---
layout: default
title: 標準技能描述（草案）
parent: SKILL相關筆記
grand_parent: 自然語言處理
nav_order: 2
date: 2026-04-21
last_modified_date: 2026-04-21T16:02:26
tags:
  - AI
  - SKILL
---

# 標準技能描述（草案）
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


目的：提供一個輕量且可擴充的 canonical schema，讓內部技能（skill）能被不同 agent（Copilot, Claude Code, Antigravity, Cursor 等）以 adapter 方式相容並安裝。核心要求：可驗證、可簽章、包含 capability 與權限、及 provenance metadata。

格式：YAML / JSON（下例同時給出 YAML 範本與欄位說明）

---
# skill manifest (YAML)

```yaml
id: "urn:skill:org:myteam:pr-summarizer:1.0.0"
name: "PR Summarizer"
description: "產生 Pull Request 摘要並標註關鍵變更、風險與測試狀態。"
version: "1.0.0"
author:
  id: "user:8649974426"
  name: "Kuang"
  email: "kuang@example.com"
license: "proprietary"
entrypoint:
  type: "http"
  url: "https://internal-service.local/skills/pr-summarizer/run"
inputs:
  - name: "repo"
    type: "string"
    required: true
  - name: "pr_number"
    type: "integer"
    required: true
outputs:
  - name: "summary"
    type: "string"
capabilities:
  - network: true
  - filesystem: false
  - git: true
permissions:
  - allow_read: ["repo_code"]
  - allow_write: ["issues"]
provenance:
  created_at: "2026-04-12T08:00:00Z"
  created_by: "user:8649974426"
  source_repo: "org/skills-repo"
  source_path: "skills/pr-summarizer/manifest.yaml"
signature:
  type: "ed25519"
  signer: "skill-registry"
  value: "BASE64_SIG"
visibility: "team" # private|team|org|public
dependencies:
  - name: "python"
    version: ">=3.10"
  - name: "requests"
    version: ">=2.28"
policy:
  review_required: true
  reviewers: ["team-lead","sec-team"]
metadata:
  tags: ["pr","summarize","developer-productivity"]
  estimated_risks: ["exposes_file_paths"]
```

---

欄位說明（要點）
- id: 全域唯一識別（建議使用 URN 格式，含 org 與版本）。
- name / description / version / author / license: 基本辨識欄位。
- entrypoint: 技能的執行端點，可為 http、cli、local-plugin 等類型。
- inputs/outputs: 宣告接口，方便 agent 型別檢查與 UI 生成。
- capabilities & permissions: 宣告所需權限（network/filesystem/git），供審核與 sandboxing 使用。
- provenance: 原始來源（repo、path、作者、時間），是治理與追溯的核心。
- signature: skill 被註冊/核准後的簽章，用於驗證技能的完整性與來源。
- visibility: 控制可見範圍（local/team/org/public）。
- dependencies: 執行所需的外部套件與版本（供審核掃描）。
- policy: 審核規則（是否需要 review、required reviewers），支援自動化審核流程。
- metadata: 可搜尋的 tag、估計風險、兼容 agent 列表等。

運用建議（快速）」
- 建立一個 signed skill registry：當技能通過自動掃描（依賴、PII、安全）與人工審核後，registry 對 manifest 做 ed25519 簽章並允許 agent 安裝簽章過的 skill。
- adapter pattern：對於每個 target agent（Copilot/Claude/Antigravity），實作一個 adapter 將 canonical manifest 轉為 agent 的 plugin/manifest 格式。
- 最小可行 manifest：在 POC 先只要求 id/name/version/entrypoint/inputs/permissions/provenance/signature/visibility，其他欄位可後續擴展。

