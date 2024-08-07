---
layout: default
title: fact checkers
parent: LLM 之微調
grand_parent: 自然語言處理
nav_order: 99
date: 2024-04-08
last_modified_date: 2024-04-20 21:59:59
tags: AI chat
---


# fact checkers
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

### source

- Factuality Challenges in the Era of Large Language Models.[(Augenstein et al., 2023)][(Augenstein et al., 2023)] [^1]

### 前言

- 我們需要一個全面的策略來解決LLM中與現實相關的挑戰，因為看來不存在單一解決方案可以完全減輕不利的後果。 
- 本文概述了各種策略的向度，這些向度結合起來可能會帶來更負責任和建設性的技術利用。 
- 有些解決方案是技術性的，需要建立一個全新的LLM。
- 雖然從頭開始訓練一個數十億參數的 LLM 需要幾個月的時間和數百個 GPU，這超出了大多數學者的能力範圍。 然而，較小的模型，例如 LLaMA、Falcon 或 Jais，在學術界是可行的。 例如，執行 7B 模型需要單一 GPU，而 13B 模型則需要兩個 GPU。 

## 面對威脅的策略方案

### 一致性和安全性

- 安全性、乃至調整LLM與人類價值和意圖一致的努力， 是ChatGPT、LLaMA 2 和 Jais 等最新模型的主要關注點。 
- 事實上，聊天機器人開發的各個階段都越來越多地考慮這些安全措施，包括
  - 訓練基本模型之前的資料清理、安全指令調整[^74]、
  - 聊天機器人隱藏提示的安全性，以及
  - 透過關鍵字和機器學習部署的聊天機器人的安全性。
- 開源LLM的可用性表明，協調工作以及其他對策（例如大型人工智慧公司的標竿管理）的有效性，可能會嚴重限制減輕潛在迫在眉睫的威脅。 儘管如此，盡一切努力抑制LLM的負面效應仍然至關重要。 

### 模組化知識基礎架構

- 當前LLM嚴重缺乏及時、全面和組織良好地展示事實密集的信息，例如態勢報告和戰略報告。
-  在預先訓練的LLM背景下，改善這一缺點的一種方法是採用**多步驟自動化框架來**(multi-step automated framework)收集和組織即時事件資訊。
-  這種模組化設計可以創造事實上準確的內容，可以使用LLM進一步完善內容，如 SmartBook[^75] 所示。 SmartBook 最初是為了在俄羅斯-烏克蘭衝突期間進行高效的地面報告而開發的，它使用LLM透過
   -  簡化基於事件的時間表、
   -  結構化摘要和
   -  綜合參考來產生初步態勢報告。 

### 檢索增強產生

檢索增強產生 (RAG)[^76],[^77] 將外部來源的上下文資訊合併到文字產生中。 RAG 透過增強LLM利用外部數據的能力，緩解了LLM產生不準確內容的挑戰。 然而，它需要大規模有效檢索接地文字和穩健的評估。 

### 幻覺控制與知識編輯

- LLM幻覺有兩種[^78]：(i) 忠實性，即生成的文本不忠於輸入脈絡； (ii) 事實性，當生成的文本在世界知識方面實際上不正確時。 最近的嘗試著重於基於LLM的自我一致性檢查79、跨模型驗證80,81或對照相關知識82來解決推理階段的幻覺問題。 假設LLM了解給定的概念，並且抽樣的回答可能相似並包含一致的事實。 另一個有前景的研究方向是為知識編輯開設LLM。 然後可以透過將事實更新註入模型83-87來定位和修復事實錯誤。 現有方法著重於透過精確編輯對三元組進行事實更新。 這可以擴展到更複雜的知識表示，例如未來的邏輯規則。 另一個挑戰是評估語言模型中知識編輯的「連鎖反應」。 目前的知識編輯基準檢查原始事實的一些釋義是否已更新，以及一些不相關的事實是否未受影響。 更多的研究必須探討從編輯中邏輯推導出來的其他事實是否也隨之改變。 減輕暴露偏差：暴露偏差，即傾向於預先存在的歸納偏差而不是新的偏差，仍然是自然語言生成中的一個挑戰，影響在固定資料集上訓練的LLM的輸出品質88。 諸如選擇性升級之類的解決方案可以動態派生相關的指令-響應對，旨在透過提高LLM有效泛化其訓練資料之外的能力來解決這一問題89。

