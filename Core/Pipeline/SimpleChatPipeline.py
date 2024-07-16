from Common.ChatReposne import Response
from Common.Context import Context
from Pipeline.ChatPipeline import ChatPipeline
from Agents.ApiScheduleAgent import ApiScheduleAgent
from Common.Config import Config


class SimpleChatPipeline(ChatPipeline):
    def __init__(self, config: Config, context: Context):
        super().__init__(config, context)
        self._init_agents()

    def _init_agents(self):
        self.api_scheduler_agent = ApiScheduleAgent(self.config, self.context)

    async def start(self, context):
        super(SimpleChatPipeline, self).start(context)
        data = self.api_scheduler_agent.reply({"context": context})
        return data.get("response")

    async def handle_api_response(self, context: Context):
        api_results = context.content
        data: dict = await self.api_scheduler_agent.handle_api_response(api_results)
        return data.get("response")

    def reset(self):
        super().reset()
        self.api_scheduler_agent.reset()
