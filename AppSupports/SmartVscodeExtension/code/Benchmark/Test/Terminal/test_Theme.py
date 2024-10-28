import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestTerminalTheme(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Terminal/Theme.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Set the font size of terminal.
        """
        self.evaluate_task()
        
    def test_2(self):
        """
        Set the mininum contrast ratio of terminal.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
