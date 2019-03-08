#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from appium import webdriver
import os,time
desired_caps = {}
desired_caps["platformVersion"] = "6.0"
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

query="你好"
os.system('adb shell am startservice -n com.tcl.walleve/com.tcl.walleve.SpeechService -a com.tcl.walleve.pitch --es text '+query)