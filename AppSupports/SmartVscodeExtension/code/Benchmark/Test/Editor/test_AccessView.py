import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorAccessView(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/AccessView.json'
        cls.load_tasks(cls, test_data_path)
    def test_1(self):
        '''Enable a text display in VSCode that's friendly for screen readers.'''
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
