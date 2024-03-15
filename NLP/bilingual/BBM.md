---
layout: default
title: BBM notes
parent: Bilingual AI Processing
grand_parent: 自然語言處理
nav_order: 99
date: 2024-03-16
last_modified_date: 2024-03-16 05:28:34
tags: AI chat
---


# BBM notes
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

- Bilingual Book Maker (BBM)應該是個普通名詞的、但它已經成為github的熱門下載，yihong0618及其52位貢獻者們獲得了近7k的好評，詳見其[官網](https://github.com/yihong0618/bilingual_book_maker)。
- 其他方案
  - browser plugin的版本： Rocky@電腦阿達王(2023)[教你使用「沉浸式翻譯」來翻譯整本外語電子書，支援 OpenAI API、Google 等數十種翻譯服務](https://www.kocpc.com.tw/archives/489405)
- 基本上BBM提供的是命令列的作業方式，除了安裝之外、設定之外，如果需要批次作業、壓縮結果，還是需要命令列其他指令的協助。

## 安裝

```bash
git clone https://github.com/yihong0618/bilingual_book_maker.git
cd bilingual_book_maker
pip install -r requirements.txt
```

## 設定

- 團隊接納許多API的來源，設定方式也較為複雜。此處以openai為例，有2種設法
  - `export openai_key=sk-...`，並在命令列中輸入`--openai_key ${openai_key}`
  - `export BBM_OPENAI_API_KEY=sk-...`，命令列中就不需要`--openai_key`選項
- 目標語言（`--language`）
  - 引數可以是縮寫(`en`、`tw-hans`、`ja`等等)、或是全名(`"Simplified Chinese"`、`"English"`等等)
  - 內設是簡體中文，如果沒有設定，會將輸入文字翻譯成`zh-hans`

## 執行

### 單次執行

- 輸入檔
  - 參數`--book_name`
  - 可以是`epub`檔（xml格式），也可以是`txt`檔，
  - 檔案長短不拘，程式會自動按照ai的消化能力判斷每次處理的文章段落。
- 輸出檔
  - 螢幕輸出
  - 內設輸出檔名`*_bilingual.txt`。`*`為輸入之主檔名。

### 批次執行

- 將螢幕輸出導至某個輸出檔，以求簡潔。

```bash
for i in {2..6};do 
  python3 make_book.py --book_name eia/C0$i.txt --openai_key ${openai_key} --language English > eia/E0$i.txt
done
```

## 結果

- 本次翻譯環評報告共5章內容，共使用了gpt-3.5-turbo等7個語言模型花了0.1USD。
- 翻譯品質的話，因為本人較少看英文的環評報告，看是看得懂，但就是覺得生硬，可能是本身的問題。
- 套件似乎還可以要求修改特定的文章語調，如對結果仍不滿意，還可以進行微調。
- GPT-4 翻譯品質比較好，但價格較貴且速度慢一些。
