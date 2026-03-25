
#!
# -*- coding: utf-8 -*-

"""
Ollama Docker 監控腳本

Author      : yckuang
Version     : 1.1.0
License     : MIT

功能說明
---------
此腳本會定期檢查 GPU 是否被 Ollama 服務佔用，
若 GPU 無使用或出現長期卡頓，則自動重新部署
指定的 Docker stack。

使用方式
--------
1. 在宿主機安裝 Docker、nvidia‑smi、python3 以及 pip。
2. 本機執行 `bash -c "python monitor.py"`
3. 若欲在容器內執行，請參考下方提供的 Dockerfile 及執行指令。

環境變數
---------
* CHECK_INTERVAL      : 監測間隔（秒）          (預設 60)
* MAX_UNHEALTHY       : 未回應次數斷線門檻      (預設 3)
* MAX_CPU_PERCENT     : CPU utilisation 上限（%）   (預設 80.0)
* MAX_MEMORY_PERCENT  : Memory utilisation 上限（%）(預設 80.0)
* MAX_IO_BYTES        : IO throughput 上限（B/s）   (預設 100000000)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 1️⃣ 主要模組導入
# ─────────────────────────────────────────────────────────────────────────────
from datetime import datetime
import logging
import logging.handlers
import os
import sys
import subprocess
import time
import threading
from datetime import datetime
from typing import List, Tuple, Any, Dict, Optional

import docker
import requests
from docker.errors import DockerException, NotFound

# ─────────────────────────────────────────────────────────────────────────────
# 2️⃣ 日誌設定
# ─────────────────────────────────────────────────────────────────────────────
# 建立啟動時刻 (ISO 8601 但更適合檔名)
# 例: 20241023_125959.log
START_TS  = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE  = f"ollama_monitor_{START_TS}.log"
LOG_HOME = f"/nas2/kuang/MyPrograms/ollama/ollama_restart"
LOG_PATH  = os.path.join(LOG_HOME, LOG_FILE)
MAX_BYTES    = 2 * 1024 * 1024            # 2 MB
BACKUP_COUNT = 5                          # 例如 .log, .log.1 … .log.5

# 先建立 handler
file_handler = logging.handlers.RotatingFileHandler(
    LOG_PATH,
    mode="a",
    maxBytes=MAX_BYTES,
    backupCount=BACKUP_COUNT,
    encoding="utf-8",
    delay=False
)
file_handler.setLevel(logging.INFO)
# 控制台（stdout）handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s | %(levelname)8s | %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 減少傳遞多個 handler 的複雜度：直接取得 __name__ 的 logger
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(file_handler)
log.addHandler(console_handler)

# ─────────────────────────────────────────────────────────────────────────────
# 3️⃣ 程式組態（可透過環境變數覆寫）
# ─────────────────────────────────────────────────────────────────────────────
CHECK_INTERVAL: int = int(os.getenv("CHECK_INTERVAL", "120"))
MAX_UNHEALTHY: int = int(os.getenv("MAX_UNHEALTHY", "3"))
MAX_CPU_PERCENT: float = float(os.getenv("MAX_CPU_PERCENT", "80.0"))
MAX_MEMORY_PERCENT: float = float(os.getenv("MAX_MEMORY_PERCENT", "80.0"))
MAX_IO_BYTES: int = int(os.getenv("MAX_IO_BYTES", "100000000"))

# ─────────────────────────────────────────────────────────────────────────────
# 4️⃣ 內部工具函式
# ─────────────────────────────────────────────────────────────────────────────
def dummy_inference(url: str, model: str, task: str = "寫一篇博士等級的論文，評論聊齋誌異，至少1000字。") -> bool:
    """
    送出一個「dummy」推論請求，藉此觸發 Ollama 服務的 GPU 負載。

    Args:
        url:   呼叫的 Ollama API 接點（例：http://localhost:55080）
        model: 需呼叫的模型名稱（例：`llama3.1:8b`）
        task:  要推論的文字，預設值為中文測試句

    Returns:
        bool: 若請求成功 (HTTP 200)，回傳 True；否則回傳 False
    """
    try:
        resp = requests.post(
            f"{url}/api/chat",
            json={"model": model, "messages": [{"role": "user", "content": task}]},
            timeout=30,
        )
        return resp.status_code == 200
    except Exception as exc:   # pragma: no cover - 例外時即失敗
        log.debug("dummy_inference 失敗: %s", exc)
        return False


def run_dummy(url: str, model: str) -> None:
    """
    在獨立執行緒中啟動 dummy 推論，避免阻塞主監控迴圈。
    """
    if dummy_inference(url, model):
        log.debug("Dummy 推論已送出")
    else:
        log.debug("Dummy 推論送出失敗／超時")


def _run_cmd(cmd: List[str], capture_output: bool = True) -> str:
    """執行 shell 命令，並回傳標準輸出。任何非 0 exit code 皆會拋例外。"""
    result = subprocess.run(
        cmd,
        capture_output=capture_output,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def gpu_usage_check(gpu_index: int = 0) -> Optional[int]:
    """
    讀取指定 GPU 的 memory 利用率（%）
    若無 GPU 或無法讀取，回傳 None。

    Args:
        gpu_index: GPU 在系統中的索引值 (default 0)

    Returns:
        Optional[int]: memory utilisation (%)  或 None
    """
    try:
        cmd = [
            "nvidia-smi",
            f"-i", str(gpu_index),
            "--query-gpu=utilization.memory",
            "--format=csv,noheader,nounits",
        ]
        out = _run_cmd(cmd)
        return int(out)
    except Exception as exc:  # pragma: no cover
        log.debug("gpu_usage_check 執行失敗: %s", exc)
        return None


def get_compute_pids(gpu_index: int = 0) -> List[int]:
    """
    取得目前在特定 GPU 上運行的 PCIe 油執行 PID
    """
    try:
        cmd = [
            "nvidia-smi",
            f"-i", str(gpu_index),
            "--query-compute-apps=pid",
            "--format=csv,noheader,nounits",
        ]
        raw = _run_cmd(cmd)
        return [int(pid) for pid in raw.splitlines() if pid.strip()]
    except Exception as exc:  # pragma: no cover
        log.debug("get_compute_pids 執行失敗: %s", exc)
        return []


def kill_pids(pids: List[int]) -> None:
    """
    給定欲殺掉的 PID 清單，逐一呼叫 `kill`。
    """
    for pid in pids:
        try:
            os.kill(pid, 15)  # SIGTERM
            log.info("Killed process %d on GPU", pid)
        except ProcessLookupError:
            log.debug("Process %d already dead", pid)
        except Exception as exc:
            log.warning("殺掉 %d 失敗: %s", pid, exc)


# ─────────────────────────────────────────────────────────────────────────────
# 5️⃣ Docker 相關工具
# ─────────────────────────────────────────────────────────────────────────────
def remove_service(name: str) -> None:
    """
    通過 docker‑py 移除指定服務。若不存在則忽略。

    Args:
        name: 服務名稱
    """
    try:
        client = docker.from_env()
        svc = client.services.get(name)
        svc.remove()
        log.info("✔︎ Service '%s' removed.", name)
    except NotFound:
        log.info("⚠︎ Service '%s' not found – nothing to remove.", name)


def remove_services(names: List[str]) -> None:
    for svc_name in names:
        remove_service(svc_name)


def deploy_stack(compose_file: str, stack_name: str) -> None:
    """
    以容器宿主機的 docker CLI 方式部署 stack。

    Args:
        compose_file : 目錄內 docker‑compose.yml 路徑
        stack_name   : Docker stack 名稱
    """
    cmd = ["docker", "stack", "deploy", "-c", compose_file, stack_name]
    log.info("🔄 Deploying stack '%s' from %s …", stack_name, compose_file)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        log.info("stdout:\n%s", result.stdout.strip())
        log.info("stderr:\n%s", result.stderr.strip())
        log.info("✔︎ Stack deployed successfully.")
    except subprocess.CalledProcessError as exc:   # pragma: no cover
        log.error("Stack deploy failed: %s", exc)
        raise


def reset_services(yml: str, stack: str = "ollama") -> None:
    """
    先刪除舊服務，再重新部署 stack。

    Args:
        yml   : docker‑compose.yml 檔案絕對路徑
        stack : stack 名稱，預設為 'ollama'
    """
    # 1️⃣ 刪除舊服務
    svc_names = [f"{stack}_{i}" for i in ["haproxy", "ollama"]]
    remove_services(svc_names)

    # 2️⃣ 重新部署
    deploy_stack(yml, stack)


# ─────────────────────────────────────────────────────────────────────────────
# 6️⃣ 主邏輯
# ─────────────────────────────────────────────────────────────────────────────
# 下面的列表是環境的硬編碼變量，您可以自行調整為從配置檔或 env 讀取。
stacks: List[str] = ["ollama", "ollama0"]
root_path: str = "/nas2/kuang/MyPrograms/ollama"
compose_files: List[str] = [
    f"{root_path}/docker-compose.yml",
    f"{root_path}/docker-compose.yml_llama3",
]
models: List[str] = ["gpt-oss:20b", "llama3.1:8b"]
ports: List[str] = ["55083", "55080"]
secs: List[int] = [15, 15]
base_url: str = "http://l40.sinotech-eng.com"
gpu_index: int = 0


def main() -> None:
    """
    程式入口：逐一監控設定好的 stack。

    - 監控 GPU 記憶體占用
    - 若沒有相應的進程，觸發 dummy 推論以產生 GPU 負載
    - 長期無 GPU 使用或卡頓即重啟服務
    """
    while True:
        for stack_id, stack_name in enumerate(stacks):
            time.sleep(CHECK_INTERVAL)

            url = f"{base_url}:{ports[stack_id]}"
            model = models[stack_id]
            compose_file = compose_files[stack_id]
            pids = get_compute_pids(gpu_index)
            gpu_mem = gpu_usage_check(gpu_index)

            # ① 沒有任何進程或 GPU 無使用
            if not pids or gpu_mem is None or gpu_mem <= 0:
                # ➊ 送 dummy 推論（背景執行）
                threading.Thread(target=run_dummy, args=(url, model), daemon=True).start()
                # ➋ 觀察 GPU 變化
                for i in range(secs[stack_id]):
                    time.sleep(1)
                    gpu_mem2 = gpu_usage_check(gpu_index)

                    if gpu_mem2 >  gpu_mem:
                        # 如果 GPU 已經恢復使用，清理原先可能殘留的進程
                        pids = get_compute_pids(gpu_index)
                        kill_pids(pids)
                        break
                if gpu_mem2 == gpu_mem:
                    log.info("Ollama PID %s GPU 未占用，將重啟服務", model)
                    reset_services(compose_file, stack_name)


if __name__ == "__main__":
    main()
