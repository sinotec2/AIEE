---
layout: default
title: " Skill 提交範本"
parent: SKILL相關筆記
grand_parent: 自然語言處理
nav_order: 5
date: 2026-04-21
last_modified_date: 2026-04-21T16:02:26
tags:
  - AI
  - SKILL
---

#  PR TEMPLATE — Skill 提交範本

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


```markdown
Title: [skill] <name> v<semver> — short description

## Changes
- Files added/changed:
  - /skills/<skill-name>/manifest.yaml
  - /skills/<skill-name>/README.md
  - /skills/<skill-name>/...

## Manifest
Path: /skills/<skill-name>/manifest.yaml
Confirm fields present: id, entrypoint, permissions, visibility

## Test (How to reproduce)
- Commands:
  - ...
- Expected output:
  - ...
- Attached logs: /skills/<skill-name>/sample_runs/log.txt

## Security checklist
- [ ] No PII or secrets included
- [ ] Network access required: yes/no (if yes, explain)
- [ ] Filesystem write required: yes/no (if yes, explain)
- [ ] External APIs called: yes/no (if yes, list)

## License & Dependencies
- License: <license>
- Dependencies: list third party libs and licenses

## Reviewers
- @team-lead
- @sec-team (if required)

## Notes
- Any other notes for reviewers
```