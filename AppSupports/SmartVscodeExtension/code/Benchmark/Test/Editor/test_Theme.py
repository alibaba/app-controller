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
        I want to enable the breadcrumbs at the top of my editor to quickly navigate between files and symbols.
        I need a way to quickly jump between different parts of my project without having to manually search for files or symbols.
        """
        self.evaluate_task()

    def test_5(self):
        """
        I want to change the color of the indent guides to green.
        """
        self.evaluate_task()

    def test_6(self):
        """
        I need to list all the symbols in my current file, such as classes, methods, and variables.
        """
        self.evaluate_task()

    def test_7(self):
        """
        I need to navigate to a specific symbol in my file, can you help me with that?
        """
        self.evaluate_task()

    def test_8(self):
        """
        I need to close all the editors that are currently open in my workspace.
        """
        self.evaluate_task()

    def test_9(self):
        """
        I need to open the welcome page again
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
