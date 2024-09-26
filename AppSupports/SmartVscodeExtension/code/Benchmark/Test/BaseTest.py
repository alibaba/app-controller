import unittest
import json
import os

from AppSupports.SmartVscodeExtension.code.Benchmark.Test.TaskTestResult import TaskTestResult
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.utils import test_one_case
from Core.Common.TimeStatistic import TimeStatistic


class BaseTest(unittest.TestCase):
    def setUp(self):
        pass

    def execute(self, case):
        return test_one_case(case)

    def evaluate(self, case):
        res: TaskTestResult = self.execute(case)
        self.assertTrue(res.success, res.info)
        return res.success



class BenchmarkTest(BaseTest):
    
    def setUp(self):
        self.benchmark_data_path = 'AppSupports/SmartVscodeExtension/code/Benchmark/Data'
        self.test_data_path = None
        self.tasks = {} # id -> task
    
    def load_tasks(self, test_data_path):
        """
        Load tasks from a JSON file and map them by their IDs.

        Args:
            test_data_path (str): The path to the JSON file containing test tasks related to the benchmark data path

        Raises:
            FileNotFoundError: If the JSON file does not exist.
            json.JSONDecodeError: If the JSON file is not properly formatted.
        """
        
        self.test_data_path = os.path.join(self.benchmark_data_path, test_data_path)
        try:
            with open(self.test_data_path, 'r') as file:
                print("\nLoad tasks from", self.test_data_path)
                tasks = json.load(file)  
            for task in tasks:
                self.tasks[task['id']] = task
        except FileNotFoundError:
            self.fail(f"FileNotFoundError: The file {self.test_data_path} does not exist.")
        except json.JSONDecodeError:
            self.fail(f"JSONDecodeError: The file {self.test_data_path} is not properly formatted.")
            
    def evaluate_task(self, task_id):
        
        """
        Evaluate one test task.
        Args:
            task_id (int/str): The unique identifier of the test task to evaluate.
        
        task (dict): A dictionary representing a test task with the following structure:
            "id": <unique identifier for the test task>,
            "q": [<list of queries>],  # Each query in the list corresponds to the same answer.
            "a": [<list of answers>]   # Each answer in the list completes the same task.
        
        Example:
            Given a task dictionary with the following content:
            {
                "id": "1",
                "q": ["query1", "query2", "query3"],
                "a": [{answer1}, {answer2}]
            }
            This method will process and evaluate the following cases:
            - Case ID: 1-1, Query: query1, Answer: [{answer1}, {answer2}]
            - Case ID: 1-2, Query: query2, Answer: [{answer1}, {answer2}]
            - Case ID: 1-3, Query: query3, Answer: [{answer1}, {answer2}]
        """
        task = self.tasks.get(task_id, None)
        
        # Safety checks
        if task is None:
            self.fail(f"Task with id {task_id} not found.")
        if not isinstance(task, dict):
            self.fail("Invalid task format: Task should be a dictionary.")
        if 'id' not in task or 'q' not in task or 'a' not in task:
            self.fail("Invalid task format: Task must contain 'id', 'q', and 'a' keys.")
        if not isinstance(task['q'], list) or not isinstance(task['a'], list):
            self.fail("Invalid task format: 'q' and 'a' must be lists.")
        if not all(isinstance(q, str) for q in task['q']):
            self.fail("Invalid task format: All queries in 'q' must be strings.")
        if not all(isinstance(a, dict) for a in task['a']):
            self.fail("Invalid task format: All answers in 'a' must be dictionaries.")

        # Evaluate each query in the task
        id = task['id']
        timer = TimeStatistic()
        count = 0
        for i, q in enumerate(task['q']):
            case = {
            "id": f'{id}-{i+1}', 
            "q": q,
            "a": task['a'],
            }
            print("-------------")
            print(f'Running test case {case["id"]}')
            print("Query: ", case["q"])
            print("Answer: ", case["a"])
            timer.start(f"task_{task_id}")
            with self.subTest(case=case):
                success = self.evaluate(case)
            elapsed_time = timer.end(f"task_{task_id}")
            print(f"Response time: {float(elapsed_time):.2f} s")
            if success:
                count += 1
                
        # Summary
        print("==============")
        print(f"Summary:\nTask {id} completed. {count}/{len(task['q'])} queries passed.")
        stats = timer.get_statistics(f"task_{task_id}")
        formatted_stats = {k: f"{v:.2f} s" for k, v in stats.items()}
        print(formatted_stats)
        