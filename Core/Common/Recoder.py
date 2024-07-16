import json

from loguru import logger

from Common.Config import Config
from Common.CustomEnum import TaskFeedBackEnum
from Database.Models.SessionModel import SessionModel


class Recorder:
    _instances = {}  # Stores instances of Recorder for each identifier

    def __new__(cls, config: Config, identifier):
        # Singleton implementation: return existing instance if one exists
        if identifier not in cls._instances:
            cls._instances[identifier] = super().__new__(cls)
        return cls._instances[identifier]

    def __init__(self, config: Config, identifier):
        # Prevent reinitialization of the instance
        if hasattr(self, 'initialized') and self.initialized:
            return
        self.logger = logger
        self.initialized = True

        self.config = config
        self.identifier = identifier
        self.messages = []
        self.input = None
        self.feedback = TaskFeedBackEnum.Unknown.name

    def user_input(self, message: str, record: bool = True):
        self.input = message
        self.info(message, record, label="Input")

    def api(self, message: str, record: bool = True):
        self.info(message, record, label="Api")

    def rag(self, message: str, record: bool = True):
        self.info(message, record, label="Rag")

    def model(self, message: str, record: bool = True):
        self.info(message, record, label="Model")

    def info(self, message: str, record: bool = True, label="Info"):
        if record:
            self.messages.append("[{}]".format(label) + message)
        self.logger.info("{}", message, identifier=self.identifier, label=label)

    def warning(self, message: str, record: bool = True):
        if record:
            self.messages.append("[Warning]:" + message)
        self.logger.warning(message, identifier=self.identifier)

    def error(self, message: str, record: bool = True):
        if record:
            self.messages.append("[Error]:" + message)
        self.logger.error(message, identifier=self.identifier)

    def task_failed(self):
        self.feedback = TaskFeedBackEnum.Fail.name

    async def save(self):
        pipeline = json.dumps(self.messages)
        await SessionModel.create(session_id=self.identifier, pipeline=pipeline, user_input=self.input, feedback=self.feedback)

    def separate(self):
        self.info("--------------------------------------------------", record=False)

    def _stdout_filter(self, record):
        # Filter used by the console handler to display the log
        return self.config.enable_stdout and record["extra"].get("identifier", None) == self.identifier

    def close(self):
        if self.identifier in self.__class__._instances:
            del self.__class__._instances[self.identifier]
