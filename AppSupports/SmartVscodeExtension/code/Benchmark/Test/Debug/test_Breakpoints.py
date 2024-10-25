import unittest
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BenchmarkTest


class TestBreakpoint(BenchmarkTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        test_data_path = 'Debug/Breakpoint.json'
        cls.load_tasks(cls, test_data_path)

    def test_1(self):
        """
        "Can you help me toggle a breakpoint on the current line of my file?",
            "I'm trying to pause the execution of my code at a specific point, can you help me do that on the current line?"
        """
        self.evaluate_task()

    def test_2(self):
        """
        "I need to add a conditional breakpoint on line 50, which should only be hit when the variable 'x' is greater than 10.",
        "I'm debugging my code and I want to pause execution on line 30, but only when a certain condition is met. Specifically, when the 'count' variable reaches 100."
        """
        self.evaluate_task()

    def test_3(self):
        """
        "I need to add a Logpoint on line 50 of my code to output some log information when the execution reaches there.",
        "I'm trying to monitor a specific line in my code without interrupting the execution. Can you help me set something up to print some messages when the program reaches that line?"
        """
        self.evaluate_task()

    def test_4(self):
        """
        "I want to set the middle mouse button click action in the editor gutter to add a Conditional Breakpoint.",
        "When I click the editor gutter with the middle mouse button, I want it to create a breakpoint that only triggers when a certain condition is met."
        """
        self.evaluate_task()

    def test_5(self):
        """
         "I want to automatically enable breakpoints when a specific breakpoint is hit in my code.",
         "I need my VScode to automatically pause execution when a certain part of my code is reached"
        """
        self.evaluate_task()

    def test_6(self):
        """
        "I want the program to stop when the hit count reaches 50."
        """
        self.evaluate_task()

    def test_7(self):
        """
        "Can you help me reapply all breakpoints in my project's source code?",
        "My debug environment seems to be misplacing breakpoints in unexpected source code. Can you help me fix this?"
        """
        self.evaluate_task()

    def test_8(self):
        """
        "I need to enable all the breakpoints in my current project."
        """
        self.evaluate_task()

    def test_9(self):
        """
        "I need to disable all the breakpoints in my current project."
        """
        self.evaluate_task()

    def test_10(self):
        """
        "I need to remove all breakpoints from my current project."
        """
        self.evaluate_task()

    def test_11(self):
        """
        "Can you help me disable the function that shows breakpoints in the editor's overview ruler?",
        "I'd like to see where I've set breakpoints directly on the side bar of my editor, can you make that happen?"
        """
        self.evaluate_task()

    def test_12(self):
        """
        "I need to see all the breakpoints in my code, can you help me with that?"
        """
        self.evaluate_task()

    def test_13(self):
        """
        "I need to add a data breakpoint for the 'count' variable in my code."
        """
        self.evaluate_task()
if __name__ == "__main__":
    unittest.main()
