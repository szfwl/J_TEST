# coding=utf-8
from selenium.webdriver.common.by import By

from test0306.Base.Base import Base
from test0306.scripts import page


class Send_sms(Base):
    def __init__(self,driver):
        # self.send_obj = Base(driver)
        # self.mes = (By.XPATH,"//*[contains(@text,'信息')]")
        # self.new_mes = (By.ID,"com.android.mms:id/floating_action_button")
        # self.send_man = (By.ID,"com.android.mms:id/recipients_editor_to")
        # self.inp_mes = (By.ID,"com.android.mms:id/edit_text_bottom")
        # self.send = (By.ID,"com.android.mms:id/send_button_01")

        Base.__init__(self, driver)

    def send_s(self):
        self.cl_el(page.mes)

    def new_sms(self):
        self.cl_el(page.new_mes)

    def input_sendmess(self,phone):
        self.inp_el(page.send_man,phone)

    def inp_send(self,text):

        self.inp_el(page.inp_mes,text)

        self.cl_el(page.send)

