import json

from Common.Context import Context
from Prompt.Prompt import Prompt


class KnowledgeApiAgentPrompt(Prompt):
    def __init__(self, config, api_json):
        super().__init__(config)
        self.api_name = api_json["name"]
        self.api_json = json.dumps(api_json)

    system_prompt = None

    start_prompt = """
        #CONTEXT#
        The {Application} provides a powerful api called {ApiJson}. Below is some information about the available parameters and document of this api: {content}
        ############
        #OBJECTIVE#
        {context}
        Should Api "{ApiName}" be able to help me accomplish my task with precision, please respond in the following JSON format:
        {
            "type": 1,
            "think": "The reason why you choose this action.",
            "api":
            {
                "name": "api name",
                "arguments":
                {
                    "argument1 name": "value1"
                }
            },
        }
        However, if the api is inadequate, inform me using the following JSON format:
        {
            "type": 2  
        }
    """

    forward_response = """
        #Suggestion from another assistant#
        The {Application} provides a powerful api called {ApiJson}. 
        The assistant provides API recommendations as a potential reference for fulfilling the user's requirement.
        Here are the recommended api calling: {ApiCall}.
    """

    def start(self, context: Context, **kwargs):
        return self.start_prompt.replace("{context}", context.to_task_prompt()).replace("{ApiJson}", self.api_json).replace(
            "{content}", kwargs["content"]).replace("{Application}", self.config.app).replace("{ApiName}", self.api_name)

    def system(self, **kwargs):
        return None

    def forward(self, api_call_json, **kwargs):
        return self.forward_response.replace("{Application}", self.config.app).replace("{ApiJson}", self.api_json).replace(
            "{ApiCall}", json.dumps(api_call_json, indent=4))
