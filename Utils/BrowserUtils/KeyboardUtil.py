# -*-coding:utf-8 -*-

import win32api
import win32con


class Keyboard(object):
    """模拟键盘操作类"""
    VK_CODE = {
        'enter':0x0D,
        "ctrl": 0x11,
        'a':0x41,
        'v': 0x56,
        'x': 0x58,
        'z': 0x5A,
        'tab': 0x09
    }

    @staticmethod
    def key_down(key_name):
        """按下"""
        win32api.keybd_event(Keyboard.VK_CODE[key_name], 0, 0, 0)

    @staticmethod
    def key_up(key_name):
        """抬起"""
        win32api.keybd_event(Keyboard.VK_CODE[key_name], 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def one_key(key_name):
        """单个按键的按下和抬起"""
        Keyboard.key_down(key_name)
        Keyboard.key_up(key_name)

    @staticmethod
    def two_key(key_name1, key_name2):
        """两个按键的按下和抬起"""
        Keyboard.key_down(key_name1)
        Keyboard.key_down(key_name2)
        Keyboard.key_up(key_name2)
        Keyboard.key_up(key_name1)