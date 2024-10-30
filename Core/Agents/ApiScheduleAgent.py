import json
from typing import List

from Api.Api import Api
from Api.SimpleApiRetriever import SimpleApiRetriever
from Common.ChatReposne import Response
from Common.Constants import TextConstants
from Common.Context import Context
from Prompt.ApiSchedulerAgentPrompt import ApiSchedulerAgentPrompt
from Agents.ApiAgentBase import ApiAgentBase
from agentscope.message import Msg
from Common.Config import Config


class ApiScheduleAgent(ApiAgentBase):
    def __init__(self, config: Config, context: Context) -> None:
        super().__init__(config, name="api_schedule_agent", prompt=ApiSchedulerAgentPrompt(config), context=context)
        self.api_retriever = SimpleApiRetriever(config, context)
        self.prompt = ApiSchedulerAgentPrompt(config)

        self.cur_iteration_count = 0
        self.trigger_failed_count = 0
        self.history_executed_apis = set()
        self.is_front_api_loop = False
        self.user_question = None

    def reset(self):
        super().reset()
        self.history_executed_apis = set()
        self.cur_iteration_count = 0
        self.user_question = None
        self.is_front_api_loop = False

    def _check_valid_response(self, model_response):
        try:
            action_type = self.get_action_type(model_response)
            model_response_json = self._parser_to_json(model_response)
            if action_type == 1:
                model_keywords = model_response_json["keywords"]
                return True if isinstance(model_keywords, list) else False
            if action_type == 2:
                api = self._get_selected_api_from_model(model_response_json)
                return True
            return True
        except:
            return False

    async def reply(self, x: dict = None) -> dict:
        context: Context = x["context"]
        knowledge_api_contents = x.get(TextConstants.KnowledgeApiContents)

        self.user_question = context.content

        self.memory.add(Msg("user", self.prompt.start(context), role="user"))

        return await self._iterate(knowledge_api_contents)

    async def handle_api_response(self, api_results) -> dict:
        self.recorder.rag("Receive api results:{}".format(api_results))

        apis_jsons = api_results if not isinstance(api_results, str) else json.loads(api_results)
        for api_json in apis_jsons:
            msg = Msg(self.name, self.prompt.api_feedback(api_json["name"], api_json["result"]), role="user")
            self.memory.add(msg)
        return await self._iterate()

    async def _iterate(self, knowledge_api_contents=None):
        while self.cur_iteration_count < self.config.max_iteration_count:
            model_response = await self._get_model_response(self._check_valid_response)
            action_type = self.get_action_type(model_response)
            model_response_json = self._parser_to_json(model_response)
            self.cur_iteration_count += 1

            if action_type == 1:
                self._add_knowledge_api_to_memory(knowledge_api_contents)
                await self._handle_ask_rag_task(model_response_json)
            elif action_type == 2:
                # fill the front api arguments
                iterate, api_call_message = self._get_api_call_message(model_response_json)
                if iterate:
                    continue
                # execute the api
                response = self._response(api_call_message)
                return response
            elif action_type == 3:
                if self.config.force_continue_task:
                    self.memory.delete(self.memory.size() - 1)
                    self.memory.add(Msg("user", self.prompt.simulate_to_continue(), role="user"))
                    return await self._iterate()
                return self._response(self._get_failed_message("Failed to finish the task, due to the lack of API"))
            elif action_type == 4:
                return self._response(self._get_success_message())
            else:
                raise ValueError("Invalid response type")
        return self._response(self._get_failed_message("Exceeded maximum number of iterations"))

    def _get_api_call_message(self, model_response_json):
        api = self._get_selected_api_from_model(model_response_json)

        # start a new iteration if the front parameterized api is found
        if self.config.enable_api_dependency:
            front_api: Api = self._search_front_api(api)
            if front_api is not None:
                self._remove_last_memory()
                self.is_front_api_loop = True
                self.recorder.info("Api Modification:{} -> {}".format(api.name, front_api.name))
                if front_api.has_parameters():
                    self.is_front_api_loop = True
                    self.memory.add(
                        Msg("user", self.prompt.fill_front_api(front_api.name, front_api.api_config_json), role="user"))
                    return True, None
                else:
                    # if the front api has no parameters, execute the front api directly and modify the system memory
                    self.memory.add(Msg("system", self.prompt.fake_front_api(front_api.api_config_json), role="system"))
                    api = front_api
        self.recorder.api(api.parameterized_api(to_str=True))
        self.history_executed_apis.add(api.name)
        # force to false if the model is request for the dependency api parameter.
        is_terminal_api = self._get_terminal_flag(model_response_json) if not self.is_front_api_loop else False
        self.is_front_api_loop = False

        return False, Response.get_api_response([api.parameterized_api()], is_terminal_api)

    def _get_failed_message(self, reason="API execution failed"):
        self.recorder.task_failed()
        return Response.get_task_failed_response(reason)

    def _get_success_message(self):
        return Response.get_task_finished_response()

    async def _handle_ask_rag_task(self, model_response_json):
        model_keywords = model_response_json["keywords"]
        apis: List[Api] = await self._retrieve_apis(self.user_question, model_keywords)

        content = self.prompt.retrieve_api(json.dumps([api.api_config_json for api in apis]))

        msg = Msg(self.name, content, role="user")
        self.memory.add(msg)

        return apis

    def get_action_type(self, model_response):
        response_json = self._parser_to_json(model_response)
        return response_json["type"]

    async def _retrieve_apis(self, user_question, model_keywords):
        apis: List[Api] = await self.api_retriever.retrieve_apis(user_question, model_keywords, self.embed_model)
        self.recorder.rag("APIs are found: {}".format([api.name for api in apis]))
        return apis

    def _search_front_api(self, api: Api):
        if api.dependency_apis is None:
            return None

        for dependent_api in api.dependency_apis:
            if dependent_api not in self.history_executed_apis:
                return self.api_manager.get_api(dependent_api)
        return None

    def _apply_dependent_apis(self, origin_apis: List[Api]):
        final_apis = []
        for origin_api in origin_apis:
            need_to_replace = False
            api: Api = self.api_manager.get_api(origin_api.name)
            if api.dependency_apis is not None:
                for dependent_api in api.dependency_apis:
                    if dependent_api not in self.history_executed_apis:
                        final_apis.append(self.api_manager.get_api(dependent_api))
                        need_to_replace = True
            if not need_to_replace:
                final_apis.append(origin_api)
        return final_apis

    def _modify_api_memory(self, selected_apis: List[Api]):
        msg = self.memory.get_memory(1)[0]
        assert msg.role == "assistant"
        model_response_json = json.loads(msg.content)
        model_response_json["api"] = [api.parameterized_api() for api in selected_apis]
        msg.content = json.dumps(model_response_json)

    def _remove_last_memory(self):
        self.memory.delete(self.memory.size() - 1)

    def _get_terminal_flag(self, model_response_json):
        return str(model_response_json.get("terminal", "")).lower() == "true"

    def _add_knowledge_api_to_memory(self, knowledge_api_contents):
        if knowledge_api_contents is None:
            return
        for knowledge_api_content in knowledge_api_contents:
            self.memory.add(Msg("user", knowledge_api_content, role="user"))
