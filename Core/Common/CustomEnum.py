from enum import Enum


class ModelLevelEnum(Enum):
    Lightweight = 1
    Advanced = 2

    @classmethod
    def from_str(cls, x: str):
        return cls[x]


class TaskFeedBackEnum(Enum):
    Success = 1
    Fail = 2
    Unknown = 3


class ResponseStatusEnum:
    TASK_API_CALL = "Task_Api_Call"
    TASK_FAILED = "Task_Failed"
    TASK_FINISHED = "Task_Finished"
    TASK_CANCELLED = "Task_Cancelled"
    TASK_EXCEPTION = "Task_Exception"
    TASK_QUESTION = "Task_Question"
    SUCCESS = "success"
