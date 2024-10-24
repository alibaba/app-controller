import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestExtensionMarketplace(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Extension/Marketplace.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Open extensions view.
        """
        self.evaluate_task()

    

if __name__ == "__main__":
    unittest.main()
