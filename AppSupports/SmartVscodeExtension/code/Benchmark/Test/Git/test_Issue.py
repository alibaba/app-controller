import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestGitIssue(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Git/Issue.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Creat an issue.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
