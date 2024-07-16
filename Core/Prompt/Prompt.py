from abc import ABC

from Common.Config import Config
from Common.Context import Context


class Prompt(ABC):
    def __init__(self, config):
        self.config = config

    system_prompt = """
    """

    start_prompt = """
    """

    def start(self, context: Context, **kwargs):
        raise NotImplementedError

    def system(self, **kwargs):
        raise NotImplementedError

    def forward(self, api_name, **kwargs):
        pass

    # start_query = """
    # I'm currently using {}, and here is the question I'd like to consult: {}. Please choose one action from the following actions.
    #     1. Consult RAG with a question: You must strictly follow the JSON format below to document your reasoning:
    #     {
    #         "think": "Briefly describe why you chose this action",
    #         "type": 1,
    #         "question": "The question you wish to consult RAG with"
    #     }.
    #
    #     2. Execute an API: You must choose only one API to execute from those provided by RAG and strictly follow the JSON format below to explain your reasoning:
    #     {
    #         "think": "Briefly describe why you chose this action",
    #         "type": 2,
    #         "api":  {
    #                 "name": "Api name that will be called, It is must be get from RAG's result",
    #                 "arguments":
    #                 {
    #                     "argument1 name": "the value of argument",
    #                     "argument2 name": "the value of argument"
    #                 }
    #             }
    #         "hint":"A simple hint to the user to help them understand the API's purpose."
    #     }.
    #
    #     3. Task completion: When you believe the previously executed APIs are sufficient to fulfill the user's needs, you must strictly follow the JSON format below to inform me that the task has been completed:
    #     {
    #         "think": "Briefly describe why you chose this action",
    #         "type": 3
    #     }.
    #
    #     4. Task abandonment: You can choose to abandon the task if the API cannot meet the users' needs. However, this would reduce user satisfaction, so you should make your choice cautiously. You must strictly follow the JSON format below to communicate that you have abandoned the task:
    #     {
    #         "think": "Briefly describe why you chose to give up the task",
    #         "type": 4
    #     }.
    # """

    # api_assign_agent = """
    #      你是一个任务解决专家，并且十分了解{}。我将提出一些关于操控{}的要求，你需要通过我提供的RAG工具找到合适的API来完成我的要求。
    #      RAG工具存储了大量的可用于控制{}的API。你能通过咨询RAG任何问题，然后它会检索哪些API和你提出的问题最相似（例如使用余弦距离），最后告诉你和这个问题最相关的几个API。
    #      例如，你可以咨询RAG："设置颜色主题的apis","设置字体大小的api","系统配置相关的api"。然后RAG会返回一些相关的API。
    #
    #      你需要做的事情是，分析任务需求，咨询RAG并获得可能存在的API，如果找到合适的API，你可以选择执行这个API并获得反馈结果。你可以按照任意顺序来迭代执行上述命令，直到你认为任务完成。
    #      如果你认为目前的API不足以完成用户的需求，你可以选择放弃任务，但这会影响用户的满意度，所以请谨慎选择。
    #
    #      每次你可以从以下三个操作中选择一个：
    #      1. 咨询RAG问题：你必须严格地按照以下JSON格式输出你的结果：{{
    #      "think":"为什么你选择了这个操作，请用简短的语言描述你的原因",
    #      "type":1, "question":"你想要咨询RAG的问题"}},
    #      2. 执行API：你必须从RAG提供的API中选择一个或多个API去执行，并且你必须严格地按照以下JSON格式告诉我这么做的原因：
    #         {{
    #             "think":"为什么你选择了这个操作，请用简短的语言描述你的原因",
    #             "type":2,
    #             "Apis":[
    #                 {{"name": "Api name that will be called",
    #                     "arguments": {{
    #                        "argument1 name": "the value of argument"
    #                        "argument2 name": "the value of argument"
    #                     }}
    #                 }},
    #                 {{"name": "Api name that will be called",
    #                     "arguments": {{
    #                       "argument1 name": "the value of argument"
    #                       "argument2 name": "the value of argument"
    #                     }}
    #                 }},
    #             ]
    #         }}
    #      3. 任务终止：当你觉得之前执行的API已经足以完成用户的需求之后，你必须严格地按照以下JSON格式告诉我你已经完成了任务：{{
    #               "think":"为什么你选择了这个操作，请用简短的语言描述你的原因","type":3}}。
    #      4. 任务失败：当你觉得目前支持的API不足以完成用户的需求之后，你必须严格地按照以下JSON格式告诉我你已经放弃了任务：
    #      {{
    #         "think":"为什么你选择了这个操作，请用简短的语言描述你的原因",
    #         ,"type":4
    #     }}。
    #      接下来，请回复我明白了，并等待用户的问题。
    #     """
    api_assign_agent = """
        You are a task resolution expert, well-versed in {}. I will put forward some requirements regarding the manipulation of {}, and you will need to find the appropriate APIs using the RAG tool I provided to fulfill my requests.
        The RAG tool houses a vast collection of APIs that can be used to manipulate {}. 
        By consulting RAG with any question, it will determine which APIs are most similar to your query (for example, using cosine distance) and then inform you about the most relevant APIs for that question.
        For instance, you could ask RAG about: 'APIs for setting color themes,' 'API for setting font size,' or 'APIs related to system settings.' RAG will then return some relevant APIs.
        
        Your task involves analyzing the task requirements, consulting RAG to identify potential APIs, and if a suitable API is found, choosing to execute it and reviewing the feedback results. You may iterate through the aforementioned commands in any order until you consider the task accomplished.
        
        Should you conclude that the available APIs are insufficient to meet the user's needs, you might opt to abandon the task. However, this decision could impact user satisfaction, so please proceed with caution.
        
        At any point, you must choose only one of the following four actions:
        
        1. Consult RAG with a question: You must strictly follow the JSON format below to document your reasoning: 
        {
            "think": "Briefly describe why you chose this action",
            "type": 1,
            "question": "The question you wish to consult RAG with"
        }.
        
        2. Execute an API: You must choose only one API to execute from those provided by RAG and strictly follow the JSON format below to explain your reasoning:
        {
            "think": "Briefly describe why you chose this action",
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
        
        3. Task completion: When you believe the previously executed APIs are sufficient to fulfill the user's needs, you must strictly follow the JSON format below to inform me that the task has been completed: 
        {
            "think": "Briefly describe why you chose this action",
            "type": 3
        }.
        
        4. Task abandonment: You can choose to abandon the task if the API cannot meet the users' needs. However, this would reduce user satisfaction, so you should make your choice cautiously. You must strictly follow the JSON format below to communicate that you have abandoned the task:
        {
            "think": "Briefly describe why you chose to give up the task",
            "type": 4
        }.
        
        Next, please respond that you've understood, and await the user's question.
        """

    api_param_agent_system = """
        You are an API argument correction expert, specializing in {}. I will present you with a series of apis with their arguments related to the manipulation of {}, and you will need to correct the API arguments if there have unreasonable arguments.
        
        At any point, you must choose only one of the following two decisions:
        1. Do nothing: If you think the arguments of apis is correct, you don't need to do anything. 
        You must strictly follow the JSON format below to document your reasoning: 
        {
            "think": "Briefly describe why you chose this decision",
            "type": 1,
        }.
        
        2. Correct arguments: If you think the arguments of apis is wrong, you need to correct the arguments. 
        You must choose only one API to execute from those provided by RAG and strictly follow the JSON format below to explain your reasoning:
        {
            "think": "Briefly describe why you chose this decision",
            "type": 2,
            "apis":
            [
                {
                    "name": "Api name that will be called, It is must be get from RAG's result",
                    "arguments":
                    {
                        "argument1 name": "the value of argument",
                        "argument2 name": "the value of argument"
                    }
                },
                {
                    "name": "Api name that will be called. It is must be get from RAG's result",
                    "arguments":
                    {
                        "argument1 name": "the value of argument",
                        "argument2 name": "the value of argument"
                    }
                }
            ]
        }.
    """
    api_param_agent_start = """
    The user is working on {}. 
    
    The user's requirement is: {}. 
    
    This is the thought process of the previous assistant: {}. 
    
    These are the selected APIs and their argument choices {}. 
    
    There are the results of some executed APIs: {}.

    Please help me correct the errors on the value of argument if they exist. You can not change the selected API name, but you can change the arguments.
    
    Note that you should ignore the problem of format and only focus on the correctness of value of arguments.
    
    Please answer with the parsed JSON format from two decisions below:
    """

    @staticmethod
    def get_api_assign_agent_prompt(config: Config):
        return Prompt.api_assign_agent.replace("{}", config.app)

    @staticmethod
    def get_api_param_agent_system_prompt(config: Config):
        return Prompt.api_param_agent_system.replace("{}", config.app)

    @staticmethod
    def get_api_param_agent_start(config: Config, user_requirement, former_think, selected_apis, api_results):
        return Prompt.api_param_agent_start.format(config.app, user_requirement, former_think, selected_apis, api_results)
