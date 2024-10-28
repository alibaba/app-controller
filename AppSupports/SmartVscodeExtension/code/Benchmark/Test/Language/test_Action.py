import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestLanguageAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Language/Action.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to change the language in VScode.
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
