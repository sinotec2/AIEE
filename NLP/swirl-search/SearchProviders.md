---
layout: default
title: SearchProviders
nav_order: 99
parent: swirl搜尋引擎
grand_parent: NLP
date: 2023-11-04
last_modified_date: 2023-11-04 20:37:49
tags: AI chat report
---
<details markdown="block">
  <summary>
    Table of Contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## SearchProviders

```json
{
    "name": "Europe PubMed Central - EuropePMC.org",
    "active": true,
    "default": true,
    "authenticator": "",
    "connector": "RequestsGet",
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
    "query_template": "{url}?query={query_string}&resultType=core&format=json",
    "post_query_template": "{}",
    "http_request_headers": {},
    "page_fetch_config_json": {
        "cache": "false",
        "headers": {
            "User-Agent": "Swirlbot/1.0 (+http://swirl.today)"
        },
        "timeout": 10
},
    "query_processors": [
        "AdaptiveQueryProcessor"
    ],
    "query_mappings": "",
    "result_grouping_field": "",
    "result_processors": [
        "MappingResultProcessor",
        "CosineRelevancyResultProcessor"
    ],
    "response_mappings": "FOUND=hitCount,RESULTS=resultList.result",
    "result_mappings": "title=title,body=abstractText,author=authorString,date_published=journalInfo.printPublicationDate,date_published_display=journalInfo.dateOfPublication,url='https://europepmc.org/article/{source}/{id}',pmid,pmcid,citedByCount,journalInfo.journal.title,authorList.author[*].fullName,meshHeadingList.meshHeading[*].descriptorName,keywordList.keyword[*],chemicalList.chemical[*].name,NO_PAYLOAD",
    "results_per_query": 10,
    "credentials": "",
    "eval_credentials": "",
    "tags": [
        "EuropePMC",
        "EPMC",
        "Health"
    ]
}
```