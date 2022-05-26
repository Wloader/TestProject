# -*- encoding=utf8 -*-
__author__ = "zhao"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
start_app("video.downloader.videodownloader.tube")
slepp(5)
touch(Template(r"tpl1647590423648.png", record_pos=(0.009, 0.247), resolution=(1080, 2340)))
poco().click