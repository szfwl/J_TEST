# coding=utf-8


from Page.Search_page import Search_page

class Page_obj:
    def __init__(self,driver):
        self.driver = driver

    def re_seach(self):
        #返回搜索对象页面
        return  Search_page(self.driver)