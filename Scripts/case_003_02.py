import  time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import  By
from Basic.Base import Base
from Basic.Init_Driver import init_driver


class Test_case:
    def __init__(self):
        self.driver = init_driver()
    def  case_003_01(self):
        try:
            base_obj = Base(self.driver)
            #启动ins下载器 进入首页
            base_obj.login_ins()
            #输入框ID，要输入的text
            search_input = (By.ID,"instasaver.instagram.video.downloader.photo:id/etInsUrl")
            search_text = "https://www.instagram.com/tv/CRv6bXHIbny/?utm_source=ig_web_copy_link"
            #下载按钮
            download_button = (By.ID, "instasaver.instagram.video.downloader.photo:id/tvDownload")
            #点击输入框 输入对应 TV 类型链接
            base_obj.click_element(search_input)
            base_obj.input_text(search_input,search_text)
            #点击下载按钮
            base_obj.click_element(download_button)
            time.sleep(10)
            #等待下载 判断首页是否出现播放按钮 若出现 视为下载成功 若未出现，下载失败
            result = self.driver.find_element_by_id("instasaver.instagram.video.downloader.photo:id/ivPlay").is_displayed()
            # print(result)
            if  result :
                print("下载成功")
            else :
                print("下载失败")
        except NoSuchElementException as msg:
            f_name = time.strftime("%Y%m%d%H%M%S",time.localtime((time.time())))
            self.driver.get_screenshot_as_file('/Users/zhao/Desktop/download_errorphoto/' + f_name + 'png')
            print(msg)

if __name__ == '__main__':
    Test_case().case_003_01()



