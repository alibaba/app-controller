import configparser
import json
import os

from Common.Utils import singleton


@singleton
class Config:
    def __init__(self, config_file):
        parser = configparser.ConfigParser()
        parser.read(config_file)

        #  App Section
        self.app = parser.get('App', 'app')
        self.app_data_dir = parser.get('App', 'app_data_dir')

        # Paths section
        self.index_dir_path = os.path.join(self.app_data_dir, "Index")
        self.metadata_dir_path = os.path.join(self.app_data_dir, "MetaData")
        self.api_dir_path = os.path.join(self.metadata_dir_path, "Apis")
        self.user_data_dir = os.path.join(self.app_data_dir, "UserData")

        # Embed Models
        self.enabled_embed_models = parser.get("Models", "enabled_embed_models").split(",")
        self.enabled_embed_models = [x.strip() for x in self.enabled_embed_models]
        self.default_embed_model_config = self.enabled_embed_models[0].split(":")[0]

        # Server section
        self.SERVER_PORT = int(parser.get('Server', 'http_port'))
        self.TEST_SERVER_PORT = int(parser.get('Server', 'TEST_SERVER_PORT'))
        self.TEST_CLIENT_PORT = int(parser.get('Server', 'TEST_CLIENT_PORT'))

        # Agents section
        self.enable_api_dependency = parser.getboolean('Agents', 'enable_api_dependency')
        self.model_response_thread_size = int(parser.get('Agents', 'model_response_thread_size'))

        # Index section
        self.api_retrieve_top_k = parser.getint('Index', 'api_retrieve_top_k')
        self.knowledge_retrieve_top_k = parser.getint('Index', 'knowledge_retrieve_top_k')

        # Scheduler section
        self.max_iteration_count = parser.getint('Scheduler', 'max_iteration_count')
        self.max_model_wrong_format_count = parser.getint('Scheduler', 'max_model_wrong_format_count')
        self.force_continue_task = parser.getboolean('Scheduler', 'force_continue_task')

        # Message section
        self.enable_stdout = parser.getboolean('Message', 'enable_stdout')

        # test
        self.test_mode = parser.getboolean('Test', 'test_mode')
        self.session_time_out = parser.getint('Test', 'session_time_out')

        # Application
        self.version = parser.get('Application', 'version')

    def get_knowledge_api_config(self, knowledge_dir_name):
        with open(os.path.join(self.metadata_dir_path, knowledge_dir_name, "config.json")) as f:
            return json.load(f)


config = Config("config.ini")
