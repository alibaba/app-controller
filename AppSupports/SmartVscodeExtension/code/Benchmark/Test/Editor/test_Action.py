import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestEditorAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Action.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        Lock the current editor group.
        """
        self.evaluate_task()

    def test_2(self):
        """
        Unlock the current editor group.
        """
        self.evaluate_task()

    def test_3(self):
        """
        I need to fold the current level where my cursor is located in the code.
        """
        self.evaluate_task()

    def test_4(self):
        """
        I need to unfold the current level where my cursor .
        """
        self.evaluate_task()

    def test_5(self):
        """
        I want to collapse all the content in my current file.
        """
        self.evaluate_task()

    def test_6(self):
        """
        I want to unfold all the contents in my current project.
        """
        self.evaluate_task()

    def test_7(self):
        """
        I need to fold all block comments in my code to make it more readable.
        """
        self.evaluate_task()

    def test_8(self):
        """
        Can you help me create a fold range for the selected text?
        """
        self.evaluate_task()

    def test_9(self):
        """
        I need to remove the manual folding ranges I've set in my code.
        """
        self.evaluate_task()

    def test_10(self):
        """
        I need to change the name of a variable in my code, can you help me with that?
        """
        self.evaluate_task()

    def test_11(self):
        """
        I need to open the global replace interface to replace words in my project.
        """
        self.evaluate_task()

    def test_12(self):
        """
        I need to scroll files together when I view multiple files at the same time.
        """
        self.evaluate_task()

    def test_13(self):
        """
        I want to increase the speed of fast scrolling when I hold down the option key.
        """
        self.evaluate_task()

    def test_14(self):
        """
        "I want to enable the Sticky Scroll feature to help me navigate through my files more easily.",
        "I'm having trouble keeping track of where I am in my files. Can you set it up so that the starting lines of the currently visible nested scopes are always shown at the top of the editor?"
        """
        self.evaluate_task()

    def test_15(self):
        """
        Can you help me open the find and replace interface in my current editor?
        """
        self.evaluate_task()

    def test_16(self):
        """
        I need to split my active editor into right side
        """
        self.evaluate_task()

    def test_17(self):
        """
        I need to split my active editor into down side
        """
        self.evaluate_task()

    def test_18(self):
        """
        I want to change the default behavior when splitting the editor to open the new editor to the right.
        """
        self.evaluate_task()

    def test_19(self):
        """
        I want to remove all the trailing whitespace in my code.
        """
        self.evaluate_task()
    
    def test_20(self):
        """
        I need to replace all instances of the word 'apple' with 'orange' in my project files.
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
