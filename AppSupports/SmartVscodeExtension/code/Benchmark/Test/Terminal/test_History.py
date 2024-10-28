import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestTerminalHistory(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Terminal/History.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Can you adjust the number of commands kept in the terminal command history to 100
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
