import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestWorkbenchActivityBar(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Workbench/ActivityBar.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Controls the location  of the Activity Bar.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
