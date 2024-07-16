class TaskTestResult:
    def __init__(self, success, info) -> None:
        self.success = success
        self.info = info

    def __str__(self) -> str:
        return f"success:{self.success}, info:{self.info}"

    def __repr__(self) -> str:
        return self.__str__()
