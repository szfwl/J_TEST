import pytest
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class test03:

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

    def webwait(self, xpath):
        return WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element_by_xpath(xpath))

    def test_001(self):
        a = self.driver.find_element_by_xpath("//*[contains(@text,'飞行模式')]")
        b = self.driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
        self.driver.drag_and_drop(a, b)
        # time.sleep(1)
        self.webwait("//*[contains(@text,'定位服务')]").click()
        # time.sleep(1)
        self.webwait("//*[contains(@text,'模式')]").click()
        # time.sleep(1)
        self.webwait("//*[contains(@text,'高精确度')]").click()
        # time.sleep(1)
        self.driver.find_element_by_id("android:id/up").click()
        time.sleep(1)

        sum_list = self.driver.find_elements_by_id("android:id/summary")

        text_list = []
        for i in sum_list:
            text_list.append(i.text)
        assert "省电模式" in text_list, "失败了~~~"


# if __name__ == "__main__":
#     test03.setup_class()
