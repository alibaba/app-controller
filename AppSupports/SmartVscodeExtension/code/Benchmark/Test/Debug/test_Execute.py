import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestExecute(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Debug/Execute.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to debug my program using the current configuration.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I need to stop the debugging process for my current project.
        """
        self.evaluate_task()

    def test_3(self):
        """
        I need to restart the debug session for my current project."
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
