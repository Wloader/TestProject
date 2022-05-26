import time
import pytest
from selenium.webdriver.common.by import By
from Basic.Base import Base
from selenium.common.exceptions import NoSuchElementException
from Basic.Init_Driver import init_driver

"""
用例3：用户未登录下载文件
1，用户进入首页
2，输入ins链接下载
3，判断是否下载成功
4，用户退出
"""

class Test_case:
    def __init__(self):
        self.driver = init_driver()
    def case_003(self):
        try:
            base_obj = Base(self.driver)
            base_obj.login_ins()
            search_input = (By.ID,"instasaver.instagram.video.downloader.photo:id/etInsUrl")

            base_obj.click_element(search_input)
            base_obj.input_text(search_input,"https://www.instagram.com/p/CQudYeGjX6c/?utm_source=ig_web_copy_link")
            download_button = (By.ID, "instasaver.instagram.video.downloader.photo:id/tvDownload")
            base_obj.click_element(download_button)
            time.sleep(2)
            text_value = self.driver.find_element_by_xpath("//*[contains(@text,'下载完成')]")
            if text_value.text == "下载完成":
                print("pass",text_value.text)
            else:
                print("failed")
        except NoSuchElementException as msg:
            f_name = time.strftime("%Y%m%d%H%M%S",time.localtime((time.time())))
            self.driver.get_screenshot_as_file('/Users/zhao/Desktop/download_errorphoto/' + f_name + 'png')
            print(msg)

        self.driver.quit()

if __name__ == '__main__':
    Test_case().case_003()