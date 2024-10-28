import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestProfileAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Profile/Action.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to import a different profile for my project.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I need to change my profile.
        """
        self.evaluate_task()

    def test_3(self):
        """
        I need to create a new profile
        """
        self.evaluate_task()

    def test_4(self):
        """
        I want to export my profile.
        """
        self.evaluate_task()

    def test_5(self):
        """
        I want to delete a profile
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
