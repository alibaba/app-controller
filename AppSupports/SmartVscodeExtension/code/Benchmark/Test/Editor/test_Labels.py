import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorLabels(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Labels.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        '''Controls the format  of the label for an editor.'''
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
