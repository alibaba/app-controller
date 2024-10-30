import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestKeybindingAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Keybinding/Action.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Set keybinding for "collapse folders".
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()