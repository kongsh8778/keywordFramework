# -*-coding:utf-8 -*-

import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtil(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.locate_method = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT
        }

    def presenceOfElement(self, locate_method, locate_expression):
        """显示等待判断元素是否存在"""
        try:
            return self.wait.until(lambda x: x.find_element(self.locate_method[locate_method],
                                                            locate_expression))
        except TimeoutException:
            traceback.print_exc()
            raise TimeoutException

    def visibleOfElement(self, locate_method, locate_expression):
        """显示等待判断元素是否可见"""
        try:
            return self.wait.until(EC.visibility_of_element_located([self.locate_method[locate_method],
                                                                     locate_expression]))
        except TimeoutException:
            traceback.print_exc()
            raise TimeoutException

    def clickbleOfElement(self, locate_method, locate_expression):
        """显示等待判断元素是否点击"""
        try:
            return self.wait.until(EC.element_to_be_clickable((self.locate_method[locate_method],
                                                               locate_expression)))
        except TimeoutException:
            traceback.print_exc()
            raise TimeoutException

    def switchToFrame(self, locate_method, locate_expression):
        """切换到指定的frame"""
        try:
            return self.wait.until(EC.frame_to_be_available_and_switch_to_it((self.locate_method[locate_method],
                                                                              locate_expression)))
        except Exception as e:
            traceback.print_exc()
            raise e

    def beSelectedOfElement(self, locate_method, locate_expression):
        """显示等待判断元素是否被选中"""
        try:
            return self.wait.until(EC.element_located_to_be_selected((self.locate_method[locate_method],
                                                                      locate_expression)))
        except TimeoutException:
            traceback.print_exc()
            raise TimeoutException


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="f:\\chromedriver")
    wait_object = WaitUtil(driver)
    driver.get("http://mail.126.com")
    try:
        wait_object.switchToFrame("xpath", "//iframe[contains(@id,'x-URS-iframe')]")
        # wait = WebDriverWait(driver, 10, 0.2)
        # wait.until(EC.frame_to_be_available_and_switch_to_it( \
        #     driver.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]")))
        import time
        time.sleep(3)
        element = driver.find_element_by_xpath('//input[@name="email"]')
        element.send_keys("xiaoxiao")
    except TimeoutException:
        print("元素未定位！")
