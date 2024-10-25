from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestView(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Command/View.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        I want to open the command list.
        """
        self.evaluate_task()
