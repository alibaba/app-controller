import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestWorkbenchLayout(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Workbench/Layout.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Open the  "Customize Layout" dropdown.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()