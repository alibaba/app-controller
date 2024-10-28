import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestSettingAction(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Setting/Action.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to turn on Settings Sync
        """
        self.evaluate_task()

    def test_2(self):
        """
        I want to stop syncing my color theme settings in VScode.
        """
        self.evaluate_task()

    def test_3(self):
        """
        I want to stop the sync for my ms-python.python extensions.
        """
        self.evaluate_task()

    def test_4(self):
        """
        I want to change the configuration of setting sync
        """
        self.evaluate_task()

    def test_5(self):
        """
        I need to access the local backups folder on my computer.
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
