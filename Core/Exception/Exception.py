class AppControllerException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class MaxFormatRetryException(AppControllerException):
    def __init__(self, message="Maximum number of retries exceeded for checking the model response format"):
        self.message = message
        super().__init__(self.message)
