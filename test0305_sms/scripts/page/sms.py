# coding=utf-8
from selenium.webdriver.common.by import By

from test0305_sms.Base.Base import Base

class Send_sms:
    def __init__(self,driver):
        self.send_obj = Base(driver)

        self.mes = (By.XPATH,"//*[contains(@text,'信息')]")

        self.new_mes = (By.ID,"com.android.mms:id/floating_action_button")

        self.send_man = (By.ID,"com.android.mms:id/recipients_editor_to")

        self.inp_mes = (By.ID,"com.android.mms:id/edit_text_bottom")

        self.send = (By.ID,"com.android.mms:id/send_button_01")

    def send_s(self):
        self.send_obj.cl_el(self.mes)

    def new_sms(self):
        self.send_obj.cl_el(self.new_mes)

    def input_sendmess(self,phone):
        self.send_obj.inp_el(self.send_man,phone)

    def inp_send(self,text):

        self.send_obj.inp_el(self.inp_mes,text)

        self.send_obj.cl_el(self.send)

