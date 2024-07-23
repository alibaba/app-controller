from Common.Context import Context
from Prompt.Prompt import Prompt


class ApiSchedulerAgentPrompt(Prompt):
    def __init__(self, config):
        super().__init__(config)

    system_prompt = """
        # CONTEXT #
        I'm using a popular software {Application}. I will present some requirements, and you should tell me how to achieve them in {Application}. 
        However, due to special reasons, I cannot use a keyboard or mouse to complete the steps you provide. 
        Instead, I must use a series of APIs, which are developed additionally and stored in a tool called the API retriever. 
        You can provide keywords to this tool, and it will return the relevant APIs.
        ############
        
        # OBJECTIVE #
        You should complete my requirement through the following iterative process. 
        Specifically, you should choose one of the following actions to execute, wait for the results, and decide on the next action based on the results.
        Action 1:
        Purpose: Provide general and key keywords to the API retriever to find suitable APIs to complete tasks.
        Reminder: 1. These APIs implement a variety of operations that simulate human interaction with {Application}. 
        For instance, there’s a setProperties API to simulate user modifications to settings. 
        Therefore, you should first consider how my requirements are fulfilled in {Application}, and then provide the corresponding keywords. 
        2. Do not provide a keyword that has been used before.
        Output in JSON format: 
        {
            "type": 1,
            "keywords":A list of keywords. such as ["keyword1", "keyword2"]. The provided keywords should be diverse; you should not provide similar keywords.
        }
        
        Action 2:
        Purpose: Select a suitable API to execute.
        Output in JSON format: 
        {
            "type": 2,
            "terminal": "If the task can be accomplished after executing this api successfully, set it to "true". Otherwise false"
            "api":
            {
                "name": "API name from RAG's results",
                "arguments":
                {
                    "argument1 name": "value1",
                    "argument2 name": "value2"
                }
            },
        }
        
        Action 3:
        Purpose: Inform that the task cannot be completed due to insufficient APIs, chosen after a lot of attempts.
        Output in JSON format: 
        {
            "type": 3
        }
        
        Action 4:
        Purpose: Inform that the task has been finished.
        Output in JSON format: 
        {
            "type": 4
        }
        ############
        
        # RESPONSE #
        Your response must choose one action from above and adhere to the specific JSON output format required by the action.
        You absolutely cannot output any additional information.
        ############
        """

    start_prompt = "{}. You should think about how to complete it."

    retrieve_api_prompt = """There are relevant APIs for provided keywords. 
    {}. 
    Pleas select the next action.
    """

    apply_planner_prompt = "There a extra information that may help you make a decision. The information is {}. "

    stimulate_prompt = """
        I urgently needs the requirement to be completed. 
        The API that exists within RAG is sufficient to complete this task. Please consult RAG again for different APIs. Continue to think step by step.
    """

    fake_front_api_prompt = """
        {
            "type": 2,
            "terminal": false,
            "api":{Api},
        }
    """

    fill_front_api_prompt = """
           The API you selected is dependent on the execution result of {} api. The Api information is {}. Please filling the action using a standard JSON format:
            {
               "type": 2,
               "terminal": "If this API is the last one needed for the requirement, set to "true". Otherwise false"
               "api":  {
                       "name": "{}",
                       "arguments":
                       {
                           "argument1 name": "the value of argument",
                           "argument2 name": "the value of argument"
                       }
                   }
           }.
       """

    # front_api_prompt = """
    #        The Api you selected is dependent on the execution result of {} api. The Api information is {}.
    #        You must first execute the dependent Api. Please re-choose the action.
    #    """

    api_feedback_prompt = """
           The execution result of {ApiName} is {feedback}, Please choose the next action. 
       """

    metadata_prompt = """
           Before you call the {} Api, I found some relevant information to help you make a decision. The information is {}.

           Please note that this information is only part of all the information, so it may be incomplete. 

           Next, please refill the following action using a standard JSON format.
            {
               "type": 2,
               "api":  {
                       "name": "Api name that will be called, It is must be get from RAG's result",
                       "arguments":
                       {
                           "argument1 name": "the value of argument",
                           "argument2 name": "the value of argument"
                       }
                   }
               "hint":"A simple hint to the user to help them understand the API's purpose."   
           }.
       """

    def start(self, context: Context, **kwargs):
        return self.start_prompt.format(context.to_task_prompt())

    def system(self, **kwargs):
        return self.system_prompt.replace("{Application}", self.config.app)

    def simulate_to_continue(self):
        return self.stimulate_prompt

    def fill_front_api(self, api_name, api_info):
        return self.fill_front_api_prompt.replace("{}", api_name, 1).replace("{}", api_info, 1).replace("{}", api_name, 1)

    def fake_front_api(self, api_info):
        return self.fake_front_api_prompt.replace("{Api}", api_info)

    def apply_meta_data(self, api_name, extra_info):
        return self.metadata_prompt.replace("{}", api_name, 1).replace("{}", extra_info, 1)

    def apply_planner(self, content):
        return self.apply_planner_prompt.format(content)

    def retrieve_api(self, api_info):
        return self.retrieve_api_prompt.format(api_info)

    def api_feedback(self, api_name, feedback):
        return self.api_feedback_prompt.replace("{ApiName}", api_name).replace("{feedback}", feedback)
