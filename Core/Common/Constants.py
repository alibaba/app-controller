class IndexConstants:
    API = "Apis"
    KNOWLEDGE_API = "KnowledgeApi"


class TextConstants:
    Environment = "environments"
    ChatModelConfig = "chatModelConfig"
    EmbeddingModelConfig = "embeddingModelConfig"
    KnowledgeApiContents = "knowledge_api_contents"
    API = "Apis"
    Knowledge_Api = "KnowledgeApi"

    # Agent Name
    API_SCHEDULER_AGENT = "ApiSchedulerAgent"

    # Exception Description
    MODEL_FORMAT_EXCEPTION = "Maximum number of retries exceeded for checking the model response format."
    TASK_CANCELLED_EXCEPTION = "The task has been canceled, which may have been due to a timeout or manual cancellation."
    INFER_LOOP_LIMITED_EXCEPTION = "The number of inferences has exceeded the limit."
    INPUT_QUESTION_EXCEPTION = "Sorry, SmartVscode is designed to complete specific tasks in VS Code. Please enter your task instead of a question or a chat message."
    APPLICATION_VERSION_EXCEPTION = "Your extension version is outdated. Please update your extension to the latest version {}."

    # Task Status
    TASK_FAILED_MSG = "Sorry, we were unable to complete your task. This may be due to the API being unavailable or the task's complexity exceeding our capabilities."

    # Info
    API_EXECUTED_RESULT_MSG = "The result of the API execution is: {}"
    RELATED_APIS_MSG = "Related APIs: {}"


SMART_VSCODE_DEFAULT_UID = "smart_vscode_default_uid"
