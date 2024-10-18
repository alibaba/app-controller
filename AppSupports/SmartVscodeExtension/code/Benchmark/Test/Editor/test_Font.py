import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorFont(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Font.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        '''Increase the font size to 20'''
        self.evaluate_task()
    
    def test_2(self):
        '''Decrease the font size'''
        self.evaluate_task()
    
    def test_3(self):
        '''Enable the font ligatures'''
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
