import unittest
import os
import json
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BaseTest

class TestAccessibility(BaseTest):
    def setUp(self):
        benchmark_data_path = 'AppSupports/SmartVscodeExtension/code/Benchmark/Data'
        self.benchmark_data_path = os.path.join(benchmark_data_path, 'Accessibility')
    def test_Accessibility_Help(self):
        self._test_cases('Help.json')
        
    def _test_cases(self, test_data_path):
        """
        Processes test cases from a given JSON file and evaluates them.
        Args:
            test_data_path (str): The path to the JSON file containing test cases related to the benchmark data path.
        The JSON file should contain a list of objects, each representing a test task with the following structure:
        {
            "id": <unique identifier for the test task>,
            "q": [<list of queries>], each query in the list correspond to the same answer.
            "a": [<list of queries>], each answer in the list finish the same task.
        }
        For each given JSON file, this method will:
        1. Load the JSON data from the file.
        2. Iterate through each test task object.
        3. For each query in the test task, create a new case dictionary with a unique id, query, and expected answer.
        4. Print the test case details.
        5. Evaluate the test case using the `evaluate` method.
        Example:
            Given a JSON file with the following content:
            [
                {
                    "id": "1",
                    "q": ["query1", "query2", "query3"],
                    "a": [{answer1}, {answer2}]
                }
            ]
            This method will process and evaluate the following cases:
            - Case ID: 1-1, Query: query1, Answer: [{answer1}, {answer2}]
            - Case ID: 1-2, Query: query2, Answer: [{answer1}, {answer2}]
            - Case ID: 1-3, Query: query3, Answer: [{answer1}, {answer2}]
        """
        test_data_path = os.path.join(self.benchmark_data_path, test_data_path)
        with open(test_data_path, 'r') as file:
            tasks = json.load(file)  
            
        for task in tasks:
            id = task['id']
            for i, q in enumerate(task['q']):
                case = {
                    "id": f'{id}-{i+1}', 
                    "q": q,
                    "a": task['a'],
                }
                print("\n-------------")
                print(f'Running test case {case["id"]} in {test_data_path}')
                print("Query: ", case["q"])
                print("Answer: ", case["a"])
                self.evaluate(case) 

if __name__ == "__main__":
    unittest.main()