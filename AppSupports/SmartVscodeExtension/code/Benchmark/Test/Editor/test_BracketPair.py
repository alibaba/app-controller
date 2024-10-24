import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorBracketPair(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/BracketPair.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        """
        Enable the colorization of matching bracket pairs.
        """
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
