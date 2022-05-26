from appium import webdriver
import time
import pytest
import html
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Basic.Init_Driver import init_driver
from Basic.Base import Base
"""
用例1：拒绝权限无法进入首页
1，启动下载器
2，拒绝权限
3，退出app"
"""

class Test_case:
    # def setup_class(self):
    #     self.driver = init_driver()
    # def teardown_class(self):
    #     self.driver.quit()
    # def test_001(self):
    #     try:
    #        base_obj = Base(self.driver)
    #        base_obj.click_element((By.ID,"instasaver.instagram.video.downloader.photo:id/tvLater"))
    #     except NoSuchElementException as msg:
    #         f_name = time.strftime("%Y%m%d%H%M%S",time.localtime((time.time())))
    #         self.driver.get_screenshot_as_file('/Users/zhao/Desktop/download_errorphoto' + f_name + '.png')
    #         print(msg)

    def __init__(self):
        self.driver = init_driver()
    def test_001(self):
        try:
           base_obj = Base(self.driver)
           base_obj.click_element((By.ID,"instasaver.instagram.video.downloader.photo:id/tvLater"))
        except NoSuchElementException as msg:
            f_name = time.strftime("%Y%m%d%H%M%S",time.localtime((time.time())))
            self.driver.get_screenshot_as_file('/Users/zhao/Desktop/download_errorphoto' + f_name + '.png')
            print(msg)
        self.driver.quit()
if __name__ == '__main__':
    # pytest.main(" test_case_001.py")
    Test_case().test_001()

