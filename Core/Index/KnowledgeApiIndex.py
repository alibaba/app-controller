import json
import os
from llama_index.core.schema import Document

from Common.SysLogger import sys_logger
from Index.BaseIndex import BaseIndex


class KnowledgeApiIndex(BaseIndex):
    def __init__(self, config, identifier, retrieve_size, data_dir, index_dir):
        super().__init__(config, identifier, data_dir, index_dir)
        self.data_json_id = "id"
        self.retrieve_size = retrieve_size

    def _update_index(self):
        docs = []

        def traverse_directories(directory):
            for entry in os.scandir(directory):
                if entry.is_dir(follow_symlinks=False):
                    traverse_directories(entry.path)  # Recursively go into directories
                elif entry.is_file() and entry.name.endswith('.json') and entry.name != 'config.json':
                    docs.extend(self.get_docs_by_json(entry.path))

        # Start the traversal from the data_dir
        traverse_directories(self.data_dir)

        # Refresh the documents in the index
        refreshed_docs = self.index.refresh_ref_docs(docs)

        # the number of docs that are refreshed. If True in refreshed_docs, it means the doc is refreshed.
        sys_logger.info("refresh {} size is {}".format(self.identifier.lower(), len([doc for doc in refreshed_docs if doc])))

    def _get_retrieve_top_k(self):
        return self.retrieve_size

    def get_docs_by_json(self, file_path):
        nodes = []
        with open(file_path, 'r') as json_file:
            item_jsons = json.load(json_file)
            for item_json in item_jsons:
                item = item_json[self.data_json_id]
                node = Document(text=json.dumps(item_json), id_=item)
                nodes.append(node)
        return nodes
