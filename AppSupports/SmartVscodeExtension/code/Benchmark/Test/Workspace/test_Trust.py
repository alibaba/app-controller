import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestWorkspaceTrust(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Workspace/Trust.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Manage the workspace trust.
        """
        self.evaluate_task()
        
    def test_2(self):
        """
        Set the handling of untrusted files in a trusted workspace.
        """
        self.evaluate_task()
    
    def test_3(self):
        """
        Set all empty windows to be trust.
        """
        self.evaluate_task()
    
    def test_4(self):
        """
        Turn on the Workspace Trust feature.
        """
        self.evaluate_task()
    
    def test_5(self):
        """
        Control when the  startup prompt to trust a workspace is shown.
        """
        self.evaluate_task()
    
    def test_6(self):
        """
        Controls how to  handle loose files in a workspace. 
        """
        self.evaluate_task()
    
    def test_7(self):
        """
        Controls when the  Restricted Mode banner is displayed. 
        """
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
