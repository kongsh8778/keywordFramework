# -*-coding:utf-8 -*-

from Utils.OtherUtils.GenTime import get_current_datetime
from Utils.FileUtils.GenTestReport import  *
from Action.SendResultAction import send_test_result
from Config.ProjVar import *

if __name__ == "__main__":
    # 第一种测试报告(可视化)
    fileName = get_current_datetime()+'.html'
    test_suite = unittest.defaultTestLoader.discover(os.path.join(proj_path, 'Scripts'), pattern='Test*.py')
    # result = BeautifulReport(test_suite, fail_picture_path)
    result = BeautifulReport(test_suite)
    result.report(filename=fileName, description='关键字驱动框架测试', log_path=test_report_path)
    fileName = os.path.join(test_report_path, fileName)

    # # 第二种测试报告
    # runner, fp, fileName = gen_test_report()
    # test_suite = unittest.defaultTestLoader.discover(\
    #     os.path.join(proj_path, 'Scripts'), pattern='Test.py')
    # runner.run(test_suite)
    # fp.close()

    # 邮件发送测试结果
    # print(fileName)
    send_test_result('测试报告', '测试通过', os.path.abspath(fileName))