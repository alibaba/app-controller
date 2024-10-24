import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestGitRemote(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Git/Remote.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Add a new remote.
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        Remove a remote.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
