import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorBreadcrumb(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Breadcrumb.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        '''Enable navigation breadcrumbs.'''
        self.evaluate_task()
    
    def test_2(self):
        '''Controls whether and how file paths are shown in the breadcrumbs view.'''
        self.evaluate_task()
    
    def test_3(self):
        '''Controls whether and how symbols are shown in the breadcrumbs view.'''
        self.evaluate_task()
    
    def test_4(self):
        '''Controls how symbols are sorted in the breadcrumbs outline view.'''
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
