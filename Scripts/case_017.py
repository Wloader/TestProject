import time
from appium.webdriver.common.touch_action import TouchAction
from Basic.Base import Base
from Basic.Init_Driver import init_driver
from selenium.webdriver.common.by import By

"""
用例17：用户切换语言
1，用户进入首页
2，进入设置页面
3，切换语言
4，用户退出
"""
class Test_case():
    def __init__(self):
        self.driver = init_driver()
    def case_017(self):
        base_object = Base(self.driver)
        self.driver.implicitly_wait(5)
        # 登录ins
        base_object.login_ins()
        time.sleep(5)
        # 定位元素信息
        # 点击相应元素
        TouchAction(self.driver).press(x=500, y=200).release().perform()
        time.sleep(3)
        self.driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/ivOpenDrawer").click()
        # base_object.click_element(e_button)
        # 点击设置按钮
        set_button = self.driver.find_elements_by_id("instasaver.instagram.video.downloader.photo:id/ivTitle")
        print(type(set_button))
        for i in set_button:
            print(i.text)
        time.sleep(3)
        set_button[4].click()
        time.sleep(3)
        # 打开语言列表
        self.driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/tvLanguage").click()
        lang_text = self.driver.find_elements_by_class_name("android.view.ViewGroup")
        print(type(lang_text))
        lang_text[0].click()
        time.sleep(3)
        # 切换语言
        self.driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/tvChange").click()
        time.sleep(5)
        #点击帮助按钮
        Help_button = (By.ID,"instasaver.instagram.video.downloader.photo:id/ivHelp")
        base_object.click_element(Help_button)
        time.sleep(3)
        # 截图
        f_name = time.strftime("%Y%m%d%H%M%S", time.localtime((time.time())))
        self.driver.get_screenshot_as_file('/Users/zhao/Desktop/Language_shot/' + f_name + '.png')
        Help_msg = self.driver.find_element_by_id("android:id/text1")
        self.driver.scroll(Help_msg[0],Help_msg[1])
        f_name = time.strftime("%Y%m%d%H%M%S", time.localtime((time.time())))
        self.driver.get_screenshot_as_file('/Users/zhao/Desktop/Language_shot/' + f_name + '.png')

        self.driver.quit()

if __name__ == '__main__':
    Test_case().case_017()