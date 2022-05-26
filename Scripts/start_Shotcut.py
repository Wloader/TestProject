from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time

desired_caps={}
#设备信息
desired_caps['platformName']='Android'
desired_caps['platormVersion']='9.0.0'
desired_caps['deviceName']=''
# desired_caps['noReset']=True
# desired_caps['fullReset']=False
#app信息
desired_caps['appPackage']='video.editor.videomaker.effects.fx'
desired_caps['appActivity']='com.atlasv.android.mediaeditor.ui.startup.StartupActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(3)

driver.find_element_by_id("video.editor.videomaker.effects.fx:id/flCreate").click()
driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()

driver.find_element_by_id("video.editor.videomaker.effects.fx:id/ivIcon").click()
el1=driver.find_element_by_xpath("//*[contains(@text,'全部')]")
el2=driver.find_element_by_xpath("//*[contains(@text,'视频')]")
driver.scroll(el1,el2)

time.sleep(3)
driver.quit()