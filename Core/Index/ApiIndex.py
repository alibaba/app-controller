import json
import os

from llama_index.core.schema import Document

from Common.Config import Config
from Common.SysLogger import sys_logger
from Index.BaseIndex import BaseIndex


class ApiIndex(BaseIndex):
    def __init__(self, config: Config, identifier, data_dir, index_dir):
        super().__init__(config, identifier, data_dir, index_dir)

    def _update_index(self):
        docs = []
        for file in os.listdir(self.data_dir):
            # skip if the file does not end with .json
            if not file.endswith(".json"):
                continue
            docs.extend(self.get_docs_by_json(os.path.join(self.data_dir, file)))
        refreshed_docs = self.index.refresh_ref_docs(docs)

        # the number of docs that are refreshed. if True in refreshed_docs, it means the doc is refreshed.
        sys_logger.info("refresh {} size is {}".format(self.identifier.lower(), len([True for doc in refreshed_docs if doc])))

    def _get_retrieve_top_k(self):
        return self.config.api_retrieve_top_k

    def get_docs_by_json(self, file_path):
        nodes = []
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for key in data.keys():
                content = json.dumps({key: data[key]})
                node = Document(text=content, id_=key)
                nodes.append(node)
        return nodes
