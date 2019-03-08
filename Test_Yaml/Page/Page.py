# coding=utf-8
from Page.Search_page import Search_page

class Page_Obj:
    def __init__(self,driver):
        self.driver = driver

    def return_search(self):
        return Search_page(self.driver)