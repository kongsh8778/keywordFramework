# -*-coding:utf-8 -*-

from Utils.OtherUtils.GenTime import *
from Config.ProjVar import *


def make_date_dir(dir_path):
    """在dir_path下创建日期目录"""
    if os.path.exists(dir_path):
        current_date = get_current_date()
        path = os.path.join(dir_path, current_date)
        if not os.path.exists(path):
            os.mkdir(path)
        return current_date
    else:
        raise Exception("make_date_dir创建目录失败！")


def make_time_dir(dir_path):
    """在dir_path下创建时间目录"""
    if os.path.exists(dir_path):
        current_time = get_current_time()
        path = os.path.join(dir_path, current_time)
        if not os.path.exists(path):
            os.mkdir(path)
        return current_time
    else:
        raise Exception("make_time_dir创建目录失败！")


if __name__ == "__main__":
    make_date_dir(log_file_path)
    make_time_dir(log_file_path)
