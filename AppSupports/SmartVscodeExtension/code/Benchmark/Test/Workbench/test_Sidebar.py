import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestWorkbenchSidebar(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Workbench/Sidebar.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Set the default  (Primary) side bar on the right.
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        Toggle the visibility of the side bar.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
