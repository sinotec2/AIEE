---
layout: NoRight
title:  vLLM Integration
parent:  docs
grand_parent: FastChat
last_modified_date: 2023-11-02 15:48:15
date: 2023-11-04
tags: AI chat
nav_order: 99
---

# vLLM Integration
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

You can use [vLLM](https://vllm.ai/) as an optimized worker implementation in FastChat.
It offers advanced continuous batching and a much higher (~10x) throughput.
See the supported models [here](https://vllm.readthedocs.io/en/latest/models/supported_models.html).

## Instructions

1. Install vLLM.
    ```
    pip install vllm
    ```

2. When you launch a model worker, replace the normal worker (`fastchat.serve.model_worker`) with the vLLM worker (`fastchat.serve.vllm_worker`). All other commands such as controller, gradio web server, and OpenAI API server are kept the same.
   ```
   python3 -m fastchat.serve.vllm_worker --model-path lmsys/vicuna-7b-v1.3
   ```

   If you see tokenizer errors, try
   ```
   python3 -m fastchat.serve.vllm_worker --model-path lmsys/vicuna-7b-v1.3 --tokenizer hf-internal-testing/llama-tokenizer
   ```
