# SPDX-License-Identifier: AGPL-3.0-or-later
# pylint: disable=missing-class-docstring, missing-module-docstring, broad-except

import typing
import re
import logging
import requests
from flask_babel import gettext
from searx.result_types import EngineResults
from . import Plugin, PluginInfo

if typing.TYPE_CHECKING:
    from searx.extended_types import SXNG_Request
    from searx.search import SearchWithPlugins
    from . import PluginCfg

logger = logging.getLogger(__name__)

import threading, queue
import time
from markdown_it import MarkdownIt

md = MarkdownIt()

class SXNGPlugin(Plugin):
    id = "ai_oes"
    name = "AI OES"
    description = "Example AI plugin with delayed post_search"
    keywords = []

    def __init__(self, plg_cfg: "PluginCfg"):
        super().__init__(plg_cfg)
        self.pattern = re.compile(r"^ai\b", re.IGNORECASE)

        self.api_url = "http://172.20.31.7:8001/v1/chat/completions"        
        #self.api_url = "http://l40.sinotech-eng.com:8001/v1/chat/completions"        
        self.api_key = None  # openai-style key if needed
        self.info = PluginInfo(
            id=self.id,
            name=gettext("AI&#43;OES Summarizer (vLLM)"),
            description=gettext(
                "Summarizes results from sino_oes engine using a local OpenAI-compatible model (vLLM)."
            ),
            preference_section="query"
        )
        logger.debug(f"[AI_PLUGIN] Plugin {self.id} initialized successfully.")

    def pre_search(self, request, search):
        # 標記 AI 模式觸發
        if search.search_query.query.lower().startswith("ai "):
            search.search_query.query = search.search_query.query[3:].strip()
            setattr(search, "_ai_mode", True)
            self.log.debug(f"[AI_PLUGIN] Triggered AI mode, query -> {search.search_query.query}")
        return True

    def post_search(self, request, search):
        from searx.result_types import Answer
        logger = self.log
        if not getattr(search, "_ai_mode", False):
            logger.debug("[AI_PLUGIN] Not in AI mode, skip post_search.")
            return []

        container = getattr(search, "result_container", None)

        # 預先建立暫時的 Answer（顯示 loading 狀態）
        ans_str=','.join(["AI Output","🤖 AI is processing search results, please wait..."])
        placeholder = Answer(answer=ans_str)
#            plugin="ai_oes"

        results_q = queue.Queue()
        def delayed_collect():
            """等待結果完成後產出最終 Answer"""
            if not container:
                logger.warning("[AI_PLUGIN] No container found in delayed_collect.")
                return
            is_closed=None
            for _ in range(30):  # 最多等 3 秒
                is_closed = getattr(container, "closed", None)
                if is_closed is None:
                    is_closed = getattr(container, "_closed", False)            
                if is_closed:
                    break
                time.sleep(0.1)
                logger.warning(f"[AI_PLUGIN] sleep...{is_closed}")

            results = []

            # 1️⃣ 從 _main_results_sorted 撈主結果
            main_sorted = getattr(container, "_main_results_sorted", None)
            if main_sorted:
                results.extend(main_sorted)

            # 2️⃣ 檢查 main_results_map（這個結構通常是 dict[id->result]）
            main_map = getattr(container, "main_results_map", None)
            if main_map and not results:
                results.extend(main_map.values())

            #str_r=','.join([','.join([i for i in list(r.values())]) for r in results])
            str_r=','.join([str(list(r.values())[2]) for r in results])
            #logger.debug(f"[AI_PLUGIN] delayed_collect: collected {len(results)} results from _main_results_sorted/main_results_map: {str_r}")
            
            logger.debug(f"[AI_PLUGIN] delayed_collect: got {len(results)} results (closed={is_closed}).")

            # 模擬 AI 處理摘要
            if results:
                results_q.put(results)
            else:
                logger.debug("[AI_PLUGIN] No results after wait, keep placeholder.")

        threading.Thread(target=delayed_collect, daemon=True).start()
        # 等最多 5 秒等結果
        try:
            results = results_q.get(timeout=5)
        except queue.Empty:
            results = []
        if results:
            top_items = results[:30]
            text_block = []
            for i, it in enumerate(top_items, 1):
                title = getattr(it, "title", "")
                content = getattr(it, "content", "")
                for d in ['<span class="highlight">','</span>']:
                    content = content.replace(d,'')
                url = getattr(it, "url", "")
                if url.count('=')>=6:
                    url = url.split("=")[-1]
                text_block.append(f"{i}. {title}\n{content}\n{url}\n")
            query_text = getattr(search.search_query, "query", "")
            s = ','.join([t for t in text_block])
            #logger.debug(f"[AI_PLUGIN] delayed_collect: collected {len(results)} results from _main_results_sorted/main_results_map: {s}")
            prompt = (
                f"以下是查詢「{query_text}」的前 3 頁搜尋結果，"
                f"請用中文撰寫重點摘要與整合結論(不要列表)：\n\n"
                + "\n".join(text_block)
            )
            try:
                summary = md.render(self.call_vllm(prompt))
                for d in ['<code>','</code>','<p>','</p>']:
                    summary = summary.replace(d,'')
            except:
                summary = 'vLLM fail'
            placeholder = Answer(answer=f"AI 摘要: {summary}")#, plugin="ai_oes")
            container.answers.add(placeholder)
            logger.debug("[AI_PLUGIN] Final Answer appended to container.")

        return [placeholder]

    def call_vllm(self, text: str) -> str:
        """呼叫本地 vLLM 模型 (OpenAI 介面)"""
        try:
            payload = {
                "model": "openai/gpt-oss-20b",  # 改為你在 vLLM 設定的模型名稱

                "messages": [{"role": "user", "content": text}],
                "temperature": 0.1,
                "max_tokens": 100_000,
            }
            headers = {"Content-Type": "application/json"}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            response = requests.post(self.api_url, headers=headers, json=payload, timeout=20)
            response.raise_for_status()
            data = response.json()
            if "choices" in data and data["choices"]:
                return data["choices"][0]["message"]["content"].strip()
            return gettext("No content returned from AI.")
        except Exception as e:
            logger.error("vLLM error: %s", str(e))
            return gettext(f"AI error: {e}")

