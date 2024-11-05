from abc import abstractmethod
from typing import List

from Agents.CustomAgentBase import CustomAgentBase
from Api.ApiManager import api_manager
from Common.Config import Config
from Common.Context import Context
from Common.Recoder import Recorder
from Index.EmbedIndexManager import EmbedIndexManager, index_manager


class ChatPipeline:
    def __init__(self, config: Config, context: Context):
        self.config = config
        self.index_manager: EmbedIndexManager = index_manager
        self.api_manager = api_manager
        self.is_task_cancelled = False
        self.user_input = None
        # this is used to store extra data for the pipeline. such as the commands or settings that the user has supported.
        self.metadata = {}
        self.context = context
        self.agents: List[CustomAgentBase] = []
        self.recorder = Recorder(config, context.session_id)

    @abstractmethod
    def start(self, context: Context):
        self.user_input = context.content
        self.recorder.user_input(context.content.strip())

    @abstractmethod
    def handle_api_response(self, current_input):
        pass

    def reset(self):
        self.is_task_cancelled = False
        self.user_input = None
        [agent.reset() for agent in self.agents]

    def stop_task(self):
        self.is_task_cancelled = True
        [agent.stop_task() for agent in self.agents]

    def add_metadata(self, key, value):
        self.metadata[key] = value
