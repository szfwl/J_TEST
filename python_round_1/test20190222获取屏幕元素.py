#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from appium import webdriver
import os,time
import base64

desired_caps = {}
desired_caps["platformVersion"] = "6.0.1"
desired_caps['unicodeKeyboard'] = True
desired_caps["deviceName"] = "huawei"
desired_caps["platformName"] = "Android"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".GridSettings"
#desired_caps["'appWaitActivity'"] = ".player.activity.TVDetailActivity"
#desired_caps["newCommandTimeout"]="180"
#desired_caps["keep_alive"]="true"
#解决设备经常断开连接重新启动问题cap.setCapability("noReset", true);newCommandTimeout:180
#desired_caps["noSign"]="true"
#desired_caps["noReset"]="true"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
a=driver.page_source

print(a)
# driver.find_element_by_id().send_keys()
if "android.widget.TextView123" in a:
    print("是的")
else:
    print("没有")
#print(driver.page_source)