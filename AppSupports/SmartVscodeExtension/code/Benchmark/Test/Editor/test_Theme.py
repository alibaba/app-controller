import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestTheme(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Theme.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I'd like to add vertical column rulers to the editor at the 30th, 50th, and 70th columns.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I want to set the line wrapping in the editor to 'on', so that the lines wrap at the viewport width.
        I'm having trouble reading my code because the lines are too long. Can you make it so they automatically move to the next line when they reach the edge of the screen?
        """
        self.evaluate_task()

    def test_3(self):
        """
        I want to turn off the indentation guides in the editor.
        I find the vertical lines indicating matching indent levels distracting. Can you help me get rid of them?
        """
        self.evaluate_task()

    def test_4(self):
        """
        I want to change the color of the indent guides to green.
        """
        self.evaluate_task()




if __name__ == "__main__":
    unittest.main()
