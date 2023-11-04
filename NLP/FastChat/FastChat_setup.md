---
layout: default
title: FastChat的裝置與應用
parent: fastchat
nav_order: 99
date: 2023-09-05
last_modified_date: 2023-09-05 13:44:37
tags: AI chat
---


# FastChat的裝置與應用
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

- [chatWeb][3]安裝在[node03:7860](http://200.200.31.47:7860/)之後，對模型的核心計算使用別人的機器，總覺得有點過意不去，希望能用自己的機器來執行全套系統看看，畢竟還是要了解整個布建需要哪些軟/硬體。就去發現了[lmsys][1]在2023/4月公開的這套[FastChat][2]。
- 除了[官網][2]之外，另有不多的中文介紹，如《知乎》網友[薛定谔的皮丘(2023/08)][9][^2]以及[Hok(2023/04)][10][^3]，想讀中文介紹的讀者也可以去訪問他們的筆記。
- 這裡除了留存一些技術心得以外，併同前面[chatWeb][3]的經驗想法，也對未來語言模型在局地的應用架構有些總結。
- 落地實例可以點選[這裡][8](公司內網)。

### lmsys簡介

- [lmsys][1]這個由美國學術界組成的開放研究組織，除了來自於頂尖的3所大學(UC Berkeley, UCSD and CMU)的研究師生之外，主要的功能在建構一個大型語言模型的競賽擂台[ChatBot Arena][4]，讓有興趣挑戰的同儕，可以在此鍛鍊進步。
- 該擂台所使用的模型都是目前私人公司與開放領域發展最新的語言模型，模型推理計算使用該機構的GPU，擂台的界面程式則是此處要引進的這套[FastChat][2]。
- [ChatBot Arena][4]的排行榜公開在[HuggingFace][5]的平台空間[lmsys/chatbot-arena-leaderboard][6]。
- 最新一版比試結果公開在[arXiv(2023/06)][7][^1]，第1名為GPT4，前5名全為私人單位發展知產品。

### FastChat簡介

[FastChat][2]界面獲得2萬7千多個github好評。依據其原版修訂應用版本有3千多個。由145個作者共同貢獻。核心功能包括多模型服務系統、API、評估工具等，其特色有下列幾點(by [chatWeb][3])

- 多模型服務系統的特色包括：
  - 支援多種模型：該系統支援多種模型，包括LLama 2、Vicuna、Alpaca、Baize、ChatGLM、Dolly、Falcon、FastChat-T5、GPT4ALL、Guanaco、MTP、OpenAssistant、RedPajama、StableLM、WizardLM等等。
  - 分散式服務：該系統是一個分散式的多模型服務系統，可以同時運行多個模型。
  - 支援多種平台：該系統支援多種平台，包括CPU、GPU、Intel XPU、Metal Backend等，並提供了相應的指令和配置方式。
  - 高效性能：該系統通過優化和分佈式架構，提供了高效的模型服務性能，能夠處理大量的用戶請求。
  - 易於使用：該系統提供了詳細的安裝和使用文檔，用戶可以根據文檔進行快速部署和配置。
- API：該系統提供了網頁界面和OpenAI兼容的RESTful API，方便用戶進行模型服務和交換。可以像openAI一樣，經提供token後，使用雲端服務業者所提供的推理計算資源。
- "評估工具"的特色如下：
  - 使用MT-bench進行評估：評估工具使用MT-bench，一組具有挑戰性的多輪開放式問題，來評估模型的品質。
  - 自動化評估流程：評估工具使用強大的LLM（如GPT-4）作為評判，自動評估模型的回答品質。
  - 提供指導：評估工具提供了運行MT-bench的指示，以及使用fastchat/llm_judge進行評估的指示。

### FastChat架構

- 以下說明為[chatWeb][3]執行結果
- `fastchat.serve.controller`
  - "`fastchat.serve.controller`"是FastChat中的一個模組，它的功能是管理分散式的模型工作器(`model worker`)。
  - 模型工作器是負責托管一個或多個模型的服務器，而控制器則負責協調這些模型工作器和與用戶交互的Web服務器之間的通信。控制器管理模型工作器的註冊、分配請求給適當的模型工作器以進行處理，並將結果返回給用戶UI。
  - 簡而言之，"`fastchat.serve.controller`"的功能是管理和協調FastChat中的模型工作器，以實現分散式的多模型服務。
- `fastchat.serve.model_worker`
  - 用於大型語言模型的聊天機器人訓練、提供服務和評估。為最耗費計算資源的部分。
  - 它是FastChat的核心組件之一，負責承擔模型的運算和處理輸入輸出。
  - 可以使用任何形式的計算資源，包括遠端或局地CPU、GPU、Intel XPU、Metal Backend等等。
  - 模型工作器（`model_worker`）通常與FastChat的控制器（`controller`）一起使用。
- `fastchat.serve.gradio_web_server`(`server_multi`)
  - 啟動一個單單/多標籤的Gradio伺服器，其中包括Chatbot Arena的標籤。
  - web_server單模式版本：與一般chatbot並沒有太大的差異。可調整temperature及topP等2個參數值。
  - 多模式版本(`server_multi`)：這個功能可以讓你在網頁上同時展示多個模型，並與這些模型進行對話。

## ip and portal arrangements

### 3個埠的關係

[FastChat][2]會需要3個埠(不能重複。如不給定，三支程式內設都會是21001，只能用一次)

1. 控制埠( \$addc=http://${ip}:21001內設)，搭配controller-address(作業埠需要)/controller-url(UI埠需要)之引數
2. 作業埠( \$add=http://${ip}:$port)。引數worker-address只需設定一次。
3. UI埠( \$addu=http://${ip}:$port1)，為使用者最後看到的界面。

安裝與其餘設定詳見[jondurbin/FastChat](https://github.com/jondurbin/FastChat)。此處詳解devp(ip=200.200.32.195)上的啟動方式。([結果位址][8])

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-09-05-15-51-50.png)

### 控制埠的啟動

- 控制埠為其他2埠作業的核心，因此其ip必須讓所有的埠都能順利取用。
- 如不指定host，則會是內設值localhost。如果為localhost，則其他2埠也必須設在localhost，因其他機器都無法存取控制埠。
- 控制埠與UI埠的關係較為單純，為簡單的一對一。
- 控制埠與模型作業埠的關係是一對多，因此需要每個作業埠都能呼叫得到的IP。
- 啟動transformer與其他模組(env name=YOLOv8)

```bash
conda activate /nas2/kuang/.conda/envs/YOLOv8
python3 -m fastchat.serve.controller --host $ip &
```

### 模型作業埠

- model-path可以指定到特定的模型。不一定是lmsys。優秀的公開模型如[lmsys/vicuna-33b-v1.3](https://huggingface.co/lmsys/vicuna-33b-v1.3)、[mosaicml/mpt-30b-chat](https://huggingface.co/mosaicml/mpt-30b-chat)及[WizardLM/WizardLM-13B-V1.1](https://huggingface.co/WizardLM/WizardLM-13B-V1.1)。或者是中國公開可商用的百川([baichuan-7b](https://blog.csdn.net/jclian91/article/details/131650918)，不過要小心國家認同議題的回覆內容。)
- 上接控制埠。所有的輸入及輸出都會通過控制埠到(從)UI埠。
- 同一個控制埠及UI埠可以(同時)接受多個模型作業埠的呼叫，只要將作業開在不同的埠就好了。
- 必須指定該機器可以提供的device，否則內設為gpu。
- 模型作業埠的位址似乎沒有特別的作用。提供給測試用而已(詳下)。

```bash
port=55083
add="http://${ip}:$port"
mdl="lmsys/vicuna-7b-v1.5-16k"
python3 -m fastchat.serve.model_worker --model-path $mdl \
--host $ip \
--worker-address $add \
--controller-address $addc --port $port --device cpu &
```

### 測試模型是否正常運作

- 啟動命令列模式之chatbot
- 需指定作業埠專屬的位址。
- 啟動做為測試的模型名稱也必須與作業模型一致。
- 此處不需(不可)再指定`device`、沒有模式路徑(`model-path`)

```bash
python3 -m fastchat.serve.test_message --model-name vicuna-7b-v1.5-16k --worker-address $add
```

### webui程式埠

- 需要設定2組位址，一個是控制埠(`controller-url`)，一個是使用者會連上的最後位址。

```bash
python3 -m fastchat.serve.gradio_web_server --host $ip --port $port1 --controller-url $addc
```

- 如果模型的名稱不在[FastChat][2]套件資料庫內，畫面會出現`Add the description at fastchat/model/model_registry.py	`
- 直接修改該程式新增模型的相關敘述即可
- 依序是簡稱、全名、來源、說明
- 輸入後，程式會自己調用相關說明顯示在畫面上。

```python
#/nas2/kuang/.conda/envs/YOLOv8/lib/python3.9/site-packages/fastchat/model/model_registry.py
...
register_model_info(
    ["gpt-4"], "ChatGPT-4", "https://openai.com/research/gpt-4", "ChatGPT-4 by OpenAI"
)
```

### up_fastchat.cs

```bash
#activate transformer and other modules
/home/anaconda3/condabin/conda activate /nas2/kuang/.conda/envs/YOLOv8

#LAN IP address
ip=200.200.32.195

# control portal
addc="http://${ip}:21001"

# up the controller in background
python3 -m fastchat.serve.controller --host $ip &

# define the model paths and designated portals
mdls=( "lmsys/vicuna-7b-v1.5-16k" "jondurbin/airoboros-13b-gpt4-1.4")
port=( 55080 55081)

#up the model kernerls
for i in 0 1;do
  add="http://${ip}:${port[$i]}"
  python3 -m fastchat.serve.model_worker --model-path ${mdls[$i]} --host $ip --worker-address $add --controller-address $addc --port $port --device cpu &;done

# the webUI python
port=55083
python3 -m fastchat.serve.gradio_web_server_multi --host $ip --port $port --controller-url $addc &
```

## 設定成果

### 落地實例

- 可以點選[這裡][8](公司內網)。

### 單模型界面使用說明

- 單模型界面也包括在雙模型界面之內，因此並不需要另外執行`fastchat.serve.gradio_web_server`
- 除了說明欄之外，此處需要選取一個模型來交談。可以直接點選或由右邊的下來選單來選擇。UI會列出控制埠納進的所有模型名稱。

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-09-05-16-23-23.png)
![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-09-05-16-25-48.png)

- 文字輸入欄：輸入文字按下enter或者是Send鍵，出現在對話框中即為接受輸入。
- 其次，UI提供了投票選項，對個別使用並不會回傳結果。按下"Clear History"會清除對話框內容。
- 由於系統並沒有使用者資料庫，因此對話並不會記錄下來。
- 之外，[FastChat][2]還提供了2個模型參數(Parameters)讓使用者可以下拉選擇，左右調整，讓模型推理結果更符合使用者的需求。

### 雙模型界面使用說明

- chatbot擂台有2個頁面
  - battle頁面會隨機選取2個模型來回答問題，讓使用者盲目評分，看哪一個模型答得好。算是盲樣測試。
  - 右側的side by side則是由使用者自行指定2個已知名稱的模型進行比對。

|![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-09-06-09-02-35.png)|
|:-:|
|<br>雙(多)模型頁面選擇</br>|

### idle and refresh

- 如果界面閒置太久，會出現`THIS SESSION HAS BEEN INACTIVE FOR TOO LONG. PLEASE REFRESH THIS PAGE.`訊息，並且拒絕運作
- 只需重新整理頁面即可啟動

### CPU 運作情形

單一模型運作約會消耗工作站一半的計算容量。約45~47個核心。

![](https://github.com/sinotec2/FAQ/raw/main/attachments/2023-09-06-09-29-23.png)

### tmux

使用[tmux](https://sinotec2.github.io/Focus-on-Air-Quality/utilities/OperationSystem/tmux)指令，讓程式在背景運作。避免終端機關閉、網路斷線後程式隨即停止。

### 模型參數

[FastChat][2]提供了2個模型參數讓使用者可以調整答案的語文內容。以下是chatGPT對這2類參數的解釋。

- temperature (chatGPT)
  - 在大型語言模型中，"temperature" 是一個控制生成文本多樣性的參數。這個參數通常用於生成隨機性的文本輸出。較高的溫度值會產生更多的隨機性，而較低的溫度值會產生較少的隨機性。
  - 具體來說，當使用較高的溫度值時，模型生成的文本更具變化性，可能包含更多不同的詞彙和結構變化，這使得生成的文本看起來更加多樣化。然而，這種多樣性可能會導致生成的文本變得不那麼連貫和隨意。
- top (chatGPT)
  - 在大型語言模型中，"top" 參數通常用於控制生成文本時的詞彙選擇。這個參數決定了在生成文本時模型將考慮多少個最有可能的詞彙選擇。有top-k及top-P 2種參數。([FastChat][2]提供的是top-P參數。)
    - 具體來說，"top-k" 是一種選擇性截斷策略，用於生成文本中的詞彙。當使用 "top-k" 時，模型會在詞彙表中選擇概率排名前 k 高的詞彙，然後從這 k 個詞彙中選擇下一個詞彙。這樣可以確保生成的文本中的詞彙是模型認為最有可能的詞彙，有助於提高文本的一致性和可讀性。
    - 相反，"top-p"（也稱為 nucleus sampling）是一種根據詞彙概率質量分佈的截斷策略。當使用 "top-p" 時，模型會在詞彙表中根據詞彙的累積概率質量（由高到低排序）來選擇詞彙，直到累積概率質量達到或超過一個給定的閾值（通常是一個很小的數值）。這樣可以確保生成的文本中的詞彙是概率質量較高的詞彙，但同時保持了一定的隨機性，因為累積概率質量可能會包含多個詞彙
  - 這兩種截斷策略可以幫助控制生成文本時的多樣性和可控性。較大的 "top-k" 或 "top-p" 值會導致生成的文本更多樣，而較小的值會導致生成的文本更加一致。

## Rethiking

- CPU執行語言模型的推演實在不是一個好的方案，對計算型的工作站而言太吃力了。還是要思考其他的方案，如雲端的GPU計算服務。這一點[FastChat][2]宣稱是有這個類似openAI API功能選項的，還需要花時間來落實。
- [FastChat][2]沒有好的歷史資料庫來保存使用者過去的對話。這個問題還蠻困擾的。每次都需要有充分的提示，chatbot才會正確回應。相關程式及資料庫、是否會員系統等，部件都還有待尋找。
- [chatWeb][3]的核心語言模型是GPT3.5，有點老舊，應可以更換成公開版的GPT4。這2個套件應該有點整併，並且將計算放在指定雲端而不是openAI，畢竟openAI販賣的不是雲端計算。
- 怎麼降低temperature設定，讓語言模型可以更貼近實際檔案知識，這點除了用[chatWeb][3]之外，還需要有具有監督性質的規範，讓語言模型可以輕鬆切換進入環工的多樣性領域。
- 這裡似乎還有很多的[prompting engineer][11]工作，諸如：你是一個環評專家...、土水專家、空品模式專家等等。

[1]: https://lmsys.org/about/ "Large Model Systems Organization (LMSYS Org)開放研究組織。該組織由UC Berkeley的學生和教職員與UCSD和CMU合作創立。他們的目標是通過共同開發開放模型、數據集、系統和評估工具，使大型模型對每個人都可用。他們的工作涉及機器學習和系統的研究。他們訓練大型語言模型並使其廣泛可用，同時開發分佈式系統來加速模型的訓練和推理。該組織的成員包括UC Berkeley、UCSD、CMU和MBZUAI等機構的學生和教職員。"
[2]: https://github.com/lm-sys/FastChat "FastChat 是一個開放平台，用於訓練、服務和評估基於大型語言模型的聊天機器人。 核心功能包括：最先進模型（例如 Vicuna）的權重、訓練代碼和評估代碼，以及具有 Web UI 和 OpenAI 兼容 RESTful API 的分佈式多模型服務系統。"
[3]: https://github.com/SkywalkerDarren/chatWeb "SkywalkerDarren(2022) ChatWeb 可以抓取任何網頁或從 PDF、DOCX、TXT 文件中提取文本，並生成嵌入式摘要。 它還可以根據文本內容回答您的問題。 它是使用基於gpt3.5的chatAPI和embeddingAPI以及向量數據庫來實現的。"
[4]: https://chat.lmsys.org/?arena "⚔️Chatbot Arena ⚔️ : Benchmarking LLMs in the Wild"
[5]: https://zh.wikipedia.org/zh-tw/Hugging_Face "Hugging Face是一家美國公司，專門開發用於構建機器學習應用的工具。該公司的代表產品是其為自然語言處理應用構建的transformers庫，以及允許使用者共享機器學習模型和資料集的平台"
[6]: https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard "Leaderboard/該排行榜基於以下三個基準。(1)Chatbot Arena - 眾包、隨機的戰鬥平台。 我們使用 50K+ 用戶投票來計算 Elo 評級。(2)MT-Bench - 一組具有挑戰性的多回合問題。 我們使用 GPT-4 對模型響應進行評分。(3)MMLU (5-shot) - 衡量模型在 57 項任務上的多任務準確性的測試。" 
[7]: https://doi.org/10.48550/arXiv.2306.05685 "Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E.P., Zhang, H., Gonzalez, J.E., Stoica, I. (2023). **Judging LLM-as-a-judge with MT-Bench and Chatbot Arena**."
[8]: http://200.200.32.195:55081 "⚔️ Chatbot Arena ⚔️ : Benchmarking LLMs in the Wild on the DEVP workstation"
[9]: https://zhuanlan.zhihu.com/p/620801429 "薛定谔的皮丘(2023/08/10)小羊驼模型(FastChat-vicuna)运行踩坑记录@知乎"
[10]: https://zhuanlan.zhihu.com/p/622292418 "Hok(发布于 2023-04-16)FastChat使用感受@知乎"
[11]: https://chat.openai.com/share/029f3f0f-7f68-436d-8145-66a75ef63d0f "在AI領域，prompting engineer 是一個角色或職位，其主要職責是設計、構建和優化用於訓練和操作大型語言模型（如GPT-3、BERT等）的提示（prompts）或輸入文本。"

[^1]: Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E.P., Zhang, H., Gonzalez, J.E., Stoica, I. (2023). **Judging LLM-as-a-judge with MT-Bench and Chatbot Arena**. [doi](https://doi.org/10.48550/arXiv.2306.05685)
[^2]: https://zhuanlan.zhihu.com/p/620801429 薛定谔的皮丘(2023/08/10)小羊驼模型(FastChat-vicuna)运行踩坑记录@[知乎][9]
[^3]: https://zhuanlan.zhihu.com/p/622292418 Hok(发布于 2023-04-16)FastChat使用感受@[知乎][10]