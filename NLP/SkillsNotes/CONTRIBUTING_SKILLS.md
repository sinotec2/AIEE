CONTRIBUTING — Skill 開發與提交指南（針對貢獻者）

目標：讓開發者以最低摩擦提交 Skill（Agent/Plugin），同時確保安全、可追溯與可跨平台部署。

一、檔案與目錄規範
- 在 skills-repo 下建立： /skills/<skill-name>/
- 必要檔案：
  - skill 程式碼（執行檔、scripts 或 package）
  - README.md（usage、examples）
  - manifest.yaml（canonical manifest，見範本）
  - tests/ 或 sample_runs/（至少一個範例執行紀錄）

二、manifest 最低欄位（PR 必須包含）
- id (urn:skill:org:team:name:semver)
- name, description, version, author
- entrypoint (http|cli|plugin path)
- inputs, outputs（至少主要 input/output）
- permissions (network/filesystem/git 列出會存取的資源)
- provenance (source_repo, source_path, commit)
- visibility (private|team|org|public)
- policy.review_required (true|false)

三、PR Checklist（請在 PR 描述中勾選）
- [ ] manifest.yaml 已放置且欄位完整
- [ ] README.md 含 usage 與至少一個 example
- [ ] 已提供 sample_runs 或測試結果（附 log）
- [ ] security checklist：是否存取敏感資料/外部 API/寫檔（簡述）
- [ ] license 與第三方依賴列出（若有）
- [ ] 指定 reviewer（team lead / sec team if required）

四、CI 會自動檢查（貢獻者無需手動）
- manifest schema validator
- dependency & license scan (SCA)
- PII / token pattern scan
- unit/integration tests 或 sample_runs 驗證
- 若 manifest 標示需要 network/filesystem 權限，會觸發額外審核

五、審核與簽章政策（要點）
- 自動通過（快速簽章）：visibility=private/team，無 network/write 權限，CI 全過
- 需要人工審核：需 network/write、visibility=org/public、或 CI 偵測高風險
- 審核通過後 registry 會簽章 manifest，並產生 promote audit 記錄（who/when/commit）

六、發佈與安裝（使用者角度）
- 安裝指令：skillctl install <urn:skill:...>（或透過 agent UI 安裝）
- 若發現問題：回報到原 skill repo，並在 registry 建 revoke request

七、撤回與修正
- revoke：registry 寫入 revoke 紀錄（append-only），阻止安裝
- 修正：提交新 PR 更新版本，通過審核後 supersede 舊版本

八、快速 PR 範例（PR description 範本）
Title: [skill] <name> v<semver> — short description
Changes: list files added/changed
Manifest: path/to/manifest.yaml (confirm fields: id, entrypoint, permissions, visibility)
Test: how to reproduce sample run (commands + expected output)
Security: note any network/filesystem/git access or PII exposure
Reviewers: @team-lead @sec-team (if required)

簡短提示：您的工作就是把 skill 程式碼 + manifest + README + 範例放到 /skills/<name>/、開 PR、勾選 checklist。CI / registry / adapter 將自動處理驗證與發佈步驟。