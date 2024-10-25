import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestZen(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Zen.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to enable Zen mode to focus on my coding.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I want to change the Zen Mode settings to hide the Activity bar and Status bar, but I still want to see the line numbers.
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
