import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestKeybindingLog(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Keybinding/Log.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        View the log of dispatched keyboard shortcuts.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
