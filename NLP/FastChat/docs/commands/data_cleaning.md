---
layout: default
title:  Data cleaning
parent: commands
grand_parent:  docs
last_modified_date: 2022-04-25 12:20:36
tags: fastchat
---
# Data cleaning
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

## Requirements

```
pip3 install bs4 markdownify
pip3 install polyglot pyicu pycld2
```

## Steps
```
# Convert html to markdown
python3 -m fastchat.data.clean_sharegpt --in sharegpt_html.json --out sharegpt_clean.json

# Keep or remove specific languages
python3 -m fastchat.data.optional_clean --in sharegpt_clean.json --out sharegpt_clean_lang.json --skip-lang SOME_LANGUAGE_CODE

# Split long conversations
python3 -m fastchat.data.split_long_conversation --in sharegpt_clean_lang.json --out sharegpt_clean_lang_split.json --model-name /home/ubuntu/model_weights/llama-7b/
```
