import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorTokenColor(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/TokenColor.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        # Set the color of comments.
        self.evaluate_task()  
    
    def test_2(self):
        # Turn semantic highlighting on for all themes.
        self.evaluate_task()  

if __name__ == "__main__":
    unittest.main()
