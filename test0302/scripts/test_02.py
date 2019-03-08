import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Test_find:
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

    #显示等待
    def wait(self,type,data):
        if type == "xpath":
            return WebDriverWait(self.driver,2,1).until(lambda x:x.find_element_by_xpath(data))
        if type == "id":
            return WebDriverWait(self.driver,2,1).until(lambda x:x.find_element_by_id(data))
        if type == "class":
            return WebDriverWait(self.driver,2,1).until(lambda x:x.find_element_by_class_name(data))

    #打开搜索及输入
    @pytest.fixture()
    def test_find(self):
        self.wait("class","android.widget.Button").click()
        characters = ["123","你好吗","wla"]
        for i in characters:
            d = self.wait("id","android:id/search_src_text")
            d.clear()
            d.send_keys(i)

    #进入wlan，关闭wlan
    @pytest.mark.usefixtures("test_find")
    def test_wlan(self):
        self.wait("id","com.android.settings:id/search_icon").click()
        te = self.wait("class","android.widget.Switch").text
        if te == "开":
            self.wait("xpath", "//*[contains(@text,'开')]").click()
        else:
            print("已关闭，谢谢")
        assert  "关" in self.wait("class","android.widget.Switch").text



