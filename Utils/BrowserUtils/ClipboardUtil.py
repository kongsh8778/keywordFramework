# -*-coding:utf-8 -*-

import win32clipboard as w
import win32con


class Clipboard(object):
    """模拟windows设置和读取剪贴板"""
    @staticmethod
    def set_text(content):
        """设置剪贴板"""
        # 打开剪贴板
        w.OpenClipboard()
        # 清空剪贴板
        w.EmptyClipboard()
        # 设置指定的内容
        w.SetClipboardData(win32con.CF_UNICODETEXT, content)
        # 关闭剪贴板
        w.CloseClipboard()

    @staticmethod
    def get_text():
        """获取剪贴板中指定的内容"""
        # 打开剪贴板
        w.OpenClipboard()
        # 读取剪贴板中的内容
        content = w.GetClipboardData(win32con.CF_TEXT)
        # 关闭剪贴板
        w.CloseClipboard()
        # 返回从剪贴板获取的数据
        return content
