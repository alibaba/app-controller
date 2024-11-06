import json
import os

from Common.CustomEnum import ModelLevelEnum
from agentscope.manager import ModelManager
from agentscope.rag.llama_index_knowledge import _EmbeddingModel


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def replace(origin: str, target: str, replace: str):
    return origin.replace(target, replace)


def extract_possible_valid_json(error_json: str):
    """
    use the re to extract the max length json string from the given string
    :return:
    """
    import re
    results = re.findall(r'(\{.*\})', error_json, re.DOTALL)
    if len(results) == 0:
        return error_json
    return results[0]


def update_model_config(context):
    # Chat models
    model_manager = ModelManager.get_instance()
    for model_level in [ModelLevelEnum.Lightweight, ModelLevelEnum.Advanced]:
        config = context.get_chat_model_config(model_level)
        model_manager.load_model_configs(config)

    # Embedding model
    config = context.get_embed_model_config()
    model_manager.load_model_configs(config)


def remove_model_config(context):
    # Chat models
    model_manager = ModelManager.get_instance()
    for model_level in [ModelLevelEnum.Lightweight, ModelLevelEnum.Advanced]:
        config_name = context.get_chat_model_config_name(model_level)
        if config_name in model_manager.model_configs:
            del model_manager.model_configs[config_name]

    # Embedding model
    config_name = context.get_embed_model_config_name()
    if config_name in model_manager.model_configs:
        del model_manager.model_configs[config_name]


def load_local_model_config(file_name):
    def replace_env(target: str, key: str):
        if key in target:
            if os.environ.get(key) is not None:
                return target.replace("{" + key + "}", os.environ.get(key))
            else:
                raise Exception("Please set {} in environment variables.".format(key))
        return target

    model_manager = ModelManager.get_instance()
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            configs = json.load(f)

        updated_configs_jsons = []
        for config_json in configs:
            config_str = json.dumps(config_json)
            # replace
            config_str = replace_env(config_str, "OPENAI_BASE_URL")
            config_str = replace_env(config_str, "DASHSCOPE_API_KEY")
            config_str = replace_env(config_str, "OPENAI_API_KEY")
            # back to json
            updated_configs_jsons.append(json.loads(config_str))
        model_manager.load_model_configs(updated_configs_jsons)


def get_embed_model(emb_model_config_name):
    model_manager = ModelManager.get_instance()
    return _EmbeddingModel(model_manager.get_model_by_config_name(emb_model_config_name))


def is_existed_model_config(model_config_name):
    model_manager = ModelManager.get_instance()
    return model_config_name in model_manager.model_configs
