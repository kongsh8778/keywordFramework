# -*-coding:utf-8 -*-

import traceback
from Utils.BrowserUtils.ObjectMap import ObjectMap
from Utils.BrowserUtils.WaitUtil import WaitUtil
from Utils.FileUtils.Capature import *
from Action.TestCaseFileParser import TestCaseFileParser
from Utils.OtherUtils.GenTime import *
from selenium import webdriver
from Config.ProjVar import *
from Utils.BrowserUtils.KeyboardUtil import *
from Utils.BrowserUtils.ClipboardUtil import *
from Utils.FileUtils.Log import *

driver = None


def open_browser(browser):
    """启动指定的浏览器"""
    global driver
    if browser.strip().lower() == "ie":
        driver = webdriver.Ie(executable_path=ie_driver)
    elif browser.strip().lower() == "chrome":
        driver = webdriver.Chrome(executable_path=chrome_driver)
    else:
        driver = webdriver.Firefox(executable_path=firefox_driver)


def visit(url):
    """访问指定的url"""
    global driver
    try:
        driver.get(url)
        driver.maximize_window()
    except:
        info("%s can't be visited!" % url)
        raise Exception("网址%s无法访问" % url)


def input(locate_method, locate_expression, value):
    """定位到元素后输入指定的内容"""
    global driver
    try:
        element = WaitUtil(driver).visibleOfElement(locate_method, locate_expression)
        element.clear()
        element.send_keys(value)
    except:
        print("输入%s内容时出现了异常"% value)
        info("element:%s->%s operate fail" % (locate_method, locate_expression))
        raise Exception("输入%s内容时出现了异常" % value)


def sleep(duration):
    """sleep"""
    time.sleep(int(duration))


def click(locate_method, locate_expression):
    """单击元素"""
    global driver
    try:
        element = WaitUtil(driver).clickbleOfElement(locate_method, locate_expression)
        element.click()
    except:
        print("单击元素时出现了异常")
        info("element:%s->%s operate fail" % (locate_method, locate_expression))
        raise Exception("单击元素时出现了异常")


def assert_visible_of_element(locate_method, locate_expression):
    """显示等待判断指定的元素可见"""
    global driver
    try:
        WaitUtil(driver).visibleOfElement(locate_method, locate_expression)
    except:
        print("断言的元素不可见")
        info("element:%s->%s assert visible fail" % (locate_method, locate_expression))
        raise Exception("断言的元素不可见")


def assert_word(content):
    """断言"""
    global driver
    assert content in driver.page_source


def switch_frame(locate_method, locate_expression):
    """切换到指定的frame"""
    global driver
    try:
        WaitUtil(driver).switchToFrame(locate_method, locate_expression)
    except:
        print("切换frame失败")
        info("element:%s->%s switch to it fail" % (locate_method, locate_expression))
        raise Exception("切换frame失败")


def switch_to_default_frame():
    """切换回默认的frame"""
    global driver
    driver.switch_to.default_content()


def capture_pic(pic_file_name):
    """截图"""
    global driver
    return capture_browser_screen(driver, pic_file_name)


def add_attachment(locate_method, locate_expression, file_path):
    """上传附件"""
    global driver
    try:
        element = WaitUtil(driver).visibleOfElement(locate_method, locate_expression)
        Clipboard.set_text(file_path)
        Keyboard.two_key('ctrl', 'v')
        time.sleep(8)
        Keyboard.one_key('enter')
    except:
        print("上传%s时出现了异常" % file_path)
        info("element:%s->%s operate fail" % (locate_method, locate_expression))
        raise Exception("上传%s内容时出现了异常" % file_path)


def quit():
    """关闭浏览器"""
    global driver
    driver.quit()


