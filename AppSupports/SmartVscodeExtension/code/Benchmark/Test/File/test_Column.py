import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestFileColumn(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'File/Column.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to enable column selection mode so that I can select multiple lines of code at once.
        """
        self.evaluate_task()



if __name__ == "__main__":
    unittest.main()
