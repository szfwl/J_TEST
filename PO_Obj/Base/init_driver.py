# coding=utf-8
from appium import webdriver


def setup():
    desired_caps = {}
    desired_caps["platformVersion"] = "6.0.1"

    # 允许输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    desired_caps["deviceName"] = "192.168.2.168:5555"
    desired_caps["platformName"] = "Android"
    desired_caps["appPackage"] = "com.android.settings"
    desired_caps["appActivity"] = ".GridSettings"

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    return driver
