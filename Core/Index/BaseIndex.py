import os
from abc import ABC, abstractmethod

from llama_index.core import StorageContext, load_index_from_storage, Settings, VectorStoreIndex
from llama_index.core.base.base_retriever import BaseRetriever

from Common.SysLogger import sys_logger
from Common.TimeStatistic import TimeStatistic
from Common.Config import Config
from Common.Utils import get_embed_model


class BaseIndex(ABC):
    def __init__(self, config: Config, identifier, data_dir, index_dir):
        self.config: Config = config
        self.identifier = identifier
        self.index = None
        self.data_dir = data_dir
        self.index_dir = index_dir

    def build_index(self, emb_model_config_name):
        Settings.embed_model = get_embed_model(emb_model_config_name)
        time_identifier = "build_{}_index".format(self.identifier.lower())
        timer = TimeStatistic()
        timer.start(time_identifier)

        if self.exist_index():
            sys_logger.info("Loading index for {}".format(self.identifier))
            self._load_index()
        else:
            self.index = VectorStoreIndex([])
        self._update_index()
        self._storage_index()

        sys_logger.info("The time taken to build the index is {}".format(timer.end(time_identifier)))

    def exist_index(self):
        return os.path.exists(self.index_dir)

    async def retrieval(self, query, embed_model):
        retriever: BaseRetriever = self.index.as_retriever(similarity_top_k=self._get_retrieve_top_k(), embed_model=embed_model)
        nodes = await retriever.aretrieve(query)
        return nodes

    @abstractmethod
    def _update_index(self):
        pass

    @abstractmethod
    def _get_retrieve_top_k(self):
        return 10

    def _storage_index(self):
        self.index.storage_context.persist(persist_dir=self.index_dir)

    def _load_index(self):
        storage_context = StorageContext.from_defaults(persist_dir=self.index_dir)
        self.index = load_index_from_storage(storage_context)
