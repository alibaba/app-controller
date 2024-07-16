from abc import ABC, abstractmethod

from Api.ApiManager import api_manager
from Common.Config import Config
from Common.Constants import TextConstants
from Common.Context import Context
from Common.Recoder import Recorder
from Index.ApiIndex import ApiIndex
from Index.EmbedIndexManager import index_manager


class ApiRetrieverBase(ABC):
    def __init__(self, config: Config, context: Context):
        self.config = config
        self.api_index: ApiIndex = index_manager.get_index(TextConstants.API, context.get_embed_model_name(config))
        self.api_manager = api_manager
        self.recorder = Recorder(config, context.session_id)

    @abstractmethod
    def retrieve_apis(self, user_question, model_question, embed_model):
        pass
