import json

import requests

from AppSupports.SmartVscodeExtension.code.Benchmark.Test.ResultChecker import ResultChecker
from Common.ChatReposne import Response
from Common.Config import Config
from Common.Context import Context


class TestManager:
    def __init__(self, config, context: Context):
        self.on_test_stage = context.is_test
        self.result_checker = ResultChecker(context.test_answer) if context.is_test else None
        self.config: Config = config
        self.result = None

    def check(self, result: Response):
        self.result = result
        if self.on_test_stage:
            self.result_checker.check(result)
            if self.result_checker.finish:
                self.post_back_to_unittest()

    def task_failed(self):
        if self.on_test_stage:
            self.result_checker.task_failed()
            self.post_back_to_unittest()

    def post_back_to_unittest(self):
        if self.result_checker and self.on_test_stage:
            requests.post(f"http://localhost:{self.config.TEST_CLIENT_PORT}/test_result",
                          data=json.dumps(
                              {'success': self.result_checker.success, 'info': self.result_checker.info}),
                          headers={'Content-Type': 'application/json'})
