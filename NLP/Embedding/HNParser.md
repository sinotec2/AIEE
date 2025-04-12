---
layout: default
title: 階層節點解析器
parent:  文檔之內嵌
grand_parent: 自然語言處理
nav_order: 99
date: 2024-01-25
last_modified_date: 2024-01-25 09:35:43
tags: AI chat
---


# 階層節點解析器
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

- [hnparser](https://docs.llamaindex.ai/en/v0.10.19/api/llama_index.core.node_parser.HierarchicalNodeParser.html)
- 在使用HierarchicalNodeParser时，您不需要手动为每一层设置内嵌区块大小。默认情况下，HierarchicalNodeParser会自动为您生成一个节点层次结构，其中每一层的区块大小是预先定义的：

第一层：区块大小为2048
第二层：区块大小为512
第三层：区块大小为128

这个默认设置可以帮助您从“粗到细”地解析文档内容。如果您有特定的需求，可能需要自定义这些设置，但在大多数情况下，默认值已经足够使用。
