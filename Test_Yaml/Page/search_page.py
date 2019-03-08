# coding=utf-8
from Test_Yaml.Base.Base import Base
import Page

class Search_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_search_btn(self):
        self.click_element(Page.search_button)

    def input_element(self,text):
        self.input_element(Page.search_input,text)

    def back_search(self):
        self.click_element(Page.search_back)