from abc import abstractmethod

from Api.ApiManager import ApiManager, api_manager
from Common.Config import Config
from Common.Context import Context
from Common.Recoder import Recorder
from Index.EmbedIndexManager import EmbedIndexManager, index_manager


class ChatPipeline:
    def __init__(self, config: Config, context: Context):
        self.config = config
        self.index_manager: EmbedIndexManager = index_manager
        self.api_manager = api_manager
        self.is_started = False
        self.user_input = None
        # this is used to store extra data for the pipeline. such as the commands or settings that the user has supported.
        self.metadata = {}
        self.context = context
        self.recorder = Recorder(config, context.session_id)

    @abstractmethod
    def start(self, context: Context):
        self.is_started = True
        self.user_input = context.content
        self.recorder.user_input(context.content.strip())

    @abstractmethod
    def handle_api_response(self, current_input):
        pass

    def reset(self):
        self.is_started = False
        self.user_input = None

    def add_metadata(self, key, value):
        self.metadata[key] = value
