import unittest

from AppSupports.SmartVscodeExtension.code.tests.TaskTestResult import TaskTestResult
from AppSupports.SmartVscodeExtension.code.tests.utils import test_one_case


class BaseTest(unittest.TestCase):
    def setUp(self):
        pass

    def execute(self, case):
        return test_one_case(case)

    def evaluate(self, case):
        res: TaskTestResult = self.execute(case)
        self.assertTrue(res.success, res.info)
