import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestWindowZoom(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Window/Zoom.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        """
        Zoom in the editor.
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        Zoom out the editor.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Reset the zoom level of the editor.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
