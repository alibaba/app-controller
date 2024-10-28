import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestFileSuffix(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'File/Suffix.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I have a custom file with the extension .mydata, but it's actually a JSON file. Can you set it up so that VScode recognizes it as such?
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
