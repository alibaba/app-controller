import json
import os

from Api.Api import Api
from Common.Config import Config
from Common.Utils import singleton


@singleton
class ApiManager:
    def __init__(self, config):
        self.config = config
        self.name_2_api = {}

    def get_api(self, name):
        return self.name_2_api[name]

    def init(self) -> None:
        dir_path: str = self.config.api_dir_path
        apis = []
        for name in os.listdir(dir_path):
            full_file_path = os.path.join(dir_path, name)
            if os.path.isfile(full_file_path):
                apis.extend(self._load_api_from_file(full_file_path))

        for api in apis:
            self.name_2_api[api.name] = api
        pass

    def _load_api_from_file(self, file_path):
        apis = []
        with open(file_path, 'r') as json_file:
            for name, api_json in json.load(json_file).items():
                apis.append(Api.from_config_json(self.config, api_json))
        return apis


api_manager = ApiManager(Config())
api_manager.init()
