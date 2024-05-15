---
layout: default
title: production yaml
parent: Anything LLM
grand_parent: 自然語言處理
nav_order: 99
date: 2024-04-30
last_modified_date: 2024-04-30 13:33:53
tags: AI chat
---


# 生產階段平行運作容器系統
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

### 生產階段的策略考量

- 服務對象的區隔
  - 使用者群組可以使用相同的API資源、相同的RAG背景資料庫、卻仍然保持使用者自己的對話記錄隱私。
  - 部門業務的區隔。群組至少需要到部門層級、或其以下。
- 服務人數、資料量的考量
  - 有的分組人數雖多，但非屬設計人員，
  - 有的資料量很大，但多半是圖檔、簡報檔，不是資訊量足夠的文本。

## node生產方案

### 作業程序

1. 下載原始碼：`git clone https://github.com/Mintplex-Labs/anything-llm.git`
2. 修改server/.env

```bash
SERVER_PORT=eng06.sinotech-eng.com:3014

LLM_PROVIDER='openai'
OPEN_AI_KEY=sk-***
OPEN_MODEL_PREF='gpt-3.5-turbo'

LLM_PROVIDER='anthropic'
ANTHROPIC_API_KEY=sk-***
ANTHROPIC_MODEL_PREF='claude-3-haiku-20240307'

LLM_PROVIDER='localai'
LOCAL_AI_BASE_PATH='http://eng06.sinotech-eng.com:55083/v1'
LOCAL_AI_MODEL_PREF='vicuna-7b-v1.5-16k'
LOCAL_AI_MODEL_TOKEN_LIMIT=4096

STORAGE_DIR=.../server/storage
```

3. 安裝、編譯、執行服務

```bash
nvm use v18.20.2
export NODE_ENV=
cd anything-llm
pnpm install
{ cd frontend && pnpm install && pnpm build && cp -r dist ../server/public } &
export NODE_ENV=production
{ cd server && pnpm install &&
    npx prisma generate --schema=./prisma/schema.prisma &&
    npx prisma migrate deploy --schema=./prisma/schema.prisma &&
    node ./index.js } &
{ cd collector && pnpm install && node index.js } &
```

### 注意事項

- chat embed：
  - docker作用OK，但node方案無法作用，原因未明。
  - 有關生產階段的作法，官網並不推薦node方案，且desktop方案也不提供embeded chat

## 伺服器導引到https目錄

- 伺服器都是在http上執行，embedded chat無法鑲嵌到https靜態網頁
- 是否可以將

## 迴圈設計

### docker-compose

妥善設計生成端口的方式，以便生成 3001 到 3006 的端口。以下是更新後的示例 YAML 文件：

```yaml
version: "3.9"

name: anythingllm

networks:
  anything-llm:
    driver: bridge

services:
  {{range seq 1 6}}
  anything-llm{{.}}:
    container_name: anything-llm{{.}}
    image: anything-llm:latest
    build:
      context: ../.
      dockerfile: ./docker/Dockerfile
      args:
        ARG_UID: ${UID:-1000}
        ARG_GID: ${GID:-1000}
    cap_add:
      - SYS_ADMIN
    volumes:
      - "./.env:/app/server/.env"
      - "../server/storage:/app/server/storage"
      - "../collector/hotdir/:/app/collector/hotdir"
      - "../collector/outputs/:/app/collector/outputs"
    user: "${UID:-1000}:${GID:-1000}"
    ports:
      - "{{add 3000 .}}:3001"
    env_file:
      - .env
    networks:
      - anything-llm
    extra_hosts:
      - "host.docker.internal:host-gateway"
  {{end}}
```

- 在這個更新的示例中，我們使用了 `{{add 3000 .}}` 來生成不同的主機端口，其中 `.` 是當前迭代的值，我們將其加上 3000 得到不同的主機端口。
- yaml與go lang似乎有不相容之處，這個作法會發生語言的錯誤期待。

### 模板及替換策略

- 這個方案以docker-compose.yml_template方式，將其中的$PORT抽換，這樣就可以啟動不同的docker，使用不同的端口，

### 目錄區隔方案

- 將各個影像分別在不同目錄下平行運作，如此彼此的設定與紀錄將不會互相干擾，可以有最穩定的執行效果。
- `for`指令必須行在環境中啟動`bash`，才會辨識`{01..14}`的意義，因此在腳本前必須有前綴`#!/bin/bash`，否則crontab無法執行批次檔。

```bash
#jiachi@eng06 ~
#$ cat up_anything
#!/usr/bin/bash

for i in {01..14};do
export STORAGE_LOCATION=$HOME/anythingllm$i && mkdir -p $STORAGE_LOCATION && touch "$STORAGE_LOCATION/.env" && docker run -d -p 30$i:3001 --cap-add SYS_ADMIN -v ${STORAGE_LOCATION}:/app/server/storage -v ${STORAGE_LOCATION}/.env:/app/server/.env -e STORAGE_DIR="/app/server/storage" --ip eng06.sinotech-eng.com mintplexlabs/anythingllm
done
```

### 批次停止所有的影像

```bash
#jiachi@eng06 ~
#$ cat docker_stop
#!/bin/bash
for n in $(docker ps|grep anything|awk '{print $1}');do
docker stop $n
done
```
