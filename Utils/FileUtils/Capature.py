# -*-coding:utf-8 -*-

from PIL import ImageGrab
from Utils.FileUtils.Dir import make_date_dir
import traceback
from Config.ProjVar import *
from Utils.FileUtils.Log import *


def capture_all_screen(picture_file_name):
    """截取整个电脑屏幕"""
    try:
        # 默认为成功的截图信息的存储路径
        picture_path = success_picture_path
        # 如果传入的图片名中指定了fail文件夹，图片存储路径修改为fail_picture_path
        if 'fail' == os.path.split(picture_file_name)[0][-4:]:
            picture_path = fail_picture_path
        # 创建当前日期目录
        current_date = make_date_dir(picture_path)
        # 拼接完整的图片名称，格式为：picture_path\\current_date\\picture_file_name
        all_pic_file_path = os.path.join(picture_path, current_date, os.path.split(picture_file_name)[-1])
        # 保存图片
        im = ImageGrab.grab()
        im.save(all_pic_file_path, "png")
        return all_pic_file_path
    except Exception as e:
        traceback.print_exc()
        info("截屏失败,错误信息为%s" % traceback.format_exc())
        raise Exception("截屏失败！")


def capture_browser_screen(driver, picture_file_name):
    """截取浏览器屏幕"""
    try:
        # 默认为成功的截图信息的存储路径
        picture_path = success_picture_path
        # 如果传入的图片名中指定了fail文件夹，图片存储路径修改为fail_picture_path
        if 'fail' == os.path.split(picture_file_name)[0][-4:]:
            picture_path = fail_picture_path
        # 创建当前日期目录
        current_date = make_date_dir(picture_path)
        # 拼接完整的图片名称，格式为：picture_path\\current_date\\picture_file_name
        all_pic_file_path = os.path.join(picture_path, current_date, os.path.split(picture_file_name)[-1])
        # 保存图片
        driver.get_screenshot_as_file(all_pic_file_path)
        return all_pic_file_path
    except Exception as e:
        traceback.print_exc()
        info("截屏失败,错误信息为%s" % traceback.format_exc())
        raise Exception("截屏失败！")


if __name__ == "__main__":
    from Action.WebElementAction import *
    open_browser('chrome')
    visit("http://www.baidu.com")
    # capture_browser_screen('baidu.png')
    capture_all_screen('screen.png')
    # capture_browser_screen(os.path.join(fail_picture_path, 'baidu.png'))
    capture_all_screen(os.path.join(fail_picture_path, 'screen.png'))
    quit()
