import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestView(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/View.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Can you open the editor playground ?
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        I need to close all the editors that are currently open in my workspace.
        """
        self.evaluate_task()

    def test_3(self):
        """
        I need to open the welcome page again
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
