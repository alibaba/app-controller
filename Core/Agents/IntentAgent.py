from Agents.CustomAgentBase import CustomAgentBase
from Common.Config import Config
from Common.Context import Context
from Common.CustomEnum import ModelLevelEnum
from Prompt.IntentAgentPrompt import IntentAgentPrompt
from agentscope.message import Msg


class IntentAgent(CustomAgentBase):
    def __init__(self, config: Config, context: Context):
        prompt = IntentAgentPrompt(config)
        super().__init__(config, context, "Intent_Agent", prompt,
                         model_config_name=context.get_chat_model_config_name(ModelLevelEnum.Lightweight),
                         embed_model_config_name=context.get_embed_model_config_name())

    async def reply(self, x: dict = None) -> dict:
        context = x["context"]
        msg = Msg("user", self.prompt.start(context), role="user")
        self.memory.add(msg)

        model_response = await self._get_model_response(self._check_valid_response)
        model_response_json, action_type = self._parser_model_response(model_response)

        if action_type == 1:
            return True
        elif action_type == 2:
            return False

    def _parser_model_response(self, model_response):
        model_response_json = self._parser_to_json(model_response)
        return model_response_json, model_response_json["type"]

    def _check_valid_response(self, model_response):
        try:
            self._parser_model_response(model_response)
            return True
        except:
            return False
