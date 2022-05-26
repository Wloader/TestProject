from appium import webdriver
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as  EC

"""
用例2：获取权限进入首页
1，启动下载器
2，允许app获取权限
3，进入首页
4，用户退出app
"""

desired_caps={}

desired_caps['platformName']='Android'
desired_caps['platformVersion']='10.0.0'
desired_caps['deviceName']=''
#app信息
desired_caps['appPackage']='instasaver.instagram.video.downloader.photo'
desired_caps['appActivity']='instasaver.instagram.video.downloader.photo.ui.startup.StartupActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(3)

# try:
#     driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/tvContinue").click()
#     driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
#     time.sleep(5)
#     driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/ivBack").click()
# except NoSuchElementException as msg:
#     f_name = time.strftime("%Y%m%d%H%M%S",time.localtime((time.time())))
#     driver.get_screenshot_as_file('/Users/zhao/Desktop/download_errorphoto' + f_name + '.png')
#     print(msg)


driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/tvContinue").click()
time.sleep(3)
driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/ivBack").click()
driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/etInsUrl").send_keys("https://www.instagram.com/p/CQs0RmXoCeB/?utm_source=ig_web_copy_link")

driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/tvDownload").click()
time.sleep(5)
result = driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/ivPlay").is_displayed()
print (result)
if result:
    print("下载成功")
else:
    print("下载失败")
# driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/ivDownloads").click()
# time.sleep(3)
# driver.find_element_by_id("instasaver.instagram.video.downloader.photo: id/ivMore").click()
# result = driver.find_element_by_id("instasaver.instagram.video.downloader.photo: id/ivMore").is_enabled()
# print(result)
# result = is_element_visible(self,(By.ID,"instasaver.instagram.video.downloader.photo: id / ivMore"))
# result = file_more.is_displayed()

# instasaver.instagram.video.downloader.photo:id/ivPlay  首页播放按钮

def is_element_visible(self, element):
        #封装断言 元素是否可见
        try:
            the_element = EC.visibility_of_element_located(element)
            assert the_element(driver)
            flag =True
        except:
            flag = False
        return flag
driver.quit()