### 更好的評估

現有的評估方法（例如 BERTScore90 和 MoverScore91）假設類似的訓練和評估資料分佈，這與LLM不斷發展的能力和要求不符。 這種差異在涉及零樣本指令和情境學習的場景中尤其明顯，這些場景突顯了不同的資料分佈場景。 最近提出的評估措施（例如 GPTScore64 和 G-Eval65）在各種任務中顯示出與人類評估的合理相關性，包括一致性、準確性和正確性。 然而，事實性評估中的相關性較弱（約 20-25%）64，這表明仍有改進的空間。 一個潛在的方向是為特定領域（例如醫學或法律）客製化事實性說明。 類似的調整已經證明了SelfCheckGPT66 的事實性評估得到了改善，該評估基於這樣的想法：一致的可複製響應植根於事實準確性，而不是通過隨機採樣或幻覺生成的響應，後者往往表現出更多的變化。 

### 隱私和資料保護

雖然 OpenAI 等組織已經實施了隱私控制並定期進行網路安全審計92，但用戶研究呼籲人工智慧系統遵守額外的資料保護法規，強調資料匿名化、聚合和差異隱私等步驟93。 雖然歐盟的人工智慧法案 94 根據已確定的風險等級規定了與透明度相關的義務，但更嚴格的監管可能會促進對第三方事實驗證 API/外掛程式的存取。 當驗證對對話至關重要時，聊天機器人用戶可以選擇使用此類工具。 

### 辨識人工智慧產生的內容

LLM的輸出已經與人類所寫的文本幾乎無法區分95。 例如，偵測人工智慧產生內容的最先進工具無法區分合法的 Twitter/X 帳戶和透過 ChatGPT31 管理的帳戶。 此外，先前根據自動產生的假新聞訓練資料訓練的錯誤訊息偵測器 96 在偵測人類產生或編輯的假內容 97 方面仍然表現不佳。 未來的模型可能會進一步縮小這一差距，從而使標記人工智慧生成的文本的嘗試變得不可靠。 水印也很容易被惡意行為者繞過。 因此，研究多個領域、多種語言的多個生成器並使用不同的檢測器非常重要，並且維護不斷增長的最新機器生成內容的集合，例如 M4 存儲庫95。 這個問題與深度造假技術在各種媒體格式中的快速發展並行，包括虛假視頻、操縱圖像、更改的音頻剪輯和風格化文本98,99。 複雜策略的出現，例如旨在逃避偵測的釋義攻擊和抵抗影像和視訊壓縮編解碼器的對抗性擾動100，強調了解決這些問題的迫切需求。 設計一種類似於貓捉老鼠遊戲的強大且萬無一失的檢測技術仍然是一項艱鉅的挑戰。 

### 內容真實性與來源

- 隨著人工智慧生成的文字變得無所不在，完全由人類編寫的文字可能會變得更有價值。 
- 針對視訊和圖像內容的內容真實性和來源的技術和標準已經存在[^101]。 這些標準描述了一種對內容進行加密簽署的方法，以便可以證明其創建的元資料沒有被更改。 我們可以對文字內容使用類似的方法來證明它們不是人工智慧生成的。 
- 由於人工智慧產生的內容在社群媒體上傳播時可能會造成傷害，因此在虛假內容傳播到許多人之前、需要對文本施加來源證明來限制虛假內容的傳播[^28]。

### 監管

