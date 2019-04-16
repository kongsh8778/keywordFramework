# -*-coding:utf-8 -*-

import time


def get_current_date():
    """生成日期字符串，格式为xxxx年xx月xx日"""
    time_tuple = time.localtime()
    current_date = "{0}年{1}月{2}日".format(str(time_tuple.tm_year),str(time_tuple.tm_mon), str(time_tuple.tm_mday))

    return current_date


def get_current_time():
    """生成时间字符串，格式为xx时xx分xx秒"""
    time_tuple = time.localtime()
    current_time = "{0}时{1}分{2}秒".format(str(time_tuple.tm_hour), str(time_tuple.tm_min), str(time_tuple.tm_sec))
    return current_time


def get_current_datetime():
    """生成日期+日期字符串，格式为xxxx年xx月xx日 xx时xx分xx秒"""
    return get_current_date() + " " + get_current_time()


if __name__ == "__main__":
    print(get_current_date())
    print(get_current_datetime())
    print(get_current_time())
