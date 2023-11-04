---
layout: default
title:  leaderboad
parent: commands
grand_parent:  docs
last_modified_date: 2022-04-25 12:20:36
tags: fastchat
---
# leaderboad
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

### Get logs
```
gsutil -m rsync -r gs://fastchat_logs ~/fastchat_logs/
```

### Clean battle data
```
cd ~/FastChat/fastchat/serve/monitor
python3 clean_battle_data.py
```

### Run Elo analysis
```
python3 elo_analysis.py --clean-battle-file clean_battle_20230523.json
```