def run_test_case(test_file):
    # 清除excel中已有测试结果
    test_file_parser = TestCaseFileParser(test_file, test_case_sheet_name)
    test_file_parser.clear_all_executed_info()
    # 获取测试用例的excel文件对象
    test_file_wb = test_file_parser.get_excel_file_obj()
    # 获取所有要执行的测试sheet名称，以及在测试用例sheet中的行号
    execute_sheet_names_dict = test_file_parser.get_execute_sheet_names()
    for sheet_name, row_no in execute_sheet_names_dict.items():
        print("#******************%s测试开始******************" % sheet_name)
        # 保存执行成功的case个数，用来判断是否所有步骤都执行成功
        successful_case_num = 0
        # 切换到sheet_name指定的sheet中
        test_file_wb.set_sheet_by_name(sheet_name)
        # 遍历测试步骤中所有的行,从2开始，忽略标题行
        for i in range(2, test_file_wb.get_max_row()+1):
            # 获取动作
            action = test_file_wb.get_cell_value(i, test_step_action_col_no)
            # 获取定位方法
            locate_method = test_file_wb.get_cell_value(i, test_step_locate_type_col_no)
            # 获取定位表达式
            locate_expression = test_file_wb.get_cell_value(i, test_step_locate_expression_col_no)
            # 获取操作值
            value = test_file_wb.get_cell_value(i, test_step_value_col_no)
            # 如果操作值以$开头和结尾，说明该测试sheet与某一个sheet关联，需要先执行关联的用例
            if isinstance(value, str) and value.strip().startswith('$') and value.strip().endswith('$'):
                # print(test_file, value.strip()[1:-1])
                run_test_unit(test_file, value.strip()[1:-1])
                # 默认此case执行成功，否则最后统计总的结果会不等于最大行数-1
                successful_case_num += 1
                continue
            # 如果操作值中包含||,代表自定义的关键字，按||切割得到测试文件名和测试sheet名
            if isinstance(value, str) and "||" in value:
                file_name, sheet_name = value.strip().split("||")
                print(file_name, sheet_name)
                run_test_unit(file_name, sheet_name)
                successful_case_num += 1
                continue
            # 如果定位方式和定位表达式没有直接写在excel中，而且通过objectMap映射的话需要特殊处理
            if locate_expression and "Page." in locate_expression:
                locate_method, locate_expression = ObjectMap(object_map_file_path).get_locate_method_and_locate_exp(\
                    locate_method.strip(), locate_expression.strip())


            # print(action, locate_method, locate_expression, value)
            # 将动作，定位方法，定位表达式,操作值拼接成WebElementAction文件中对应函数的调用
            # 没有参数的情况
            if action is not None and locate_method is None and locate_expression \
                is None and value is None:
                command = "%s()" % action
            # 只有操作值的情况
            elif action is not None and locate_method is None and locate_expression \
                is None and value is not None:
                command = "%s('%s')" % (action, value)
            # 有定位方法和定位表达式的情况
            elif action is not None and locate_method is not None and locate_expression \
                     is not None and value is None:
                command = "%s('%s','%s')" % (action, locate_method, locate_expression)
            # 有定位方法、定位表达式和操作值的情况
            elif action is not None and locate_method is not None and locate_expression \
                     is not None and value is not None:
                command = "%s('%s','%s','%s')" % (action, locate_method, locate_expression, value)

            print(command)
            # 执行拼接好的命令command
            try:
                eval(command)
            except Exception as e:
                error("测试用例：%s执行失败，错误信息为：%s" % (action, str(traceback.format_exc())))
                # 在测试步骤工作表中写入执行时间
                test_file_wb.write_cell_datetime(i, test_step_executed_time_col_no)
                # 在测试步骤工作表中写入执行结果
                test_file_wb.write_cell(i, test_step_executed_result_col_no, "fail")
                # 在测试步骤工作表中写入异常信息
                test_file_wb.write_cell(i, test_step_executed_exception_info_col_no, traceback.format_exc())
                # 在测试步骤工作表中写入异常信息截图位置
                picture_file = os.path.join(fail_picture_path, action+get_current_time()+".png")
                picture_file = capture_pic(picture_file)
                test_file_wb.write_cell(i, test_step_executed_capture_pic_path_col_no, picture_file)

            else:
                #info("测试用例：%s执行成功" % action)
                # 在测试步骤工作表中写入执行时间
                test_file_wb.write_cell_datetime(i, test_step_executed_time_col_no)
                # 在测试步骤工作表中写入执行结果
                test_file_wb.write_cell(i, test_step_executed_result_col_no, "pass")
                # 在测试步骤工作表中写入异常信息
                successful_case_num += 1

        # 切换到test_case_sheet_name中，写入整体的测试结果
        result = "pass"
        # print('========', successful_case_num, test_file_wb.get_max_row()-1)
        if successful_case_num != test_file_wb.get_max_row()-1:
            result = "fail"
        test_file_wb.set_sheet_by_name(test_case_sheet_name)
        # 在测试用例工作表中写入执行日期和时间
        test_file_wb.write_cell_datetime(row_no, test_case_executed_time_col_no)
        # 在测试用例工作表中写入测试执行结果
        test_file_wb.write_cell(row_no, test_case_executed_result_col_no, result)
        print("Done!!")


