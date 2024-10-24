import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestGitBaseAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Git/BaseAction.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Initialize a repository.
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        Stage changes in current active file.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Stage all changes.
        """
        self.evaluate_task()
    
    def test_4(self):
        """
        Unstage Changes in current active file.
        """
        self.evaluate_task()
    
    def test_5(self):
        """
        Unstage all changes.
        """
        self.evaluate_task()
    
    def test_6(self):
        """
        Discard changes in current active file.
        """
        self.evaluate_task()
    
    def test_7(self):
        """
        Set auto git sfetch.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
