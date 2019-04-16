# -*-coding:utf-8 -*-

import unittest
from Action.WebElementAction import *
from Utils.FileUtils.Log import *
from Action.WebElementAction import capture_pic
from BeautifulReport import BeautifulReport


class KeywordDrivenUnitTest(unittest.TestCase):

    def save_img(self, img_name):
        """save_img，在测试过程中出现错误时，会调用此方法自动截图并返回失败"""
        capture_pic(img_name)

    def setUp(self):
        info('****************starting run test cases****************')

    @BeautifulReport.add_test_img(os.path.join(fail_picture_path), "test_126mail")
    def test_126mail(self):
        run_test_case(test_file_path)

    def tearDown(self):
        info('****************test case run completed****************')


if __name__ == "__main__":
    unittest.main()


