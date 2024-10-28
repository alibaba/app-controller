import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestTerminalCursor(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Terminal/Cursor.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to change the cursor style in the terminal to a line.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I want to adjust the cursor width in the terminal to 3 pixels when the cursor style is set to line.
        """
        self.evaluate_task()

    def test_3(self):
        """
        I want the cursor to blink when the terminal is focused, can you help me set that up?
        """
        self.evaluate_task()

    def test_4(self):
        """
        I want to change the style of the terminal cursor when it's not focused to 'block'.
        """
        self.evaluate_task()




if __name__ == "__main__":
    unittest.main()
