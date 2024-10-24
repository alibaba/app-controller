import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestExtensionLocation(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Extension/Location.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Open the location where extensions are installed.
        """
        self.evaluate_task()

    

if __name__ == "__main__":
    unittest.main()
