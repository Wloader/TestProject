# -*- encoding=utf8 -*-
__author__ = "zhao"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
start_app("video.downloader.videodownloader.tube")

poco("video.downloader.videodownloader.tube:id/tvContinue").click()
sleep(3.0)
poco("video.downloader.videodownloader.tube:id/tvGotIt").click()
touch(Template(r"tpl1647594520369.png", record_pos=(-0.116, -0.736), resolution=(1080, 2340)))
sleep(5.0)
poco("onetrust-reject-all-handler").click()
sleep(3.0)
poco("Watch now").click()
sleep(5)
poco("video.downloader.videodownloader.tube:id/cvImageLayout").click()
sleep(3)
poco("video.downloader.videodownloader.tube:id/video_list_view").click()

poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("video.downloader.videodownloader.tube:id/contentListView").child("android.view.ViewGroup")[0].child("video.downloader.videodownloader.tube:id/downloadView").click()

assert_exists()

