import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestGitOutput(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Git/Output.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Show git output.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
