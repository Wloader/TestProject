from appium import webdriver
import time
# import pytest
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support import expected_conditions as  EC

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

driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/tvContinue").click()
time.sleep(3)
driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/ivBack").click()
time.sleep(3)
driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/etInsUrl").send_keys("https://www.instagram.com/stories/instagram/2820681081601434108/")
driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/tvDownload").click()
time.sleep(3)
driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/flLoginIns").click()
time.sleep(5)
print(driver.contexts)
# print(driver.page_source)
driver.switch_to.context("WEBVIEW_instasaver.instagram.video.downloader.photo")
print(driver.page_source)
driver.switch_to.context("NATIVE_APP")
print(driver.current_context)
print(driver.page_source)

hans = driver.window_handles
print(u"拥有"+str(len(hans))+u"窗口句柄")
# print(driver.window_handles)
# hand_name = hans[-1]
# driver.switch_to.window(hand_name)

print("123")
time.sleep(3)
# driver.find_element_by_css_selector("[name='username']").click()
# driver.find_element_by_xpath("//*[contains(@text,'密码')]").send_keys("Test@1234")
driver.find_element_by_android_uiautomator('new UiSelector().text("密码")').click().send_keys("Test@1234")
driver.find_element_by_name('username').send_keys("testatlas10")
# driver.find_element_by_xpath("//*[contains(@name,'password')]").send_keys("Test@1234")
driver.find_element_by_tag_name("button").click()

driver.quit()