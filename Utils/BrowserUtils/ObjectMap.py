# -*-coding:utf-8 -*-

from Utils.FileUtils.ConfigParser import ConfigParser
from Utils.BrowserUtils.WaitUtil import WaitUtil

class ObjectMap(object):
    """对象映射类"""
    def __init__(self, config_file_path):
        self.cf = ConfigParser(config_file_path)

    def get_locate_method_and_locate_exp(self, section_name, option_name):
        """获取定位方法和定位表达式"""
        locators = self.cf.get_option(section_name, option_name).split(">")
        return locators

    def get_element_object(self, driver, section_name, option_name):
        """由ini文件中指定的section_name和option_name，得到webElement对象"""
        try:
            # 获取定位方法和定位表达式
            locators = self.cf.get_option(section_name, option_name).split(">")
            # 根据定位方法和定位表达式，通过显示等待得到页面元素对象
            element = WaitUtil(driver).presenceOfElement(locators[0], locators[1])
        except Exception as e:
            raise e
        else:
            # 返回页面元素对象
            return element


if __name__ == '__main__':
    from selenium import webdriver
    from Config.ProjVar import object_map_file_path
    driver = webdriver.Chrome(executable_path="f:\\chromedriver")
    driver.get("http://www.baidu.com")
    objmap = ObjectMap(object_map_file_path)
    print(objmap.get_element_object(driver, "baidu", "SearchPage.InputBox"))
    print(objmap.get_element_object(driver, "baidu", "SearchPage.SubmitButton"))