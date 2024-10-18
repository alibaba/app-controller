import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Action.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        '''Lock the current editor group'''
        self.evaluate_task()
    
    def test_2(self):
        '''Unlock the current editor group'''
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
