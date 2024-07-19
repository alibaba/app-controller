import json
import os

from Common.CustomEnum import ModelLevelEnum
from agentscope.models import read_model_configs, _MODEL_CONFIGS, load_model_by_config_name
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
    for model_level in [ModelLevelEnum.Lightweight, ModelLevelEnum.Advanced]:
        name = context.get_chat_model_config_name(model_level)
        config = context.get_chat_model_config(model_level)
        if name in _MODEL_CONFIGS:
            del _MODEL_CONFIGS[name]
        read_model_configs(config)

    # Embedding model
    name = context.get_embed_model_config_name()
    config = context.get_embed_model_config()
    if name in _MODEL_CONFIGS:
        del _MODEL_CONFIGS[name]
    read_model_configs(config)


def load_model_config(file_name):
    def replace_env(target: str, key: str):
        if key in target:
            if os.environ.get(key) is not None:
                return target.replace("{" + key + "}", os.environ.get(key))
            else:
                raise Exception("Please set {} in environment variables.".format(key))
        return target

    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            configs = json.load(f)

        updated_configs_json = []
        for config_json in configs:
            config_str = json.dumps(config_json)
            # replace
            config_str = replace_env(config_str, "OPENAI_BASE_URL")
            config_str = replace_env(config_str, "DASHSCOPE_API_KEY")
            config_str = replace_env(config_str, "OPENAI_API_KEY")
            # back to json
            updated_configs_json.append(json.loads(config_str))

        read_model_configs(updated_configs_json)


def get_embed_model(emb_model_config_name):
    return _EmbeddingModel(load_model_by_config_name(emb_model_config_name))


def is_existed_model_config(model_config_name):
    return model_config_name in _MODEL_CONFIGS
