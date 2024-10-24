import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestAccessibilityHelp(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Accessibility/Help.json'
        cls.load_tasks(cls, test_data_path)
    def test_1(self):
        """
        Open the accessibility help menu.
        """
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
