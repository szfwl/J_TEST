import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Test_index:
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

    def teardown_class(self):
        self.driver.quit()

    def wait(self,type,data):
        if type == "id":
            return WebDriverWait(self.driver,5,1)\
                .until(lambda x:x.find_element_by_id(data))
        if type == "xpath":
            return WebDriverWait(self.driver,5,1)\
                .until(lambda x:x.find_element_by_xpath(data))
    # @pytest.fixture()
    def test_in_idex(self):
        more = self.wait("xpath","//*[contains(@text,'飞行模式')]")
        more2 = self.wait("xpath","//*[contains(@text,'WLAN')]")
        #滑动界面
        self.driver.drag_and_drop(more,more2)

        self.wait("xpath","//*[contains(@text,'定位服务')]").click()

    # @pytest.mark.usefixtures("test_in_idex")
    def test_change_mod(self):
        #改变模式
        self.wait("xpath","//*[contains(@text,'模式')]").click()
        self.wait("xpath","//*[contains(@text,'省电模式')]").click()
        self.wait("id","android:id/up").click()
        assert "省电模式" in self.driver.find_element_by_id("android:id/summary").text

