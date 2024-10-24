import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestGitBranch(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Git/Branch.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Creat a new branch.
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        Checkout to a branch.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
