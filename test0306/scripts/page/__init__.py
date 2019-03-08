# coding=utf-8
from selenium.webdriver.common.by import By

mes = (By.XPATH,"//*[contains(@text,'信息')]")

new_mes = (By.ID,"com.android.mms:id/floating_action_button")

send_man = (By.ID,"com.android.mms:id/recipients_editor_to")

inp_mes = (By.ID,"com.android.mms:id/edit_text_bottom")

send = (By.ID,"com.android.mms:id/send_button_01")
