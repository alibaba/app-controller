import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestFile(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/File.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
       Can you set the new file to open down the current active file?
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
