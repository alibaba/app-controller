import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestTerminalProfile(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Terminal/Profile.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to set my default shell profile to bash in the terminal.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I want to set my default terminal profile to 'my-bash' instead of 'my-pwsh'
        """
        self.evaluate_task()




if __name__ == "__main__":
    unittest.main()
