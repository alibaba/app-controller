import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest



class TestEditorWhitespace(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Whitespace.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        '''Set the color of comments.'''
        self.evaluate_task()  

if __name__ == "__main__":
    unittest.main()