- 鑑於新興技術的顛覆性影響，出現了各種監管措施。
  - 中國的一項新規定要求人工智慧產生的內容帶有浮水印，
  - 而 ChatGPT 在義大利因 [GDPR](https://zh.wikipedia.org/zh-tw/歐盟一般資料保護規範) 合規問題而被暫時禁止，但在適當遵守透明度後最終被允許102。 
- 歐盟的人工智慧法案可能是第一個監管跨多個部門的高風險人工智慧應用的法案[^94]。
- 在美國，聯邦貿易委員會已對創建誤導性工具發出警告，強調現有法規禁止此類工具，並暗示這些規則可能適用於 GenAI[^103]。 
- 類似地，加拿大自動決策指令規定了廣泛的指導方針，促進數據驅動的實踐和聯邦合規性、透明度和減少負面演算法結果104。 
- 人工智慧監管有效性面臨的挑戰之一源自於科技的快速進步。 一方面，控制LLM及其使用者可能與處理參與網路釣魚和錯誤訊息的個人一樣具有挑戰性。 另一方面，使用開源模型的不良行為者將不受監管約束。 

### 公眾教育

大眾對欺騙性「華而不實」內容的認識至關重要，就像我們對透過 Photoshop 篡改的圖像持懷疑態度一樣。 這種意識延伸到了深度偽造視覺技術。 專家為此類教育做出貢獻的一種建設性方式是透過教學影片和程式碼等資源來解釋 ChatGPT 背後的基本技術。 然而，提高對基於 LLM 的聊天機器人的認識具有挑戰性，因為它們帶來的風險需要立即關注，這與過去幾年發展的對視覺內容深度偽造的逐漸理解不同。 另一個警告是，懷疑的公民可能會失去對可信、權威資訊來源的信任，更容易受到陰謀論的影響。

[^1]: Augenstein, I., Baldwin, T., Cha, M., Chakraborty, T., Ciampaglia, G.L., Corney, D., DiResta, R., Ferrara, E., Hale, S., Halevy, A., Hovy, E., Ji, H., Menczer, F., Miguez, R., Nakov, P., Scheufele, D., Sharma, S., Zagni, G. (2023). Factuality Challenges in the Era of Large Language Models. https://doi.org/10.48550/arXiv.2310.05189
[^28]: Menczer, F., Crandall, D., Ahn, Y.-Y. & Kapadia, A. Addressing the harms of AI-generated inauthentic content. Nat. Mach. Intell. 5, 678–680, [DOI: 10.1038/s42256-023-00690-w](https://www.nature.com/articles/s42256-023-00690-w) (2023).
[^74]: Wang, Y., Li, H., Han, X., Nakov, P. & Baldwin, T. Do-not-answer: A dataset for evaluating safeguards in llms. arXiv preprint 2308.13387 (2023). 2308.13387.
[^75]: Reddy, R. G. et al. Smartbook: AI-assisted situation report generation (2023). [2303.14337](https://arxiv.org/abs/2303.14337).
[^76]: Yu, W. et al. A survey of knowledge-enhanced text generation. ACM Comput. Surv. 54, DOI: [10.1145/3512467 (2022)](https://dl.acm.org/doi/10.1145/3512467).
[^77]: Guu, K., Lee, K., Tung, Z., Pasupat, P. & Chang, M.-W. Realm: retrieval-augmented language model pre-training. [ArXiv (2020)](https://arxiv.org/abs/2002.08909).
[^78]: Filippova, K. Controlled hallucinations: learning to generate faithfully from noisy data. In Findings of the Association for Computational Linguistics: EMNLP 2020, 864–870, DOI: 10.18653/v1/2020.findings-emnlp.76 (Association for Computational Linguistics, Online, 2020).
[^94]: [EUR-Lex - 52021PC0206 - EN - EUR-Lex — eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0).
[^101]: Content Authenticity Initiative — [contentauthenticity.org](https://contentauthenticity.org/). [Accessed 08-09-2023].
[^103]: Chatbots, deepfakes, and voice clones: AI deception for sale — [ftc.gov](https://www.ftc.gov/business-guidance/blog/2023/03/chatbots-deepfakes-voice-clones-ai-deception-sale). [Accessed 08-09-2023].

[(Augenstein et al., 2023)]:  https://doi.org/10.48550/arXiv.2310.05189 "Augenstein, I., Baldwin, T., Cha, M., Chakraborty, T., Ciampaglia, G.L., Corney, D., DiResta, R., Ferrara, E., Hale, S., Halevy, A., Hovy, E., Ji, H., Menczer, F., Miguez, R., Nakov, P., Scheufele, D., Sharma, S., Zagni, G. (2023). Factuality Challenges in the Era of Large Language Models."
