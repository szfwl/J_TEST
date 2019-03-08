# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver

    # def find_element(self,vod,vod_valus,timeout=5,poll=1):
    #     return WebDriverWait(self.driver,timeout,poll)\
    #         .until(lambda x:x.find_element(vod,vod_valus))

    #loc是元祖类型
    def find_element(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll)\
            .until(lambda x:x.find_element(*loc))


    def cl_el(self,loc):
        self.find_element(loc).click()

    def inp_el(self,loc,text):
        ele = self.find_element(loc).send_key(text)

