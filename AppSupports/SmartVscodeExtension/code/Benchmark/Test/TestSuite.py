# 使用discover()来实现添加执行整个目录下所有的测试用例
import os
import unittest
import time

from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport

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


# 执行并生成测试报告
# 加个时间戳
now = time.strftime("%y-%m_%d_%H_%M_%S_",time.localtime(time.time()))
# 创建html类型测试报告对象，将执行的过程写入到file_obj中
# file_path = os.path.join(case_path,"test_report")
file_path = "AppSupports/SmartVscodeExtension/code/Benchmark/Test/test_report"
os.makedirs(file_path,exist_ok=True)
file_path = os.path.join(file_path,"{}test_report.html".format(now))
print(file_path)
# file_obj = open(file_path,"w+",encoding="utf-8")
# # 创建配置html测试报告的相关信息的对象
# runner = HTMLTestRunner.HTMLTestRunner(stream=file_obj, title="第一次的测试报告",
#                                        description="我是测试报告的描述信息")
# # 生成html测试报告；如果要生成测试报告，则不通过unittest.main()方法执行
# runner.run(main_suite)


runner = BeautifulReport(main_suite)
runner.report(description='beautifulreport', filename=file_path)