import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestView(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Explorer/View.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I need to access the explorer view to manage my project files.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I want to move the Explorer View to the top of the screen.
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
