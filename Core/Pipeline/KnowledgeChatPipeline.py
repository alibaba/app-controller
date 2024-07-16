import asyncio
import json
import os
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from typing import List

from Agents.KnowledgeApiAgent import KnowledgeApiAgent
from Common.Config import Config
from Common.Constants import TextConstants
from Common.Context import Context
from Pipeline.SimpleChatPipeline import SimpleChatPipeline

process_pool_executor = ProcessPoolExecutor(max_workers=8)
thread_pool_executor = ThreadPoolExecutor(max_workers=8)


class KnowledgeAgentChatPipeline(SimpleChatPipeline):
    def __init__(self, config: Config, context: Context):
        self.knowledge_api_agents: List[KnowledgeApiAgent] = []
        super().__init__(config, context)

    def _init_agents(self):
        super()._init_agents()
        knowledge_api_dirs = [d for d in os.listdir(self.config.metadata_dir_path) if d.startswith(TextConstants.Knowledge_Api)]
        for knowledge_api_dir in knowledge_api_dirs:
            with open(os.path.join(self.config.metadata_dir_path, knowledge_api_dir, "config.json")) as f:
                self.knowledge_api_agents.append(KnowledgeApiAgent(self.config, self.context, knowledge_api_dir, json.load(f)))

    async def start(self, context):
        super(SimpleChatPipeline, self).start(context)
        messages = {"context": context}
        await asyncio.gather(
            *(knowledge_api_agent.reply(messages) for knowledge_api_agent in self.knowledge_api_agents)
        )
        data: dict = await self.api_scheduler_agent.reply(messages)
        return data.get("response")

    def reset(self):
        super().reset()
        [agent.reset() for agent in self.knowledge_api_agents]