def run_test_unit(test_file_name, test_sheet_name):
    """执行指定的测试单元"""
    # 清除excel中已有测试结果
    test_file_parser = TestCaseFileParser(test_file_name, test_sheet_name)
    test_file_parser.clear_test_case_result()
    # 获取测试用例的excel文件对象
    test_file_wb = test_file_parser.get_excel_file_obj()

    # 遍历测试步骤中所有的行,从2开始，忽略标题行
    for i in range(2, test_file_wb.get_max_row()+1):
        # 获取动作
        action = test_file_wb.get_cell_value(i, test_step_action_col_no)
        # 获取定位方法
        locate_method = test_file_wb.get_cell_value(i, test_step_locate_type_col_no)
        # 获取定位表达式
        locate_expression = test_file_wb.get_cell_value(i, test_step_locate_expression_col_no)
        # 获取操作值
        value = test_file_wb.get_cell_value(i, test_step_value_col_no)
        # 如果定位方式和定位表达式没有直接写在excel中，而且通过objectMap映射的话需要特殊处理
        if locate_expression and "Page." in locate_expression:
            locate_method, locate_expression = ObjectMap(object_map_file_path).get_locate_method_and_locate_exp(\
                locate_method.strip(), locate_expression.strip())
        # print(action, locate_method, locate_expression, value)
        # 将动作，定位方法，定位表达式,操作值拼接成WebElementAction文件中对应函数的调用
        # 没有参数的情况
        if action is not None and locate_method is None and locate_expression \
            is None and value is None:
            command = "%s()" % action
        # 只有操作值的情况
        elif action is not None and locate_method is None and locate_expression \
            is None and value is not None:
            command = "%s('%s')" % (action, value)
        # 有定位方法和定位表达式的情况
        elif action is not None and locate_method is not None and locate_expression \
                 is not None and value is None:
            command = "%s('%s','%s')" % (action, locate_method, locate_expression)
        # 有定位方法、定位表达式和操作值的情况
        elif action is not None and locate_method is not None and locate_expression \
                 is not None and value is not None:
            command = "%s('%s','%s','%s')" % (action, locate_method, locate_expression, value)

        print(command)
        # 执行拼接好的命令command
        try:
            eval(command)
        except Exception as e:
            info("测试用例：%s执行失败，错误信息为：%s" % (action, str(traceback.format_exc())))
            # 在测试步骤工作表中写入执行时间
            test_file_wb.write_cell_datetime(i, test_step_executed_time_col_no)
            # 在测试步骤工作表中写入执行结果
            test_file_wb.write_cell(i, test_step_executed_result_col_no, "fail")
            # 在测试步骤工作表中写入异常信息
            test_file_wb.write_cell(i, test_step_executed_exception_info_col_no, traceback.format_exc())
            # 在测试步骤工作表中写入异常信息截图位置
            picture_file = os.path.join(fail_picture_path, action + get_current_time() + ".png")
            picture_file = capture_pic(picture_file)
            test_file_wb.write_cell(i, test_step_executed_capture_pic_path_col_no, picture_file)

        else:
            #info("测试用例：%s执行成功" % action)
            # 在测试步骤工作表中写入执行时间
            test_file_wb.write_cell_datetime(i, test_step_executed_time_col_no)
            # 在测试步骤工作表中写入执行结果
            test_file_wb.write_cell(i, test_step_executed_result_col_no, "pass")
    print("Done!!")


if __name__ == "__main__":
    try:
        open_browser('chrome')
        visit("http://www.sogou.com")
        add_attachment("id", "query", "陈伟霆")
        # input("id", "query", "陈伟霆")
        # click('xpath','//*[@id="stb"]')
        sleep(3)
        assert_word("陈伟霆")
    except Exception as e:
        print("测试执行失败")
        traceback.print_exc()
    finally:
        quit()
    # run_test_case(test_file_path)
