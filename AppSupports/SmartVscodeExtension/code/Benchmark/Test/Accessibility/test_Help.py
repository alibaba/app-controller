import unittest
import os
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestAccessibilityHelp(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_data_path = 'Accessibility/Help.json'
        cls.load_tasks(cls, cls.test_data_path)
    def test_1(self):
        # open the accessibility help menu
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
