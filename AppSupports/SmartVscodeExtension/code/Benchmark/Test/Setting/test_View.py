import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestSettingView(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Setting/View.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Open setting editor.
        """
        self.evaluate_task()
        
    def test_2(self):
        """
        Open global (user) setting editor.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Open workspace setting editor.
        """
        self.evaluate_task()
        
    def test_4(self):
        """
        Open default settings.json file.
        """
        self.evaluate_task()
    
    def test_5(self):
        """
        Open global settings.json file.
        """
        self.evaluate_task()
        
    def test_6(self):
        """
        Open workspace settings.json file.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
