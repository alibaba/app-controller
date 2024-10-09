import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorDimUnfocused(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/DimUnfocused.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        # Controll whether to dim unfocused editors and terminals
        self.evaluate_task()
    
    def test_2(self):
        # Controll the opacity fraction (0.2 to 1.0) to use for unfocused editors and terminals.
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
