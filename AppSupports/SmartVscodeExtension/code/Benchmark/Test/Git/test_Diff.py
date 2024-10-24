import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestGitDiff(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Git/Diff.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Open changes of the current file by git.
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        Open changes of the repository by git.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Set the diff editor shows to side by side.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
