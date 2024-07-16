import os
from collections import defaultdict
from concurrent.futures.thread import ThreadPoolExecutor

from Common.Config import Config
from Common.Constants import TextConstants
from Common.SysLogger import sys_logger
from Common.Utils import singleton
from Index.ApiIndex import ApiIndex
from Index.KnowledgeApiIndex import KnowledgeApiIndex


@singleton
class EmbedIndexManager:
    def __init__(self, config):
        self.config: Config = config
        self.name_2_model_2_index = defaultdict(dict)

    def build_indexes(self):
        with ThreadPoolExecutor(max_workers=1) as executor:
            futures = []
            for dir_name in os.listdir(self.config.metadata_dir_path):
                # skip non-directory files in metadata directory
                if not os.path.isdir(os.path.join(self.config.metadata_dir_path, dir_name)):
                    continue
                for extend_model_name in self.config.enabled_embed_models:
                    future = executor.submit(self._build_global_index, extend_model_name, dir_name)
                    futures.append(future)

            # wait for all threads to complete
            for future in futures:
                future.result()

        sys_logger.info("Completed building all indexes.")

    def _build_global_index(self, extend_model_name, dir_name):
        index_dir = self._get_index_path(extend_model_name, dir_name)
        data_dir = self._get_data_path(dir_name)

        if dir_name == TextConstants.API:
            index = ApiIndex(self.config, dir_name, data_dir, index_dir)
        elif dir_name.startswith(TextConstants.Knowledge_Api):
            retrieve_size = self._get_knowledge_api_retrieve_size(dir_name)
            index = KnowledgeApiIndex(self.config, dir_name, retrieve_size, data_dir, index_dir)
        else:
            return
        model_config, model_name = extend_model_name.split(":")
        index.build_index(model_config)
        self.name_2_model_2_index[dir_name][model_name] = index

    def get_index(self, category, model_name):
        return self.name_2_model_2_index[category][model_name]

    def _get_index_path(self, model_name, category):
        return os.path.join(self.config.index_dir_path, model_name, category)

    def _get_data_path(self, category):
        return os.path.join(self.config.metadata_dir_path, category)

    def _get_knowledge_api_retrieve_size(self, knowledge_api_name):
        return self.config.get_knowledge_api_config(knowledge_api_name).get("retrieve_size", self.config.knowledge_retrieve_top_k)


index_manager = EmbedIndexManager(Config())
