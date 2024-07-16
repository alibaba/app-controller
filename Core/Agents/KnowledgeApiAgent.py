import json
from typing import List

from Agents.CustomAgentBase import CustomAgentBase
from Api.Api import Api
from Api.ApiManager import ApiManager, api_manager
from Common.Constants import TextConstants
from Common.CustomEnum import ModelLevelEnum
from Common.Config import Config
from Common.Context import Context
from Prompt.KnowledgeApiAgentPrompt import KnowledgeApiAgentPrompt
from Index.KnowledgeApiIndex import KnowledgeApiIndex
from agentscope.message import Msg


class KnowledgeItem:
    def __init__(self, item_id, desc, example):
        self.id = item_id
        self.desc = desc
        self.example = example

    @classmethod
    def from_json(cls, data):
        if isinstance(data, str):
            data = json.loads(data)
        return KnowledgeItem(data["id"], data["desc"], data.get("example", None))

    def to_json(self):
        return {"id": self.id, "desc": self.desc, "example": self.example}


class KnowledgeApiAgent(CustomAgentBase):
    def __init__(self, config: Config, context: Context, name, agent_config: dict):
        api_json, model_level = self.parser(agent_config)
        prompt = KnowledgeApiAgentPrompt(config, api_json)
        super().__init__(config, context, "{}_Agent".format(name), prompt,
                         model_config_name=context.get_chat_model_config_name(model_level),
                         embed_model_config_name=context.get_embed_model_config_name())
        self.index: KnowledgeApiIndex = self.index_manager.get_index(name, context.get_embed_model_name(config))
        self.api_manager: ApiManager = api_manager

    def parser(self, agent_config):
        return agent_config["api"], ModelLevelEnum.from_str(agent_config["chatModelLevel"])

    async def reply(self, x: dict = None) -> dict:
        context = x["context"]
        user_input = context.content

        _candidates: List[KnowledgeItem] = await self._retrieve(user_input)
        self.recorder.rag("Candidate: {}".format([c.id for c in _candidates]))

        if len(_candidates) != 0:
            msg = Msg("user", self.prompt.start(context, content=json.dumps([c.to_json() for c in _candidates])), role="user")
            self.memory.add(msg)

            model_response = await self._get_model_response(self._check_valid_response)
            model_response_json = self._parser_to_json(model_response)
            action = self._get_action_type(model_response_json)

            if action == 1:
                api: Api = self._get_apis_from_content(model_response_json)
                if TextConstants.KnowledgeApiContents not in x:
                    x[TextConstants.KnowledgeApiContents] = []
                x[TextConstants.KnowledgeApiContents].append(self.prompt.forward(api.parameterized_api()))
            self.recorder.separate()
        return x

    async def _retrieve(self, user_input) -> List[KnowledgeItem]:
        nodes = await self.index.retrieval(user_input, self.embed_model)
        items = []
        for node in nodes:
            items.append(KnowledgeItem.from_json(node.text))
        return items

    def _get_action_type(self, model_response_json):
        return model_response_json["type"]

    def _check_valid_response(self, model_response):
        try:
            model_response_json = self._parser_to_json(model_response)
            action_type = self._get_action_type(model_response_json)
            if action_type == 1:
                self._get_apis_from_content(model_response_json)
            return True
        except:
            return False

    def _get_apis_from_content(self, model_response_json):
        api_json = model_response_json["api"]
        name = api_json["name"].split(".")[-1]
        arguments = api_json["arguments"]
        api = self.api_manager.get_api(name)
        api.arguments = arguments
        return api
