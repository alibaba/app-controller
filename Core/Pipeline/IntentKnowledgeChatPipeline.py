import asyncio
import json
import os
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from typing import List

from Agents.KnowledgeApiAgent import KnowledgeApiAgent
from Agents.IntentAgent import IntentAgent
from Common.ChatReposne import Response
from Common.Config import Config
from Common.Context import Context
from Pipeline.KnowledgeChatPipeline import KnowledgeAgentChatPipeline
from Pipeline.SimpleChatPipeline import SimpleChatPipeline

process_pool_executor = ProcessPoolExecutor(max_workers=8)
thread_pool_executor = ThreadPoolExecutor(max_workers=8)


class IntentKnowledgeAgentChatPipeline(KnowledgeAgentChatPipeline):
    def __init__(self, config: Config, context: Context):
        super().__init__(config, context)

    def _init_agents(self):
        super()._init_agents()
        self.intent_agent = IntentAgent(self.config, self.context)
        self.agents.append(self.intent_agent)

    async def start(self, context):
        super(SimpleChatPipeline, self).start(context)
        messages = {"context": context}

        is_question = await self.is_question(messages)
        if is_question:
            return Response.get_task_question_response()

        await asyncio.gather(
            *(knowledge_api_agent.reply(messages) for knowledge_api_agent in self.knowledge_api_agents)
        )
        data: dict = await self.api_scheduler_agent.reply(messages)
        return data.get("response")

    async def is_question(self, messages):
        return await self.intent_agent.reply(messages)
