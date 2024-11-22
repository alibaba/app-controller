from Common.Config import config
from Common.Constants import TextConstants
from Common.CustomEnum import ModelLevelEnum
from agentscope.manager import ModelManager

from Exception.Exception import ApplicationVersionException


class Context:
    def __init__(self, user_id, session_id, content, environments, chat_model_config,
                 embedding_model_config, is_test, test_answer, application_version, enable_free_token=False):
        # the user id is used to identify the user. Each user should have a unique user id.
        self.user_id = user_id

        # the session id is used to identify the session for the user's input. Each input should have a unique session id.
        self.session_id = session_id

        # the user input
        self.content = content

        # the extra environment information for your application
        self.environments = environments

        # for model
        self.chat_model_config = chat_model_config
        self.embedding_model_config = embedding_model_config

        # for test
        self.is_test = is_test
        self.test_answer = test_answer

        self.application_version = application_version
        self.enable_free_token = enable_free_token

    def to_task_prompt(self):
        return """
            My task is: {}. {}
        """.format(self.content, self._get_envs_prompt(self.environments)).strip()

    @classmethod
    def from_dict(cls, x):
        return cls(x["userId"], x["sessionId"], x.get("content", None),
                   cls._parser_envs(x),
                   *cls._parser_model(x),
                   *cls._parser_test_data(x),
                   cls._parser_application_version(x),
                   *cls._parser_others(x)
                   )

    @classmethod
    def _parser_envs(cls, x):
        return x.get(TextConstants.Environment, {})

    @classmethod
    def _parser_model(cls, x):
        if TextConstants.ChatModelConfig not in x or TextConstants.EmbeddingModelConfig not in x:
            return Exception("Context missing chatModelConfig or embeddingModelConfig")

        chat_model_config = x[TextConstants.ChatModelConfig]
        embedding_model_config = x[TextConstants.EmbeddingModelConfig]

        # update config name
        for model_level in [ModelLevelEnum.Lightweight, ModelLevelEnum.Advanced]:
            chat_model_config[model_level.name]["config_name"] = x["sessionId"] + str(model_level.name) + "_chat"

        embedding_model_config["config_name"] = x["sessionId"] + "_embedding"

        cls._add_tongyi_free_api_key(chat_model_config, embedding_model_config)
        return chat_model_config, embedding_model_config

    @classmethod
    def _parser_test_data(cls, x):
        return x.get("isTest", False), x.get("testAnswer", None)

    @classmethod
    def _parser_application_version(cls, x):
        version = x.get("version", None)
        if version is None or version != config.version:
            raise ApplicationVersionException(config.version)
        return version

    @classmethod
    def _parser_others(cls, x):
        enable_free_token = x.get("enable_free_tongyi_token", False)
        return enable_free_token,

    def _get_envs_prompt(self, environments):
        prompt = ""
        for key, value in environments.items():
            if value is not None and value != "" and key is not None and key != "":
                prompt += "{}: {}\n".format(key, value)
        return "The environments are {}.".format(prompt) if prompt != "" else ""

    def get_chat_model_config_name(self, model_level: ModelLevelEnum):
        return self.chat_model_config[model_level.name]["config_name"]

    def get_chat_model_config(self, model_level: ModelLevelEnum):
        return self.chat_model_config[model_level.name]

    def get_embed_model_config_name(self):
        return self.embedding_model_config["config_name"]

    def get_embed_model_config(self):
        return self.embedding_model_config

    def get_embed_model_name(self, config):
        if self.chat_model_config is None:
            return config.default_embed_model_name

        model_manager = ModelManager.get_instance()
        model = model_manager.get_model_by_config_name(self.get_embed_model_config_name())
        return model.model_name

    @classmethod
    def _add_tongyi_free_api_key(cls, chat_model_config, embedding_model_config):
        from server import TONGYI_FREE_API_KEY

        # for chat model
        if chat_model_config["Lightweight"]["model_type"] == "dashscope_chat":
            chat_model_config["Lightweight"]["api_key"] = TONGYI_FREE_API_KEY
        if chat_model_config["Advanced"]["model_type"] == "dashscope_chat":
            chat_model_config["Advanced"]["api_key"] = TONGYI_FREE_API_KEY

        # for embedding model
        if embedding_model_config["model_type"] == "dashscope_text_embedding":
            embedding_model_config["api_key"] = TONGYI_FREE_API_KEY
