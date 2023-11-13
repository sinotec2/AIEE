---
layout: default
title: 原版README
parent: swirl搜尋引擎
grand_parent: 自然語言處理
nav_order: 99
date: 2023-11-04
last_modified_date: 2023-11-04 20:37:49
has_children: true
tags: AI chat report
---

# swirl README
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

<div align="center">

[![Swirl](https://docs.swirl.today/images/transparent_header_3.png)](https://www.swirl.today)

<h1>Swirl</h1>

### Swirl is open source software that simultaneously searches multiple content sources and returns AI ranked results.

[Start Searching](#-try-swirl-now-in-docker) · [Slack](https://join.slack.com/t/swirlmetasearch/shared_invite/zt-1qk7q02eo-kpqFAbiZJGOdqgYVvR1sfw) · [Key Features ](#-key-features) · [Contribute](#-contributing-to-swirl) · [Documentation](#-documentation) · [Connectors](#-list-of-connectors)
</div>

---

<br/>

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?color=088395&logoColor=blue&style=flat-square)](https://opensource.org/license/apache-2-0/)
[![GitHub Release](https://img.shields.io/github/v/release/swirlai/swirl-search?style=flat-square&color=8DDFCB&label=Release)](https://github.com/swirlai/swirl-search/releases)
[![Docker Build](https://github.com/swirlai/swirl-search/actions/workflows/docker-image.yml/badge.svg?style=flat-square&branch=main)](https://github.com/swirlai/swirl-search/actions/workflows/docker-image.yml)
[![Tests](https://github.com/swirlai/swirl-search/actions/workflows/smoke-tests.yml/badge.svg?branch=main)](https://github.com/swirlai/swirl-search/actions/workflows/smoke-tests.yml)
[![Slack](https://custom-icon-badges.demolab.com/badge/Join%20Our%20Slack-black?style=flat-square&logo=slack&color=0E21A0&logoColor=white)](https://join.slack.com/t/swirlmetasearch/shared_invite/zt-1qk7q02eo-kpqFAbiZJGOdqgYVvR1sfw)
[![Website](https://custom-icon-badges.demolab.com/badge/www.swirl.today-black?style=flat-square&logo=globe&color=241468&logoColor=white)](https://www.swirl.today)

</div>

Swirl is open source software that simultaneously searches multiple content sources and returns AI ranked results. Prompt your choice of Generative AI using the top N results to get answers incorporating your own data.

Swirl can connect to:

* Databases (SQL, NoSQL, Google BigQuery)
* Public data services (Google Programmable Search Engines, ArXiv.org, etc.)
* Enterprise sources (Microsoft 365, Jira, Miro, etc.)

And generate insights with AI and LLMs like ChatGPT. Start discovering and generating the answers you need based on your data.

Swirl is as simple as ABC: (a) Download YML, (b) Start in Docker, (c) Search with Swirl. From there, add credentials to preloaded SearchProviders to get results from more sources.

## 🚀 Try Swirl with ChatGPT 

![Swirl with ChatGPT as a configured AI Model](https://docs.swirl.today/images/Animation_1.gif)

_Swirl with ChatGPT as a configured AI Model._

>**Note**
> We need your help 🙏. Help us create more examples of things you can or want to do with Swirl. Join our [Slack Community](https://join.slack.com/t/swirlmetasearch/shared_invite/zt-1qk7q02eo-kpqFAbiZJGOdqgYVvR1sfw) to discuss and learn more. We'd be very happy to help you contribute 🤗!

<br/>

# 🔎 How Swirl Works

Swirl adapts and distributes user queries to anything with a search API - search engines, databases, noSQL engines, cloud/SaaS services, data siloes, etc. and uses Large Language Models to re-rank the unified results *without* extracting or indexing *anything*. 

![Swirl Diagram](https://docs.swirl.today/images/Animation_2.gif)

<br/>

# 🔌 List of Connectors

<img src="https://docs.swirl.today/images/Connectors_2.png" height=60% width=70%/>

➕ **For Enterprise Support on Connectors**  Contact the Swirl Team at: [support@swirl.today](mailto:support@swirl.today)  

🚀 **Help Us Expand!** Want to see a new connector? [Contribute by adding a connector](#👩‍💻-contributing-to-swirl) and join our growing community of contributors. 

<br/>

# 🔥 Try Swirl Now In Docker

## Prerequisites

* To run Swirl in Docker, you must have the latest [Docker app](https://docs.docker.com/get-docker/) for MacOS, Linux, or Windows installed and running locally.

* Windows users must also install and configure either the WSL 2 or the Hyper-V backend, as outlined in the  [System Requirements for installing Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows-install/#system-requirements).

## Start Swirl in Docker

> **Warning** 
> Make sure the Docker app is running before proceeding!

* Download the YML file: [https://raw.githubusercontent.com/swirlai/swirl-search/main/docker-compose.yaml](https://raw.githubusercontent.com/swirlai/swirl-search/main/docker-compose.yaml)

```
curl https://raw.githubusercontent.com/swirlai/swirl-search/main/docker-compose.yaml -o docker-compose.yaml
```

* *Optional*: To enable Swirl's Real-Time Retrieval Augmented Generation (RAG) in Docker, run the following commands from the Console using a valid OpenAI API key:
``` shell
export MSAL_CB_PORT=8000
export MSAL_HOST=localhost
export OPENAI_API_KEY=‘<your-OpenAI-API-key>’
```

* In MacOS or Linux, run the following command from the Console:

```
docker-compose pull && docker-compose up
```

* In Windows, run the following command from PowerShell:

```
docker compose up
```

After a few minutes the following or similar should appear:

<img src="https://docs.swirl.today/images/swirl_docker_1.png" height="70%" width="90%">

* Open this URL with a browser: <http://localhost:8000> (or <http://localhost:8000/galaxy>)

* If the search page appears, click `Log Out` at the top, right. The Swirl login page will appear.

* Enter the username `admin` and password `password`, then click `Login`.

* Enter a search in the search box and press the `Search` button. Ranked results appear in just a few seconds:

<img src="https://docs.swirl.today/images/galaxy_ui_2.png" height="70%" weight="70%">

* To view the raw JSON, open <http://localhost:8000/swirl/search/>

The most recent Search object will be displayed at the top. Click on the `result_url` link to view the full JSON Response.

## Notes 📝

> **Warning**
> The Docker version of Swirl *does not* retain any data or configuration when shut down!

:key: Swirl includes five (5) Google Programmable Search Engines (PSEs) to get you up and running right away. The credentials for these are shared with the Swirl Community.

:key: Using Swirl with Microsoft 365 requires installation and approval by an authorized company Administrator. For more information, please review the [M365 Guide](https://docs.swirl.today/M365-Guide.html) or [contact us](mailto:hello@swirl.today).

## Next Steps 👇

* Check out the details of our [latest release](https://github.com/swirlai/swirl-search/releases)!

* Head over to the [Quick Start Guide](https://docs.swirl.today/Quick-Start.html) and install Swirl locally!

<br/>

# 🌟 Key Features

| ✦ | Feature |
|:-----:|:--------|
| 📌 | [Microsoft 365 integration and OAUTH2 support](https://docs.swirl.today/M365-Guide.html) |
| 🔍 | [SearchProvider configurations](https://github.com/swirlai/swirl-search/tree/main/SearchProviders) for all included Connectors. They can be [organized with the active, default and tags properties](https://docs.swirl.today/User-Guide.html#organizing-searchproviders-with-active-default-and-tags). |
| ✏️ | [Adaptation of the query for each provider](https://docs.swirl.today/User-Guide.html#search-syntax) such as rewriting `NOT term` to `-term`, removing NOTted terms from providers that don't support NOT, and passing down the AND, + and OR operators. |
| ⏳ | [Synchronous or asynchronous search federation](https://docs.swirl.today/Developer-Guide.html#architecture) via [APIs](http://localhost:8000/swirl/swagger-ui/) |
| 🛎️ | [Optional subscribe feature](https://docs.swirl.today/Developer-Guide.html#subscribe-to-a-search) to continuously monitor any search for new results |
| 🛠️ | Pipelining of [Processor](https://docs.swirl.today/Developer-Guide.html#develop-new-processors) stages for real-time adaptation and transformation of queries, responses and results |
| 🗄️ | [Results stored](https://docs.swirl.today/Developer-Reference.html#result-objects) in SQLite3 or PostgreSQL for post-processing, consumption and/or analytics |
| ➡️ | Built-in [Query Transformation](https://docs.swirl.today/Developer-Guide.html#using-query-transformations) support, including re-writing and replacement |
| 📖 | [Matching on word stems](https://docs.swirl.today/Developer-Reference.html#cosinerelevancypostresultprocessor) and [handling of stopwords](https://docs.swirl.today/Developer-Guide.html#configure-stopwords-language) via NLTK |
| 🚫 | [Duplicate detection](https://docs.swirl.today/Developer-Guide.html#detect-and-remove-duplicate-results) on field or by configurable Cosine Similarity threshold |
| 🔄 | Re-ranking of unified results [using Cosine Vector Similarity](https://docs.swirl.today/Developer-Reference.html#cosinerelevancypostresultprocessor) based on [spaCy](https://spacy.io/)'s large language model and [NLTK](https://www.nltk.org/) |
| 🎚️ | [Result mixers](https://docs.swirl.today/Developer-Reference.html#mixers-1) order results by relevancy, date or round-robin (stack) format, with optional filtering of just new items in subscribe mode |
| 📄 | Page through all results requested, re-run, re-score and update searches using URLs provided with each result set |
| 📁 | [Sample data sets](https://github.com/swirlai/swirl-search/tree/main/Data) for use with SQLite3 and PostgreSQL |
| ✒️ | [Optional spell correction](https://docs.swirl.today/Developer-Guide.html#add-spelling-correction) using [TextBlob](https://textblob.readthedocs.io/en/dev/quickstart.html#spelling-correction) |
| ⌛ | [Optional search/result expiration service](https://docs.swirl.today/Admin-Guide.html#search-expiration-service) to limit storage use |
| 🔌 | Easily extensible [Connector](https://github.com/swirlai/swirl-search/tree/main/swirl/connectors) and [Mixer](https://github.com/swirlai/swirl-search/tree/main/swirl/mixers) objects |

<br/>

# 👩‍💻 Contributing to Swirl 

**Do you have a brilliant idea or improvement for Swirl?** We're all ears, and thrilled you're here to help!

🔗 **Get Started in 3 Easy Steps**:
1. **Connect with Fellow Enthusiasts** - Jump into the [Swirl Slack Community](https://join.slack.com/t/swirlmetasearch/shared_invite/zt-1qk7q02eo-kpqFAbiZJGOdqgYVvR1sfw) and share your ideas. You'll find a welcoming group of Swirl enthusiasts and team members eager to assist and collaborate.
2. **Branch It Out** - Always branch off from the `develop` branch with a descriptive name that encapsulates your idea or fix.
3. **Start Your Contribution** - Ready to get your hands dirty? Make sure all contributions come through a GitHub pull request. We roughly follow the [Gitflow branching model](https://nvie.com/posts/a-successful-git-branching-model/), so all changes destined for the next release should be made to the `develop` branch.

📚 **First time contributing on GitHub?** No worries, the [GitHub documentation](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) has you covered with a great guide on contributing to projects.

💡 Every contribution, big or small, makes a difference. Join us in shaping the future of Swirl!

<br/>

# ☁ Use the Swirl Cloud 

For information about Swirl as a managed service, please [contact us](mailto:hello@swirl.today)!

<br/>

# 📖 Documentation

[Overview](https://docs.swirl.today/) | [Quick Start](https://docs.swirl.today/Quick-Start) | [User Guide](https://docs.swirl.today/User-Guide) | [Admin Guide](https://docs.swirl.today/Admin-Guide) | [M365 Guide](https://docs.swirl.today/M365-Guide) | [Developer Guide](https://docs.swirl.today/Developer-Guide) | [Developer Reference](https://docs.swirl.today/Developer-Reference) | [AI Guide](https://docs.swirl.today/AI-Guide)

<br/>

# 👷‍♂️ Need Help? We're Here for You!

At Swirl, every user matters to us. Whether you're a beginner finding your way or an expert with feedback, we're here to support, listen, and help. Don't hesitate to reach out to us.

* 🎉 **Join the Conversation:** Dive into our vibrant [Swirl Community on Slack](https://join.slack.com/t/swirlmetasearch/shared_invite/zt-1qk7q02eo-kpqFAbiZJGOdqgYVvR1sfw) - it's where all the magic happens!

* 📧 **Direct Support:** For any questions, suggestions, or even a simple hello, drop us an email at [support@swirl.today](mailto:support@swirl.today). We cherish every message and promise to get back to you promptly!

* 💼 **Request A Connector (Enterprise Support)** Want to see a new connector quickly and fast. Contact the Swirl Team at: [support@swirl.today](mailto:support@swirl.today)

Remember, you're part of our family now. 🌍💙

## 名詞解釋

### swagger

Swagger是一個開源的框架和工具集，用於設計、構建、文檔化和使用RESTful Web服務。Swagger的主要目標是幫助開發人員和團隊更容易地設計和理解API，以及提供一個互動式的方式來測試和使用API。

以下是Swagger的主要特點和功能：

1. **API文檔自動生成：** Swagger允許開發人員通過註釋代碼，自動生成API的詳細文檔，包括端點、請求方法、參數、響應等信息。這使得API的文檔保持最新且易於維護。

2. **互動式API探索：** Swagger UI是Swagger的一個組件，它提供了一個互動式的Web界面，用戶可以在其中瀏覽和測試API端點。這使得開發人員可以輕鬆了解API的用法，而無需依賴其他工具。

3. **程式化的API測試：** Swagger提供了一個程式化的方式來測試API，這對於自動化測試和集成測試非常有用。您可以使用Swagger的工具來發送請求並驗證響應。

4. **支援多種語言和框架：** Swagger支援多種編程語言和Web框架，使其適用於各種技術堆棧。您可以在不同的編程語言中使用Swagger生成和使用API文檔。

5. **集成到開發工具：** Swagger可以集成到許多開發工具中，包括IDE、CI/CD工具和API管理平台，以提高開發和部署效率。

6. **規范化API設計：** Swagger遵循一個稱為OpenAPI Specification的開放標準，這使得API設計和文檔可以具有一致的格式和結構。

總的來說，Swagger是一個用於簡化API開發、文檔化和測試的工具，它使開發人員能夠更容易地理解、使用和共享API。它在許多領域和行業中廣泛應用，並有助於提高API的可靠性和可用性。

### Google Programmable Search Engines (PSEs)

Google Programmable Search Engines（PSEs）是一種由Google提供的自訂搜索引擎服務。它允許開發人員和網站擁有者創建自己的自訂搜索引擎，以便在其網站上提供更有針對性的搜索體驗。以下是有關Google Programmable Search Engines的主要特點和功能：

1. **自定義搜索範圍：** 使用PSEs，您可以指定要搜索的網站範圍，這意味著搜索結果將僅包含您指定的網站內容。這使您能夠提供與特定主題或主題相關的搜索結果。

2. **自訂外觀：** 您可以自訂PSE的外觀，以使其與您的網站風格保持一致。您可以自訂搜索框的外觀、顏色、字體等，以達到視覺一致性。

3. **簡單的集成：** Google Programmable Search Engines可以輕鬆集成到您的網站中，通常只需添加一小段HTML代碼即可。Google提供了相關的文檔和工具，以協助您完成集成。

4. **自訂排名：** 您可以使用自定義排名功能來調整搜索結果的排名，以確保特定內容在搜索結果中更容易找到。

5. **高級搜索功能：** PSEs支援高級搜索功能，如同義詞、排除詞、站內搜索等，以提供更精確的搜索結果。

6. **統計和分析：** 您可以查看關於搜索活動的統計和分析報告，以了解用戶的搜索行為和網站上最受歡迎的內容。

Google Programmable Search Engines是一個強大的工具，可讓網站擁有者為其訪問者提供定制的搜索體驗，並確保他們可以輕鬆找到所需的內容。這對於許多不同類型的網站，包括博客、教育網站、企業網站等都非常有用。

Google Programmable Search Engines（PSEs）提供兩種不同的版本：免費版和付費版。以下是它們的主要區別：

1. **免費版：** 免費版的PSEs允許您創建自訂搜索引擎，但在搜索結果頁面上可能會顯示Google廣告。此外，對於每個搜索查詢，您的PSE每天僅有一定數量的免費查詢限額。

2. **付費版：** 如果您需要更高的搜索查詢限額、自訂搜索結果中無廣告顯示，以及其他高級功能，您可以選擇使用付費版PSEs，也稱為Custom Search JSON API。這需要支付相應的費用，費用取決於您的搜索使用情況和需求。

因此，您可以根據您的需求和預算選擇使用免費版或付費版的PSEs。免費版適用於小型網站或較低的搜索需求，而付費版適用於需要更多功能和高級支援的情況。您可以訪問Google Programmable Search Engines的官方網站以瞭解詳細的價格和計劃信息。