import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestView(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Debug/View.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        "I need to check the state of my variables while debugging. Can you open the Variables view in the Run and Debug view on the left side?",
        "I'm trying to troubleshoot my code and need to see what's happening with my variables. Can you show me where to find this information?"
        """
        self.evaluate_task()

    def test_2(self):
        """
        "I need to open the Run and Debug view for my current project."
        """
        self.evaluate_task()

    def test_3(self):
        """
        "I need to view the debug console to check the output of my code"
        """
        self.evaluate_task()

    def test_4(self):
        """
        I want to see the debug toolbar only in debug views
        """
        self.evaluate_task()

    def test_5(self):
        """
        "I don't want to see the debug toolbar at all when debugging"
        :return:
        """
        self.evaluate_task()

    def test_6(self):
        """
        "Can you help me open the Debug toolbar? I need to debug my code."
        :return:
        """
        self.evaluate_task()

    def test_7(self):
        """
        "I need to open the Debug Console REPL to debug my code."
        :return:
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
