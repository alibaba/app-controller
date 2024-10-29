# 使用discover()来实现添加执行整个目录下所有的测试用例
import os
import unittest
import time
import json
import sys

# from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from XTestRunner import HTMLTestRunner
from XTestRunner.config import RunResult

# test_model = "gpt-4-turbo"
test_model = "qwen-max"

class QueryCounter:
    @staticmethod
    def count_queries_in_file(file_path):
        """Read the JSON file and count the total number of queries in the 'q' lists."""
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        q_count = 0
        for item in data:
            if 'q' in item and isinstance(item['q'], list):
                q_count += len(item['q'])
        
        return q_count

    @staticmethod
    def count_queries_in_directory(directory_path):
        """Count the number of queries in the 'q' list in all JSON files within a directory and its subdirectories."""
        total_query_count = 0
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    total_query_count += QueryCounter.count_queries_in_file(file_path)
        return total_query_count

# Todo: support skip
# support statistics of subtests
class myRunner(HTMLTestRunner):
    def __init__(self, stream=sys.stdout, verbosity=1, title=None, tester="Anonymous", description=None, rerun=0, language="en", logger=None, **kwargs):
        super().__init__(stream, verbosity, title, tester, description, rerun, language, logger, **kwargs)
        self.cases_count = kwargs.pop('cases_count', 0)
        self.subcases_count = kwargs.pop('subcases_count', 0)
    
    
    def get_report_attributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        start_time_format = str(self.start_time)[:19]
        end_time_format = str(self.end_time)[:19]
        duration = str(self.end_time - self.start_time)[:-3]

        RunResult.start_time = start_time_format
        RunResult.end_time = end_time_format
        RunResult.duration = duration
        RunResult.passed = self.subcases_count-result.failure_count-result.error_count
        RunResult.failed = result.failure_count
        RunResult.errors = result.error_count
        RunResult.skipped = result.skip_count
        all_passed = result.success_count-RunResult.passed
        
        count = RunResult.passed + RunResult.failed + RunResult.errors + RunResult.skipped
        p_percent = '0.00'
        e_percent = '0.00'
        f_percent = '0.00'
        s_percent = '0.00'
        all_passed_rate = '0.00'
        if count > 0:
            p_percent = '{:.2%}'.format(RunResult.passed / count)
            e_percent = '{:.2%}'.format(RunResult.errors / count)
            f_percent = '{:.2%}'.format(RunResult.failed / count)
            s_percent = '{:.2%}'.format(RunResult.skipped / count)
            all_passed_rate = '{:.2%}'.format(all_passed / self.cases_count) 

        RunResult.count = count
        RunResult.pass_rate = p_percent
        RunResult.error_rate = e_percent
        RunResult.failure_rate = f_percent
        RunResult.skip_rate = s_percent

        base_info = {
            "start_time": start_time_format,
            "end_time": end_time_format,
            "duration": duration
        }

        statistics_info = {
            "p": {
                "number": RunResult.passed,
                "percent": p_percent
            },
            "e": {
                "number": RunResult.errors,
                "percent": e_percent
            },
            "f": {
                "number": RunResult.failed,
                "percent": f_percent
            },
            "s": {
                "number": all_passed,
                "percent": all_passed_rate
            },
        }

        return base_info, statistics_info
        
        

# 获取当前路径
case_path = os.path.dirname(__file__)
# case_path = os.path.join(case_path, "Accessibility")

# 匹配测试用例路径下的所有的测试方法
discover = unittest.defaultTestLoader.discover(start_dir=case_path,  # 用例路径
                                               pattern="test_*.py",
                                               top_level_dir=os.getcwd())   
# 创建主套件
main_suite = unittest.TestSuite()
# 把测试用例路径添加到主套件中
main_suite.addTest(discover)
# 执行主套件里的测试用例；如果要生成测试报告，则不通过unittest.main()方法执行
# unittest.main(defaultTest="main_suite",verbosity=2)
cases_count =  main_suite.countTestCases()
print("Count of test cases: ", cases_count)

directory_path = os.path.join(os.path.dirname(case_path), "Data")
subcases_count = QueryCounter.count_queries_in_directory(directory_path)
print("Count of sub test cases: ", subcases_count)

# 执行并生成测试报告
# 加个时间戳
now = time.strftime("%y-%m_%d_%H_%M_%S_",time.localtime(time.time()))
# 创建html类型测试报告对象，将执行的过程写入到file_obj中
file_path = "AppSupports/SmartVscodeExtension/code/Benchmark/Test/test_report"
os.makedirs(file_path,exist_ok=True)
file_path = os.path.join(file_path,"{}test_report.html".format(now))

# 创建配置html测试报告的
# 相关信息的对象
with open(file_path, "wb") as file_obj:
    # runner = HTMLTestRunner(stream=file_obj, title="AppController-Test",
    #                                    description=f"Test the {cases_count} cases and {subcases_count} subcases in VSCode Benchmark\n the statics are the subtests and the 'skipped' is the item of all cases passed",
    #                                    tester="gpt-4-turbo"
    #                                    )
    
    # myRunner 
    runner = myRunner(stream=file_obj, title="AppController-Test",
                                       description=f"Test the {cases_count} cases (APIs) and {subcases_count} subcases (QA) in VSCode Benchmark\n the statics are the subtests and the 'skipped' is the item of all cases passed",
                                       tester=test_model, cases_count=cases_count, subcases_count=subcases_count
                                       )
    # # 生成html测试报告；如果要生成测试报告，则不通过unittest.main()方法执行
    runner.run(main_suite)
    
    # unittest.main(defaultTest="main_suite", testRunner=runner)
