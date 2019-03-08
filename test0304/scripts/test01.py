# coding=utf-8
import pytest
import os,sys
import time
# sys.path.append(os.getcwd())
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from Base.Base import Base

class Test:
    def setup(self):
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

        self.base_ojb = Base(self.driver)

    def test1(self):

        s_b = (By.XPATH,"//*[contains(@text,'应用程序')]")
        s_b1 = (By.XPATH,"//*[contains(@text,'我的文件')]")
        s_b2 = (By.XPATH,"//*[contains(@text,'图片')]")
        time.sleep(2)
        self.driver.keyevent(4)
        time.sleep(2)
        self.base_ojb.cl_el(s_b)

        self.base_ojb.cl_el(s_b1)

        self.base_ojb.cl_el(s_b2)

        TouchAction(self.driver).long_press(x=375,y=559,property=5)\
            .release().perform()

        self.driver.keyevent(3)

    def teardown(self):
        self.driver.quit()


