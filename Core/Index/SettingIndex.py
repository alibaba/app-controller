import json
import os

from llama_index.core import VectorStoreIndex
from llama_index.core.schema import TextNode, Document

from Common.TimeStatistic import TimeStatistic
from Index.BaseIndex import BaseIndex
from Index.KnowledgeApiIndex import KnowledgeApiIndex


class SettingIndex(KnowledgeApiIndex):
    def __init__(self, config, identifier, data_dir, index_dir):
        super().__init__(config, identifier, data_dir, index_dir)
        self.data_json_id = "settingId"

    def _get_retrieve_top_k(self):
        return self.config.setting_retrieve_top_k
