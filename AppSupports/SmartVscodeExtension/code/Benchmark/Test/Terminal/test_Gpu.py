import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestTerminalGPU(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Terminal/Gpu.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to enable GPU acceleration for the terminal to improve rendering speed.
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
