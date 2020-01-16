# -*-coding:utf-8 -*-

import os

'''文件路径'''
# 工程路径
proj_path = os.path.dirname(os.path.dirname(__file__))
# 测试用例的sheet名称
test_file_path = os.path.join(proj_path, "TestData", "测试用例.xlsx")
# 测试case的sheet名称
test_case_sheet_name = "测试用例"
# 错误截图保存路径
fail_picture_path = os.path.join(proj_path, "Report", "CapturePics", "fail")
# 成功截图保存路径
success_picture_path = os.path.join(proj_path, "Report", "CapturePics", "pass")
# 测试log所在的路径
log_file_path = os.path.join(proj_path, "Report", "Log")
# 测试报告所在的路径
test_report_path = os.path.join(proj_path, "Report")
# 日志配置文件路径
conf_path = os.path.join(proj_path, "Config", "Logger.conf")
# 邮件配置文件路径
mail_file_conf_path = os.path.join(proj_path, "TestData", "MailReceiver.ini")
# ini文件路径
object_map_file_path = os.path.join(proj_path, "TestData", "ObjectDeposit.ini")

'''测试用例sheet中的相关列的列号'''
# 测试步骤工作表名称所在的列号
test_case_test_step_sheet_name_col_no = 3
# 是否执行列号
test_case_is_executed_col_no = 4
# 执行时间列号
test_case_executed_time_col_no = 5
# 执行结果列号
test_case_executed_result_col_no = 6

'''测试步骤sheet中的相关列的列号'''
# action列号
test_step_action_col_no = 2
# 定位方式列号
test_step_locate_type_col_no = 3
# 定位表达式列号
test_step_locate_expression_col_no = 4
# 操作值列号
test_step_value_col_no = 5
# 执行时间列号
test_step_executed_time_col_no = 6
# 执行结果列号
test_step_executed_result_col_no = 7
# 异常信息列号
test_step_executed_exception_info_col_no = 8
# 异常信息图片存储路径列号
test_step_executed_capture_pic_path_col_no = 9

'''浏览器驱动所在的路径'''
# ie浏览器驱动所在路径
ie_driver = "d:\\IEDriverServer"
# chrome浏览器驱动所在路径
chrome_driver = "d:\\chromedriver"
# firefox浏览器驱动所在路径
firefox_driver = "d:\\geckodriver"
# 浏览器名称
browser = 'chrome'


if __name__ == "__main__":
    print(proj_path)
    print(test_file_path)
    print(log_file_path)
