import json

from Api.ApiRetrieverBase import ApiRetrieverBase
from Common.TimeStatistic import TimeStatistic
from Common.Config import Config
from Common.Context import Context


class SimpleApiRetriever(ApiRetrieverBase):
    def __init__(self, config: Config, context: Context):
        super().__init__(config, context)

    async def retrieve_apis(self, user_question, model_keywords, embed_model):
        TimeStatistic.start("RAG retrieval")
        nodes = []
        nodes.extend(await self.api_index.retrieval(user_question, embed_model))
        for keyword in model_keywords:
            nodes.extend(await self.api_index.retrieval(keyword, embed_model))

        apis = []
        for node in nodes:
            api_json = next(iter(json.loads(node.text).values()))
            api = self.api_manager.get_api(api_json["name"])
            if api not in apis:
                apis.append(api)
        TimeStatistic.end("RAG retrieval", self.recorder, output=True)
        return apis
