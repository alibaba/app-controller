import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestFileView(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'File/View.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to see my recently opened files.
        """
        self.evaluate_task()

    def test_2(self):
        """
        Can you open the current file in the system window?
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
