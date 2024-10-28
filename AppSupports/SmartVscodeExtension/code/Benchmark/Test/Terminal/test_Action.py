import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestTerminalAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Terminal/Action.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to enable the feature that automatically copies the text when I select it in the terminal.
        """
        self.evaluate_task()

    def test_2(self):
        """
        Open a new terminal.
        """
        self.evaluate_task()

    def test_3(self):
        """
        I want the terminal to open in the '/home/myproject' directory instead of the default one.
        """
        self.evaluate_task()

    def test_4(self):
        """
        I need to execute the current file I'm working on in the terminal.
        """
        self.evaluate_task()

    def test_5(self):
        """
        I want to enable the warning when I paste multiple lines in the terminal.
        """
        self.evaluate_task()

    def test_6(self):
        """
        I want to enable the bracketed paste mode in the terminal, can you help me with that?
        """
        self.evaluate_task()

    def test_7(self):
        """
        I want to configure the terminal to automatically respond 'N' when asked 'Terminate batch job (Y/N)?'.
        """
        self.evaluate_task()

    def test_8(self):
        """
        I need to quickly navigate to the top of my terminal view.
        """
        self.evaluate_task()

    def test_9(self):
        """
        I want to increase the amount of scrollback kept in the terminal buffer to 2000.
        """
        self.evaluate_task()

    def test_10(self):
        """
        I need to open the find view in the terminal to search for a specific string.
        """
        self.evaluate_task()

    def test_11(self):
        """
        I want to enable the smooth scrolling feature in the terminal view.
        """
        self.evaluate_task()

    def test_12(self):
        """
        When I split the terminal, I want the new terminal to start in the same location as the original one.
        """
        self.evaluate_task()

    def test_13(self):
        """
        I'd like to avoid any prompts when I close terminals that are running tasks. Can you help me with that?
        """
        self.evaluate_task()

    def test_14(self):
        """
        I'd like to be prompted every time I try to close the window while there are still active terminal sessions. Can you make that happen?
        """
        self.evaluate_task()

    def test_15(self):
        """
        Can you help me turn on the alert for terminal process termination with non-zero exit code?
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
