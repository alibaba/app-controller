import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestTerminalTheme(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Terminal/Theme.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I need to enlarge the terminal panel to full screen for better visibility.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I want to change the default location of the terminal to the editor area.
        """
        self.evaluate_task()

    def test_3(self):
        """
        Can you adjust the terminal columns to match the longest line in the terminal?
        """
        self.evaluate_task()

    def test_4(self):
        """
        I need to set the terminal dimensions to 80 columns and 24 rows.
        """
        self.evaluate_task()

    def test_5(self):
        """
        Can you make it so that I only see the command status indicators on the left side of the terminal?
        """
        self.evaluate_task()

    def test_6(self):
        """
        I want to enable the sticky scroll feature in the terminal so that I can easily see the command that the output belongs to.
        """
        self.evaluate_task()

    def test_7(self):
        """
        I want to change the font family of the terminal to 'Courier New'.
        """
        self.evaluate_task()

    def test_8(self):
        """
        I'd like to adjust the font size in the terminal to 14 pixels.
        """
        self.evaluate_task()

    def test_9(self):
        """
        I'd like to increase the spacing between characters in the terminal to 2 pixels.
        """
        self.evaluate_task()

    def test_10(self):
        """
        I want to increase the vertical spacing between characters in my terminal. Let's make it 20% more than the regular line height.
        """
        self.evaluate_task()

    def test_11(self):
        """
        I want to change the font weight of the normal text in the terminal to 'bold'.
        """
        self.evaluate_task()

    def test_12(self):
        """
        I want to always see the terminal's actions in the view header, can you set it up for me?
        """
        self.evaluate_task()

    def test_13(self):
        """
        I want to change the text color of my terminal to green.
        """
        self.evaluate_task()

    def test_14(self):
        """
        I want to set the terminal to always use the bright ANSI color variant for bold text.
        """
        self.evaluate_task()

    def test_15(self):
        """
        I need to switch to a different command line interface, specifically PowerShell.
        """
        self.evaluate_task()

    def test_16(self):
        """
        Can you show me my recent terminal commands?
        """
        self.evaluate_task()

    def test_17(self):
        """
        I don't want to see the terminal when I open VScode, regardless of whether there are any ongoing sessions.
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
