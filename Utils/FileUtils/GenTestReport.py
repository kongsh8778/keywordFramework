# -*-coding:utf-8 -*-

import time
import unittest
from Utils.FileUtils.Log import info,error
from Utils.FileUtils import HTMLTestRunner
from Config.ProjVar import *
from BeautifulReport import BeautifulReport


def gen_test_report():
    """用HTMLTestRunner 实现的测试报告"""
    curr_time = time.strftime('%Y-%m-%d %H_%M_%S')
    file_name = test_report_path + r'\report' + curr_time + '.html'
    try:
        fp = open(file_name, 'wb')
    except Exception :
        error('[%s] open error cause Failed to generate test report' % file_name)
    else:
        runner = HTMLTestRunner.HTMLTestRunner(\
            stream=fp, title='关键字驱动测试报告', description='处理器:Intel(R) Core(TM) '
                                                           'i5-6200U CPU @ 2030GHz 2.40 GHz '
                                                '内存:8G 系统类型: 64位 版本: windows 10 家庭中文版')
        info('successed to generate test report [%s]' %file_name)
        return runner, fp, file_name


def add_test_case(test_case_path=log_file_path, rule='test*.py'):
    """
    :param test_case_path: 测试用例存放路径
    :param rule: 匹配的测试用例文件
    :return:  测试套件
    """
    discover = unittest.defaultTestLoader.discover(test_case_path, rule)

    return discover


def run_test_case(discover):
    """用BeautifulReport模块实现测试报告"""
    curr_time = time.strftime('%Y-%m-%d %H_%M_%S')
    file_name = curr_time+'.html'
    try:
        result = BeautifulReport(discover)
        result.report(filename=file_name, description='测试报告', log_path=log_file_path)
    except Exception:
        error('Failed to generate test report', exc_info=True)
    else:
        info('successed to generate test report [%s]' % file_name)
        return file_name


if __name__ == '__main__':
    gen_test_report()
    suite = add_test_case()
    run_test_case(suite)
