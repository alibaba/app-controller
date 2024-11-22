from Common.Constants import TextConstants


class AppControllerException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ModelFormatException(AppControllerException):
    def __init__(self, message=TextConstants.MODEL_FORMAT_EXCEPTION):
        self.message = message
        super().__init__(self.message)


class InferCountLimitedException(AppControllerException):
    def __init__(self, message=TextConstants.INFER_LOOP_LIMITED_EXCEPTION):
        self.message = message
        super().__init__(self.message)


class TaskCancelledException(AppControllerException):
    def __init__(self, message=TextConstants.TASK_CANCELLED_EXCEPTION):
        self.message = message
        super().__init__(self.message)


class InputQuestionException(AppControllerException):
    def __init__(self, message=TextConstants.INPUT_QUESTION_EXCEPTION):
        self.message = message
        super().__init__(self.message)


class ApplicationVersionException(AppControllerException):
    def __init__(self, version):
        self.message = TextConstants.APPLICATION_VERSION_EXCEPTION.format(version)
        super().__init__(self.message)
