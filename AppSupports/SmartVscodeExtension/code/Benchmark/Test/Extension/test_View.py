import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestExtensionView(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Extension/View.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        """
        Open extensions view.
        """
        self.evaluate_task()
    
    def test_2(self):
        """
        Show recommended extensions.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Show recently published extensions.
        """
        self.evaluate_task()
    
    def test_4(self):
        """
        Show built-in extensions.
        """
        self.evaluate_task()
    
    def test_5(self):
        """
        Show recently updated extensions.
        """
        self.evaluate_task()
    
    def test_6(self):
        """
        Show extensions that are not supported in the workspace.
        """
        self.evaluate_task()
    
    def test_7(self):
        """
        Show enabled extensions.
        """
        self.evaluate_task()
    
    def test_8(self):
        """
        Show disabled extensions.
        """
        self.evaluate_task()
    
    def test_9(self):
        """
        Clear search results in the Extension view.
        """
        self.evaluate_task()
    
    def test_10(self):
        """
        Refresh the list of extensions in the Extension view.
        """
        self.evaluate_task()
    
    def test_11(self):
        """
        Show the installed extensions.
        """
        self.evaluate_task()
    
    def test_12(self):
        """
        Show the outdated extensions.
        """
        self.evaluate_task()
    
    def test_13(self):
        """
        Show the featured extensions.
        """
        self.evaluate_task()
    
    def test_14(self):
        """
        Sort the extensions sorted by the number of installs.
        """
        self.evaluate_task()
    
    def test_15(self):
        """
        Sort the extensions sorted by name.
        """
        self.evaluate_task()
    
    def test_16(self):
        """
        Sort the extensions sorted by publication date.
        """
        self.evaluate_task()
    
    def test_17(self):
        """
        Sort the extensions sorted by rating.
        """
        self.evaluate_task()
    
    def test_18(self):
        """
        Sort the extensions sorted by updated date.
        """
        self.evaluate_task()

    

if __name__ == "__main__":
    unittest.main()
