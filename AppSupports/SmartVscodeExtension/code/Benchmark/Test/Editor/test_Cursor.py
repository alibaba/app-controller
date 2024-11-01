import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestCursor(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Cursor.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I need to add a cursor above the current position in my code.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I need to add a cursor below the current position in my code.
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
