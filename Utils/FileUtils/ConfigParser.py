# -*-coding:utf-8 -*-

import configparser
import traceback


class ConfigParser(object):
    """解析ini文件的类"""
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        # 实例化ConfigParser
        self.cf = configparser.ConfigParser()
        # 读取指定的ini文件
        self.cf.read(self.config_file_path, encoding="utf-8-sig")

    def get_all_sections(self):
        """获取所有的section，也就是用[]中的内容"""
        return self.cf.sections()

    def get_option(self, section_name, option_name):
        """获取所有的section，也就是用[]中的内容"""
        try:
            value = self.cf.get(section_name, option_name)
            return value
        except configparser.NoSectionError:
            traceback.print_exc()
            # raise configparser.NoSectionError("section或action不存在！")
        except Exception:
            traceback.print_exc()
            # raise Exception("get_option失败！")

    def get_all_option_items(self, section_name):
        """获取section下所有的option,以字典的形式返回"""
        try:
            items = self.cf.items(section_name)
            return dict(items)
        except configparser.NoSectionError:
            traceback.print_exc()
            # raise configparser.NoSectionError("section不存在！")
        except Exception:
            traceback.print_exc()
            # raise Exception("get_all_option_items失败！")


if __name__ == "__main__":
    from Config.ProjVar import object_map_file_path
    cf = ConfigParser(object_map_file_path)
    print(cf.get_all_sections())
    print(cf.get_option('baidu', "SearchPage.InputBox"))
    # print(cf.get_option('bing', "SearchPage.InputBox"))
    print(cf.get_all_option_items('baidu'))
