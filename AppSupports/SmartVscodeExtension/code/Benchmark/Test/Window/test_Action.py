import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestWindowAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Window/Action.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        """
        Copy the current editor into a new window.
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        Move the active editor into a new window.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Control whether files should open in a new window.
        """
        self.evaluate_task()
    
    def test_4(self):
        """
        Control whether folders should open in a new window.
        """
        self.evaluate_task()
    
    def test_5(self):
        """
        Control how windows are being reopened after starting for the first time.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
