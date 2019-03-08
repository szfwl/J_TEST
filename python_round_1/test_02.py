
class Base:
    def __init__(self,driver):
        #初始化设备
        self.driver = driver

    def find_element(self,loc,loc_value):
        #定位方法
        return self.driver.find_element(loc,loc_value)

    def click_element(self,loc,loc_value):
        #点击元素
        self.find_element(loc,loc_value).click()

    def input_element(self,loc,loc_value,text):
        #输入内容
        self.find_element(loc,loc_value).send_key(text)