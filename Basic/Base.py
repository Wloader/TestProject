import time

from appium  import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

class Base(object):
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc,timeout=10):
        # 封装为智能等待方法
        # loc:类型为元组，格式（By.ID,value),(By.CLASS_NAME,value),(By.XPATH,value)
        # timeout : 搜索超时时间
        return WebDriverWait(self.driver,timeout).until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        # 封装点击操作
        self.find_element(loc).click()

    def input_text(self, loc, text):
        # 封装输入操作
        self.fm = self.find_element(loc)
        self.fm.clear()  # 需要先清空输入框，防止有默认内容
        self.fm.send_keys(text)

    def login_ins(self):
        #封装进入启动app进入首页
        self.click_element((By.ID,"instasaver.instagram.video.downloader.photo:id/tvContinue"))
        # self.click_element((By.ID,"com.android.packageinstaller:id/permission_allow_button"))
        self.click_element((By.ID,"instasaver.instagram.video.downloader.photo:id/ivBack"))
        # time.sleep(3)

    def is_element_visible(self, element):
        #封装断言 元素是否可见
        try:
            the_element = EC.visibility_of_element_located(element)
            assert the_element(self)
            flag = True
        except:
            flag = False
        return flag





