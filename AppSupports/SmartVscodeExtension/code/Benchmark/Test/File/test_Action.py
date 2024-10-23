import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestFileAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'File/Action.json'
        cls.load_tasks(cls, test_data_path)
    
    def test_1(self):
        '''Compare active file with clipboard.'''
        self.evaluate_task()
    
    def test_2(self):
        '''Format active file on save.'''
        self.evaluate_task()
    
    def test_3(self):
        '''Format active file on paste.'''
        self.evaluate_task()
    
    def test_4(self):
        '''Set the auto save.'''
        self.evaluate_task()
    
    def test_5(self):
        '''Set the auto save delay.'''
        self.evaluate_task()
    
    def test_6(self):
        '''Set the excluding files and folders in fulltext searches.'''
        self.evaluate_task()
    
    def test_7(self):
        '''Set the file associations.'''
        self.evaluate_task()
        

if __name__ == "__main__":
    unittest.main()
