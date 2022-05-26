from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Basic.Init_Driver import init_driver
from Basic.Base import Base
import time
import  pytest

"""
case_004：用户登录后下载文件
1，用户进入首页
2，输入ins链接点击下载
3，登录ins账号
4，判断是否下载成功
5，用户退出
"""

class Test_case():
    def __init__(self):
        self.driver = init_driver()
    def case_004(self):

        base_object = Base(self.driver)
        # base_object.login_ins()
        time.sleep(15)
        # 链接输入框
        search_input = (By.ID,"instasaver.instagram.video.downloader.photo:id/etInsUrl")
        # 下载按钮
        download_button = (By.ID,"instasaver.instagram.video.downloader.photo:id/tvDownload")
        # 输入框中输入链接
        input_text = ['https://instagram.com/stories/nany2994cam/2596338567684917600?utm_source=ig_story_item_share&utm_medium=share_sheet ']
        print(self.driver.context)
        base_object.input_text(search_input,"https://www.instagram.com/stories/instagram/2820681081601434108/ ")
        base_object.click_element(download_button)
        time.sleep(5)
        # 点击登录ins
        base_object.click_element((By.ID,"instasaver.instagram.video.downloader.photo:id/flLoginIns"))
        time.sleep(5)
        #查看所有上下文
        all_contexts = self.driver.contexts
        print(all_contexts)
        #切换上下文
        self.driver.switch_to.context("WEBVIEW_instasaver.instagram.video.downloader.photo")
        #查看是否切换成功
        print(self.driver.current_context)
        time.sleep(5)
        # 输入ins账号密ma
        print("123")
        # self.driver.find_element_by_name('username').send_keys("testatlas10")
        print("》》》》",self.driver.find_element_by_class_name('_2hvTZ pexuQ zyHYP'))
        # self.driver.find_element_by_name("password").send_keys("Test@1234")
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(5)
        # 登录ins成功
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(5)
        #切换时上下文返回原环境
        self.driver.switch_to.context("NATIVE_APP")
        self.driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/ivDownloads").click()

        # self.driver.quit()

if __name__ == '__main__':
    Test_case().case_004()

