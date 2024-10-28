import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestTerminalTab(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Terminal/Tab.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want the terminal tabs view to never hide, regardless of how many terminals or terminal groups are open.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I'd like to have the terminal tabs shown on the left side of the terminal.
        """
        self.evaluate_task()

    def test_3(self):
        """
        I want the terminal tab title to display the current working directory instead of the process name.
        """
        self.evaluate_task()

    def test_4(self):
        """
        I want to disable the animation that appears on the right of the terminal tab.
        """
        self.evaluate_task()




if __name__ == "__main__":
    unittest.main()
