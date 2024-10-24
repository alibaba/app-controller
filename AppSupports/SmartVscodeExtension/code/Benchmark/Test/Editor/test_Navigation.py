import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorNavigation(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Navigation.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        """
        Go to the type definition.
        """
        self.evaluate_task()    
    
    def test_2(self):
        """
        Go to the implementation.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Jump to the matching  bracket.
        """
        self.evaluate_task()
    
    def test_4(self):
        """
        Set the peek stable.
        """
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
