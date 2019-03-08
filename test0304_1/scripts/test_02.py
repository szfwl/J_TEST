# coding=utf-8
import sys,os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

sys.path.append(os.getcwd())
from appium import webdriver
from test0304_1.scripts.search.search import Search_page
import pytest

class Test_search_text:
    def setup_class(self):

        desired_caps = {}
        desired_caps["platformVersion"] = "6.0.1"
                    # 允许输入中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        desired_caps["deviceName"] = "192.168.2.168:5555"
        desired_caps["platformName"] = "Android"
        desired_caps["appPackage"] = "com.android.settings"
        desired_caps["appActivity"] = ".GridSettings"

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.search_ojb = Search_page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("text",[1,2,3])
    def test_search(self,text):
        self.search_ojb.search_text(text)


