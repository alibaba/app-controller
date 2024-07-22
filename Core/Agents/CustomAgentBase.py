import asyncio
import json
from abc import ABC

from Common.Context import Context
from Common.Recoder import Recorder
from Common.TimeStatistic import TimeStatistic
from Common.Config import Config
from Index.EmbedIndexManager import EmbedIndexManager, index_manager
from Prompt.Prompt import Prompt
from agentscope.agents import AgentBase
from agentscope.message import Msg
from init import model_response_thread_pool
from Common.Utils import extract_possible_valid_json, get_embed_model


class CustomAgentBase(AgentBase, ABC):
    def __init__(self, config: Config, context: Context, name, prompt: Prompt, model_config_name, embed_model_config_name):
        super().__init__(name=name, sys_prompt=prompt.system(), model_config_name=model_config_name)
        self.context = context
        self.config = config
        self.prompt = prompt
        self.embed_model = get_embed_model(embed_model_config_name) if embed_model_config_name is not None else None
        self.index_manager: EmbedIndexManager = index_manager
        self.recorder = Recorder(config, context.session_id)

    def reset(self):
        self.memory.clear()

    def _response(self, data):
        return {"response": data}

    async def _get_model_response(self, _check_valid_response):
        while True:
            try:
                timer = TimeStatistic()
                prompt = self.model.format(Msg("system", self.prompt.system(), role="system"), self.memory.get_memory())
                timer.start("Model request")
                loop = asyncio.get_event_loop()
                model_response = await loop.run_in_executor(model_response_thread_pool, self.model, prompt)
                self.recorder.time(timer.end("Model request"))

                if _check_valid_response(model_response):
                    if model_response.text is not None:
                        self.memory.add(Msg("assistant", model_response.text, role="assistant"))
                        self.recorder.model(model_response.text)
                    return model_response
                else:
                    self.recorder.separate()
                    self.recorder.info("Invalid model response: {}. Retrying...".format(model_response.text))
                    self.recorder.separate()
            except Exception as e:
                raise e

    def _parser_to_json(self, model_response):
        response_json = json.loads(extract_possible_valid_json(model_response.text))
        return response_json
