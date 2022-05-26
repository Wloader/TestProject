from appium import webdriver
def init_driver():
    # 服务端启动参数
    desired_caps = {}
    # 手机系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10.0'
    desired_caps['deviceName'] = ''
    # app包名和启动名
    desired_caps['appPackage'] = 'instasaver.instagram.video.downloader.photo'
    desired_caps['appActivity'] = 'instasaver.instagram.video.downloader.photo.ui.startup.StartupActivity'

    desired_caps['chromedriverExecutbleDir'] = '/usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac'
    desired_caps['chromedriverChromeMappingFile'] = '/usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver/chromedriver_support.json'
    # 手机驱动对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver # 返回driver对象