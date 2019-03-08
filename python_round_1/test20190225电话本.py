#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from appium import webdriver
import os,time
import base64

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
    # time.sleep(5)
    # driver.swipe(1623,977,458,985,5000)
    # driver.background_app(5)
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[contains(@text,'生活')]").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[contains(@text,'教育')]").click()
    # print(driver.device_time)
    # print(driver.get_window_size())
    # a = driver.get_window_size()
    # x = a.get("width")/2
    # y = a.get("height")*0.8
    # y_1 = a.get("height")*0.2
    #
    # driver.swipe(x,y,x,y_1,1000)
    # for i in range(3):
    #     driver.keyevent(25)
    #打开通知栏
    # # driver.open_notifications()
    # driver.open_notifications()
    # # driver.set_network_connection(0)
    # # driver.find_element_by_xpath("//*[contains(@text,'保护中')]").click()
    # driver.swipe(667,625,378,617,1000)

    # s = driver.find_element_by_xpath("//*[contains(@text,'飞行')]")
    # m = driver.find_element_by_xpath("//*[contains(@text,'帮助')]")
    # driver.drag_and_drop(s,m)
    #
    # w_h = driver.get_window_size()
    # x = w_h.get("width")/2
    # y = w_h.get("height")*0.2
    # y_2 = w_h.get("height")*0.8
    #
    # driver.swipe(x,y_2,x,y,500)
    #
    # cc = driver.find_element_by_xpath("//*[contains(@text,'壁纸')]")
    # print(cc.location)
    #
    # # time.sleep(5)
    # driver.open_notifications()
    # a = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'保护中')]"))
    # a.click()
    # driver.background_app(5)
    # b = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'加速')]"))
    # b.click()
    # driver.get_screenshot_as_file("./other/0226.png")
    print(driver.keyevent(25))
    #  driver.find_element_by_xpath("//*[contains(@text,'保护中')]").click()
    driver.win
    # driver.get_screenshot_as_file("E:\python_work\other\1.png")
except Exception as e:
    print(e)
finally:
    print(time.strftime("%H:%M:%S", time.localtime()))
    driver.quit()