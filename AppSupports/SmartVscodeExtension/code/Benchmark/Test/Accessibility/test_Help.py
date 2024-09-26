import unittest
import os
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestAccessibilityHelp(BenchmarkTest):
    def setUp(self):
        super().setUp()
        self.test_data_path = 'Accessibility/Help.json'
        self.load_tasks(self.test_data_path)
    def test_1(self):
        # open the accessibility help menu
        task_id = 1
        self.evaluate_task(task_id)

if __name__ == "__main__":
    unittest.main()
