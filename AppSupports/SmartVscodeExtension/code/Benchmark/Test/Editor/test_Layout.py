import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorLayout(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Layout.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        # Duplicate the current editor into a new editor group to the left.
        self.evaluate_task()
    
    def test_2(self):
        # Toggles the layout of editor groups between vertical and horizontal orientation.
        self.evaluate_task()
    
    def test_3(self):
        # Split the current editor in the same editor group.
        self.evaluate_task()
    
    def test_4(self):
        # Toggle the split mode for the current editor group.
        self.evaluate_task()
    
    def test_5(self):
        # Toggles the layout of the split editor between vertical and horizontal orientation.
        self.evaluate_task()
    
    def test_6(self):
        # Return to a single editor in the group.
        self.evaluate_task()
        
    def test_7(self):
        # Move the editor in a floating window.
        self.evaluate_task()
    
    def test_8(self):
        # Copy the editor in a floating window.
        self.evaluate_task()
        
    

if __name__ == "__main__":
    unittest.main()
