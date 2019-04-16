# -*-coding:utf-8 -*-

from Utils.FileUtils.Excel import *
from Config.ProjVar import *


class TestCaseFileParser(object):
    """测试文件解析类"""
    def __init__(self, test_data_file, test_sheet_name):
        # 根据指定的文件名获取excel对象
        self.test_data_wb = ParseExcel(test_data_file)
        self.test_data_wb.set_sheet_by_name(test_sheet_name)

    def get_excel_file_obj(self):
        return self.test_data_wb

    def get_execute_sheet_names(self):
        """从测试用例sheet中获取所有要执行的sheet名称,以字典形式返回"""
        # 要执行的sheet名称为key，在测试用例sheet中行号为value,方便后续写测试结果使用
        execute_sheet_names_dict = {}
        # 在测试用例工作表中找到"是否执行"这一整列
        is_execute_col = self.test_data_wb.get_col(test_case_is_executed_col_no)
        # 忽略表头所在的行，所以行索引从2开始
        # 将值为y的单元格所对应的测试步骤工作表名取出来，添加到execute_sheet_names_list中
        for row_no, cell in enumerate(is_execute_col[1:], start=2):
            if cell.value and cell.value.strip().lower() == "y":
                # print(row_no, cell,cell.value)
                execute_sheet_names_dict[self.test_data_wb.get_cell_value(
                    row_no, test_case_test_step_sheet_name_col_no)] = row_no

        # 将execute_sheet_names_dict返回
        return execute_sheet_names_dict

    def clear_test_case_result(self):
        """清除测试用例sheet中测试结果和执行时间单元格内容"""
        try:
            # 获取所有要执行的测试sheet名称，以及在测试用例sheet中的行号
            execute_sheet_names_dict = self.get_execute_sheet_names()
            # print(execute_sheet_names_dict)
            for sheet_name, row_no in execute_sheet_names_dict.items():
                self.test_data_wb.write_cell(row_no=row_no, col_no=test_case_executed_time_col_no, value="")
                self.test_data_wb.write_cell(row_no=row_no, col_no=test_case_executed_result_col_no, value="")
        except:
            traceback.format_exc()
            return False
        else:
            return True

    def clear_test_step_result(self):
        """清除测试步骤sheet中，测试结果、执行时间，异常信息和错误截图单元格内容"""
        try:
            # 保存切换前的sheet名称
            default_sheet_name = self.test_data_wb.get_current_sheet_name()
            # 获取所有要执行的测试sheet名称，以及在测试用例sheet中的行号
            execute_sheet_names_dict = self.get_execute_sheet_names()
            for sheet_name, row_no in execute_sheet_names_dict.items():
                # 切换sheet
                self.test_data_wb.set_sheet_by_name(sheet_name)
                # 遍历所有的行，忽略表头所在的行，所以索引从2开始
                for line in range(2, self.test_data_wb.get_max_row()+1):
                    # 清除"执行时间"内容
                    self.test_data_wb.write_cell(row_no=line, col_no=test_step_executed_time_col_no, value="")
                    # 清除"测试结果"内容
                    self.test_data_wb.write_cell(row_no=line, col_no=test_step_executed_result_col_no, value="")
                    # 清除"异常信息"内容
                    self.test_data_wb.write_cell(row_no=line, col_no=test_step_executed_exception_info_col_no, value="")
                    # 清除"截图位置"内容
                    self.test_data_wb.write_cell(row_no=line, col_no=test_step_executed_capture_pic_path_col_no, value="")
        except:
            traceback.format_exc()
            return False
        else:
            return True
        finally:
            # 切换回初始的sheet
            self.test_data_wb.set_sheet_by_name(default_sheet_name)

    def clear_all_executed_info(self):
        """清除测试用例和测试步骤中执行过的信息"""
        result1 = self.clear_test_case_result()
        result2 = self.clear_test_step_result()
        if result1 and result2:
            return True
        else:
            return False


if __name__ == "__main__":
    fp = TestCaseFileParser(test_file_path, test_case_sheet_name)
    print(fp.get_execute_sheet_names())
    print(fp.clear_all_executed_info())
    print(fp.get_execute_sheet_names())
    # print(fp.clear_test_case_result())
    # print(fp.clear_test_step_result())

