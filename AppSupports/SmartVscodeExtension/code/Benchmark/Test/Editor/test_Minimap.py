import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestMinimap(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Editor/Minimap.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to move the minimap to the left side of the screen.
        """
        self.evaluate_task()

    def test_2(self):
        """
        I want to disable the minimap in my editor.
        """
        self.evaluate_task()


if __name__ == "__main__":
    unittest.main()
