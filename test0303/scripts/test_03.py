
import sys,os
# sys.path.append(os.getcwd())#搜索系统包路径
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from appium import webdriver
from selenium.webdriver.common.by import By
from Base.Base import Base

class Test_search:
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

    def test_po001(self,):
        #点击搜索按钮
        self.base_ojb.click_element(By.CLASS_NAME,"android.widget.Button")
        # 搜索框输入
        self.base_ojb.input_element(By.ID,"android:id/search_src_text","123")
        # 点击返回
        self.base_ojb.click_element(By.ID,"android:id/up")

    def teardown(self):
        self.driver.quit()
