import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorInlayHints(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/InlayHints.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        '''Enable Inlay Hints'''
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
