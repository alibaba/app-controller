import json
from abc import ABC

from deprecated import deprecated

from Api.Api import Api
from Api.ApiManager import ApiManager, api_manager
from Common.Config import Config
from Common.Context import Context
from Common.CustomEnum import ModelLevelEnum
from Agents.CustomAgentBase import CustomAgentBase


class ApiAgentBase(CustomAgentBase, ABC):
    def __init__(self, config: Config, name, prompt, context: Context):
        super().__init__(config, context, name, prompt, context.get_chat_model_config_name(ModelLevelEnum.Advanced),
                         context.get_embed_model_config_name())
        self.enable_tool_call = False
        self.api_manager: ApiManager = api_manager

    def _get_selected_api_from_model(self, model_response_json):
        return self._get_apis_from_content(model_response_json)

    @deprecated
    def _get_apis_from_tool_calls(self, model_response):
        tool_calls = model_response.origin.choices[0].message.tool_calls
        apis = []
        if tool_calls is not None:
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                apis.append(Api(function_name, function_args, tool_call.id))
            self.memory.add(model_response.origin.choices[0].message)
            # self.memory.add(Msg(name="assistant", content=None, role="assistant",))
        return apis

    def _get_apis_from_content(self, model_response_json):
        api_json = model_response_json["api"]
        name = api_json["name"].split(".")[-1]
        arguments = api_json["arguments"]
        api = self.api_manager.get_api(name)
        api.arguments = arguments
        return api
