簡要說明
---
這個目錄包含 Git hooks（預先提交檢查），用來阻止將 `.obsidian/` 等應被忽略的檔案加入版本控制。請各協作者在 clone 後依照下列步驟安裝 hooks，以確保一致性。

安裝 hooks（推薦）
1. 在專案根目錄執行：

   git config core.hooksPath .githooks

   這樣 Git 會使用本 repository 下的 `.githooks` 作為 hooks 路徑（會自動啟用裡面的可執行檔）。

2. 在 Windows 上，如果使用 PowerShell 或 Git Bash，請確保 `.githooks/pre-commit` 可執行：

   # Git Bash
   chmod +x .githooks/pre-commit

   # PowerShell (必要時)
   # 無需特殊指令，但請確認檔案存在且 git config 指向正確路徑。

設定全域忽略（建議，每台機器執行一次）
---
為避免在任意 repo 重複碰到同樣問題，建議每位開發者把 `.obsidian/` 加到全域忽略：

```bash
echo ".obsidian/" >> $HOME/.gitignore_global
git config --global core.excludesfile $HOME/.gitignore_global
```

若同事是 Windows PowerShell：

```powershell
Add-Content -Path $HOME\\.gitignore_global -Value ".obsidian/"
git config --global core.excludesfile $HOME\\.gitignore_global
```

若遠端或歷史中曾經追蹤過 `.obsidian`（我們已在此 repo 停止追蹤），個人若仍被追蹤請執行：

```bash
git rm -r --cached .obsidian
git commit -m "Stop tracking .obsidian"
git push
```

其他說明
---
- 如果你偏好不改本地 `core.hooksPath`，也可以把 `.githooks/pre-commit` 複製到 `.git/hooks/pre-commit`（並確保可執行）。
- 若要從整個 repo 歷史徹底移除 `.obsidian`，請聯絡倉庫管理者，我們可以用 `git filter-repo` / BFG 做歷史重寫（需協調所有協作者）。

謝謝配合。
