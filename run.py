import os
import time
import unittest

# from common.HTMLTestReportCN import HTMLTestRunner
from common.HtmlTestRunner import HTMLTestReportEN

#测试报告的存放路径

report_path = './report/'
#测试报告的标题
report_title= '冒烟测试'
#测试的描述
report_desc = '本次测试是对于加减法功能的测试'

if not os.path.exists(report_path):
    os.mkdir(report_path)

#测试报告的命名
report_name = time.strftime("%Y%m%d%H%M%S")

#构建测试报告存放路径和名字
file_path = report_path+report_name+'.html'


#执行测试，生成报告
case_path = './test_case'

#模糊匹配
suite = unittest.defaultTestLoader.discover(start_dir=case_path,pattern="C*.py")

with open(file_path,'wb')as report:
    #使用HTMLTestRunner
    #第一个参数指的是生成的测试报告给哪个文件写入
    runner = HTMLTestReportEN(report,title=report_title,description=report_desc)

    #执行测试套件
    runner.run(suite)

