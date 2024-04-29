

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

在這個更新的示例中，我們使用了 `{{add 3000 .}}` 來生成不同的主機端口，其中 `.` 是當前迭代的值，我們將其加上 3000 得到不同的主機端口。這樣，生成的端口將是 3001 到 3006，而不是 3000 到 18000。


