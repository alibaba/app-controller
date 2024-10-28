import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestWorkbenchPanel(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Workbench/Panel.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Set the panel size.
        """
        self.evaluate_task()
        
    def test_2(self):
        """
        Open PROBLEMS panel.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Set the layout of the panel.
        """
        self.evaluate_task()

    def test_4(self):
        """
        Toggles the visibility of the panel area.
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
