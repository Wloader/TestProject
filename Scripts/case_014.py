from Basic.Init_Driver import init_driver
from Basic.Base import Base

"""
用例14：用户查看帮助信息
1，用户进入首页
2，查看帮助信息
3，用户退出
"""
class Test_case:
    def __init__(self):
        self.driver = init_driver()
    def case_014(self):
        base_obj = Base(self.driver)
        base_obj.login_ins()
        base_obj.input_text()
