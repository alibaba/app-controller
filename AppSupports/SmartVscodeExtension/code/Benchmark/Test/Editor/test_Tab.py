import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorTab(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Tab.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        """
        Pin the tab.
        """
        self.evaluate_task()    
    
    def test_2(self):
        """
        Unpin the tab.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Set the tab size.
        """
        self.evaluate_task()
    
    def test_4(self):
        """
        Seperate pinned editor tabs.
        """
        self.evaluate_task()

    def test_5(self):
        """
        I want to display only one tab in my workbench editor.
        """
        self.evaluate_task()
    def test_6(self):
        """
        "I want to change the scroll bar size between the tab and editor regions to large.",
        "Can you set larger size between the tab and editor regions?"
        """
        self.evaluate_task()

    def test_7(self):
        """
        "I want to set to open new tabs on the left side of my workspace forever"
        """
        self.evaluate_task()

    def test_8(self):
        """
        "I want to enable the editor tabs to wrap and fill multiple rows above the editor region.",
        "I'd like to have my tabs arranged in multiple rows above the editor region, instead of a single row."
        """
        self.evaluate_task()

    def test_9(self):
        """
        "I want to enable the tab preview mode so that I can quickly browse through my files without opening each one in a new tab."
        """
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
