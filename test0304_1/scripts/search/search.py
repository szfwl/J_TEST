# coding=utf-8
from selenium.webdriver.common.by import By
from test0304.Base.Base import Base

class Search_page:
    def __init__(self,driver):
        self.s_b = (By.CLASS_NAME,"android.widget.Button")

        self.s_e = (By.ID,"android:id/search_src_text")

        self.s_r = (By.ID,"android:id/up")

        self.base_ojb = Base(driver)

    def search_text(self,text):
        self.base_ojb.cl_el(self.s_b)

        self.base_ojb.inp_el(self.s_e,text)

        self.base_ojb.cl_el(self.s_r)

