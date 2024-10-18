import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorTabKey(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/TabKey.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        '''Set the size of Tab characters.'''
        self.evaluate_task()    
    
    def test_2(self):
        '''Set the 'Tab' key to spaces.'''
        self.evaluate_task()
    
    def test_3(self):
        '''Enables tab completions.'''
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
