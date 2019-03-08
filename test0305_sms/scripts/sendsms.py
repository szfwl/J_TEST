# coding=utf-8
import time
import pytest
from selenium.webdriver.common.by import By

import selenium

from test0305_sms.scripts.page.sms import Send_sms
from appium import webdriver
import os,sys
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
sys.path.append(os.getcwd())
class Test_sendsms:
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

        self.sms_obj = Send_sms(self.driver)

    def teardown_class(self):
        self.driver.quit()
    #进入信息
    def test_sms(self):
        self.driver.keyevent(4)
        time.sleep(2)
        self.sms_obj.send_s()
    #新建信息
    def test_newsms(self):
        self.sms_obj.new_sms()

    #增加收件人
    # @pytest.mark.parametrize("oo",[1232312323,123123123])
    # @pytest.mark.run(order=1)
    # @pytest.fixture(params=['13632780071'])
    def test_man(self):
        self.sms_obj.input_sendmess("13632780071")

    @pytest.mark.parametrize("text",["你好",4656])
    def test_leirong(self,text):
        self.sms_obj.inp_send(text)
        time.sleep(2)
        self.driver.find_element(By.ID,"android:id/button1").click()
        #截图
        self.driver.get_screenshot_as_file("s_%s.png"%text)

