import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestGitCommit(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Git/Commit.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Git undo commit.
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        Git commit.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
