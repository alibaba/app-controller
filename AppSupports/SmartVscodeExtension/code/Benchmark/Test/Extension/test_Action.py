import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestExtensionAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Extension/Action.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        '''Install an extension from a .vsix file.'''
        self.evaluate_task()

    def test_2(self):
        '''Ingore the extension recommendations.'''
        self.evaluate_task()
    
    def test_3(self):
        '''Disable all installed extensions.'''
        self.evaluate_task()
        
    def test_4(self):
        '''Disable all installed extensions in the workspace.'''
        self.evaluate_task()
    
    def test_5(self):
        '''Enable all disabled extensions.'''
        self.evaluate_task()
    
    def test_6(self):
        '''Enable all disabled extensions in the workspace.'''
        self.evaluate_task()
    
    def test_7(self):
        '''Turn off auto update for extensions.'''
        self.evaluate_task()
    
    def test_8(self):
        '''Enable the automatic update check for extensions.'''
        self.evaluate_task()
    
    def test_9(self):
        '''Check for updates for all installed extensions.'''
        self.evaluate_task()
        
    
    

if __name__ == "__main__":
    unittest.main()
