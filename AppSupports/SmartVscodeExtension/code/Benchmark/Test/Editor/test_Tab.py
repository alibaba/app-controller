import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorTab(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Tab.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        # Pin the tab.
        self.evaluate_task()    
    
    def test_2(self):
        # Unpin the tab.
        self.evaluate_task()
    
    def test_3(self):
        # Set the tab size.
        self.evaluate_task()
    
    def test_4(self):
        # Seperate pinned editor tabs.
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
