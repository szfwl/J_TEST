# coding=utf-8
from Base.Base import Base
import Page

class Search_page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def cli_search_btn(self):
        self.click_element(Page.search_button)

    def inp_search(self,text):
        self.input_element(Page.search_input,text)

    def retrun_search(self):
        self.click_element(Page.search_back)