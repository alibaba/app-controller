import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestWorkspaceView(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Workspace/View.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Open the recently opened folders.
        """
        self.evaluate_task()
        
    def test_2(self):
        """
        Show all symbols in the workspace.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Go to a symbol.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
