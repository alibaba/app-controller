import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest

class TestEditorIntellisense(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Intellisense.json'
        cls.load_tasks(cls, test_data_path)
        
    def test_1(self):
        '''Enable Intellisense'''
        self.evaluate_task()
    
    def test_2(self):
        '''Accept Intellisense on Enter'''
        self.evaluate_task()
    
    def test_3(self):
        '''Set the Intellisense delay'''
        self.evaluate_task()
    
    def test_4(self):
        '''Turn on the suggestions when typing trigger characters'''
        self.evaluate_task()
    
    def test_5(self):
        '''Controls whether sorting favors words that appear close to the cursor'''
        self.evaluate_task()
    
    def test_6(self):  
        '''Controls how suggestions are pre-selected when showing the suggest list.'''
        self.evaluate_task()
    
    def test_7(self):
        '''Controls whether completions should be computed based on words in the document and from which documents they are computed.'''
        self.evaluate_task()
    
    def test_8(self):
        '''Enables a pop-up that shows parameter documentation and type information as you type.'''
        self.evaluate_task()

if __name__ == "__main__":
    unittest.main()
