# coding=utf-8
from test0306.scripts.page.sms import Send_sms
from test0306.scripts.page.search import Search_page

class Page_ojb:
    def __init__(self,driver):
        self.driver = driver

    def Send_sss(self):
        return Send_sms(self.driver)

    def Search_ppp(self):
        return Search_page(self.driver)