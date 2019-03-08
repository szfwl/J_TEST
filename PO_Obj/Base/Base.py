# coding=utf-8

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver

    def find_element_I(self,loc,timeout=10,poll=1):
        return WebDriverWait(self.driver,timeout,poll)\
            .until(lambda x:x.find_element(*loc))

    def click_element(self,loc):
        self.find_element_I(loc).click()

    def input_element(self,loc,text):
        # a = self.find_element_I(loc)
        # a.clear()
        # a.send_keys(text)

        self.find_element_I(loc).send_keys(text)