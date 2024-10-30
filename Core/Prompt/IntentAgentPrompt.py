import json

from Common.Context import Context
from Prompt.Prompt import Prompt


class IntentAgentPrompt(Prompt):
    def __init__(self, config):
        super().__init__(config)

    system_prompt = """
        #CONTEXT#
        I am using {Application}, please help me determine if my input is a question or a task. A task is something that needs to be completed using {Application}. Otherwise, it is considered a question.
        ############
        #OBJECTIVE#
        {context}
        If my input is a question, Please respond in the following JSON format:
        {
            "type": 1
        }
        If my input is a task, inform me using the following JSON format:
        {
            "type": 2  
        }
    """

    start_prompt = """
        My input is {Input}, Please respond in the JSON format.
    """

    def start(self, context: Context, **kwargs):
        return self.start_prompt.replace("{Input}", context.content)

    def system(self, **kwargs):
        return self.system_prompt.replace("{Application}", self.config.app)
