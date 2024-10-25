import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestSymbol(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Symbol.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I need to view the definition of a specific function in a separate window.
        """
        self.evaluate_task()

    def test_2(self):
        """
        Can you show me the references of the selected variable?
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
