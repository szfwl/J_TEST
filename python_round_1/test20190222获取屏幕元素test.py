#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from appium import webdriver
import os,time
import base64

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps["platformVersion"] = "6.0"

#允许输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard']=True

desired_caps["deviceName"] = "192.168.2.168:5555"
desired_caps["platformName"] = "Android"
desired_caps["appPackage"] = "com.tcl.cyberui"
desired_caps["appActivity"] = ".MainActivity"
#desired_caps["'appWaitActivity'"] = ".player.activity.TVDetailActivity"
#desired_caps["newCommandTimeout"]="180"
#desired_caps["keep_alive"]="true"
#解决设备经常断开连接重新启动问题cap.setCapability("noReset", true);newCommandTimeout:180
#desired_caps["noSign"]="true"
#desired_caps["noReset"]="true"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


try:
    # a = driver.find_elements_by_id("com.android.settings:id/title")
    # for e_list in a:
    #     print(e_list.text)
    #     if e_list.text == '帮助':
    #         e_list.click()
    #         time.sleep(10)

    # aa = driver.find_elements_by_class_name("android.widget.TextView")
    # for c_list in aa:
    #     if 'WLAN' in c_list.text:
    #         c_list.click()

    # xpath_value = "//*[contains(@class,'android.widget.TextView')]"
    # ele_xpath_list = driver.find_elements_by_xpath(xpath_value)

    # for i in     ele_xpath_list:
    #     if 'WLA' in i.text:
    #         i.click()
    #     time.sleep(2)
    #
    # driver.find_element_by_class_name("android.widget.Button").click()
    #
    # driver.find_element_by_id("android:id/search_src_text").send_keys("帮助")
    #
    # driver.find_element_by_id("android:id/search_src_text").clear()
    #
    # driver.find_element_by_id("android:id/search_src_text").send_keys("WLAN")

    # driver.find_element_by_class_name("android.widget.Button").click()
    #
    # for i in("W","imde324","帮助"):
    #     dd = driver.find_element_by_id("android:id/search_src_text")
    #     dd.clear()
    #     dd.send_keys(i)
    #     dd2 = dd.find_element_by_id("android:id/list").text
    #     if dd2:
    #         print(True)
    #     else:
    #
    #         print(False)
    # time.sleep(5)
    #获取属性值
    t = WebDriverWait(driver,timeout=5,poll_frequency=0.5)\
        .until(lambda x:x.find_element_by_xpath("//*[contains(@text,'精')]").get_attribute("name"))
    # a = driver.find_element_by_xpath("//*[contains(@text,'精')]").get_attribute("className")
    print(t)
    #获取 坐标
    # a = driver.find_element_by_xpath("//*[contains(@text,'精')]").location
    # print(a)
   # print("包：",driver.current_activity)
   # print("启动：",driver.current_package)


    # print(time.strftime("%H:%M:%S",time.localtime()))
    # # 显示等待
    # ele = WebDriverWait(driver,timeout=5,poll_frequency=0.5)\
    #     .until(lambda x:x.find_element_by_xpath("//*[contains(@text,'WLA')]"))
    # ele.click()

except Exception as e:
    print(e)
finally:
    print(time.strftime("%H:%M:%S", time.localtime()))
    driver.quit()