from Common.CustomEnum import ResponseStatusEnum


class Response:
    def __init__(self, status, data):
        self.status = status
        self.data = data

    @classmethod
    def get_api_response(cls, apis, is_terminal_api):
        return Response(ResponseStatusEnum.TASK_API_CALL, {"apis": apis, "isTerminal": is_terminal_api})

    @classmethod
    def get_task_failed_response(cls, reason):
        return Response(ResponseStatusEnum.TASK_FAILED, {"reason": reason})

    @classmethod
    def get_task_finished_response(cls):
        return Response(ResponseStatusEnum.TASK_FINISHED, None)

    @classmethod
    def get_task_cancelled_response(cls, msg=None):
        return Response(ResponseStatusEnum.TASK_CANCELLED, {"msg": msg})

    @classmethod
    def get_task_question_response(cls):
        return Response(ResponseStatusEnum.TASK_QUESTION, {})

    @classmethod
    def get_exception_response(cls, msg="There is an exception in the task, Please try again later."):
        return Response(ResponseStatusEnum.TASK_EXCEPTION, {"msg": msg})

    @classmethod
    def get_success_response(cls, msg=None):
        return Response(ResponseStatusEnum.SUCCESS, {"msg": msg})

    def to_json(self):
        return {
            "status": self.status,
            "data": self.data
        }
