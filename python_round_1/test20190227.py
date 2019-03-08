#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

import sys
from appium import webdriver
import os,time
import base64


from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps["platformVersion"] = "6.0.1"

#允许输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard']=True

desired_caps["deviceName"] = "192.168.2.168:5555"
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


try:
    #左右滑动屏幕
    # driver.start_activity("com.sec.android.app.launcher","com.android.launcher2.Launcher")
    # time.sleep(2)
    # aaa = driver.get_window_size()
    # w = aaa.get("width")
    # h = aaa.get("height")
    # # driver.swipe(w*0.9,h*0.5,w*0.2,h*0.5,1000)
    # ww = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
    # #通过元素
    # # TouchAction(driver).tap(ww).perform()
    #
    # #通过坐标
    # TouchAction(driver).tap(x = ww.location.get("x"),y = ww.location.get("y")).perform()

    #通过元素
    # TouchAction(driver).long_press(ww).release().perform()

    def wait(pat):
        return WebDriverWait(driver,5,0.5).until(lambda x: x.find_element_by_xpath(pat))
    #
    a = wait("//*[contains(@text,'飞行')]")
    b = wait("//*[contains(@text,'快捷设置')]")

    TouchAction(driver).press(a).move_to(b).release().perform()
    # driver.drag_and_drop(a,b)
    #
    # wait("//*[contains(@text,'锁定屏幕')]").click()
    #
    # wait("//*[contains(@text,'屏幕锁定')]").click()
    #
    # wait("//*[contains(@text,'图案')]").click()
    # time.sleep(2)
    # #    286,1206      720,1206      720,1637    1145,1637
    # TouchAction(driver).press(x=286,y=1206)\
    #     .wait(200).move_to(x=720,y=1206).wait(200)\
    #     .move_to(x=720,y=1637).wait(200).move_to(x=1145,y=1637)\
    #     .wait(200).perform()
    # time.sleep(5)
    # print(a)
    # w2 = driver.find_element_by_id("android:id/icon")
    # TouchAction(driver).press(w2).wait(2000).release().perform()
    # time.sleep(2)
    # TouchAction(driver).long_press(x=399,y=969,duration=1000).perform()
    # time.sleep(2)

except Exception as e:
    print(e)
finally:
    print(time.strftime("%H:%M:%S", time.localtime()))
    driver.quit()