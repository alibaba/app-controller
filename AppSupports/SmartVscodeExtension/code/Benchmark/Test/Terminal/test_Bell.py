import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestTerminalBell(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Terminal/Bell.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to enable the visual bell in the terminal. Can you help me with that?
        """
        self.evaluate_task()

    def test_2(self):
        """
        I want the yellow bell icon to show for 2000 milliseconds when the terminal's bell is triggered.
        """
        self.evaluate_task()




if __name__ == "__main__":
    unittest.main()
