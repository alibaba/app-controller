import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestKeybindingView(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Keybinding/View.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Open keybinding settings.
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        Open default keybinding settings file.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Open keybinding settings file.
        """
        self.evaluate_task()
    
    def test_4(self):
        """
        View default keybinding settings.
        """
        self.evaluate_task()
    
    def test_5(self):
        """
        View extension keybinding settings.
        """
        self.evaluate_task()
    
    def test_6(self):
        """
        View user defined keybinding settings.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
