# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from selenium import webdriver

import time,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

import io
import unittest
import sys

# 1. 打开浏览器，访问p.to
driver = webdriver.Ie
def openDriver():
    driver.get()
    driver.maximize_window()

# 2. 登陆
class loginClass(object):
    """docstring for login"""
    def __init__(self, arg):
        self.login_pwd = arg

    def login(self):
        waitandSendkeys('//*[@id="Pwd"]', self.login_pwd)
        waitandClick('//*[@id="Save"]')

def login(data):
    openDriver()
    test1 = loginClass(data)
    test1.login()

# 3.修改管理员密码
class changePwdClass(object):
    """docstring for changePwdClass"""
    def __init__(self, arg):
        self.pwdNew = arg.get('pwdNew', '')
        self.pwdOld = arg.get('pwdOld', '')

    def changeUserPwd(self):
        waitandClick('//*[@id="Con"]/div[1]/ul[2]/li[1]')
        waitandClick('//*[@id="Con"]/div[1]/ul[2]/li[1]/ul/li[3]')
        waitforDisplay('//*[@id="_Widget"]')
        waitandSendkeys('//*[@id="PwdOld"]', self.pwdOld)
        waitandSendkeys('//*[@id="PwdNew"]', self.pwdNew)
        waitandSendkeys('//*[@id="PwdCfm"]', self.pwdNew)
        waitandClick('//*[@id="SavePwd"]')

def changeUserPwd_main(data):
    changePwdObj = changePwdClass(data)
    changePwdObj.changeUserPwd()

# 4. 单元测试数据
errcode = ['oldPwdErr', 'lenErr', 'charErr', 'matchErr', 'pwdSameErr',\
    'oldPwdBlankErr', 'newPwdBlankErr']
errTips = {
    'oldPwdErr' :'原密码错误',
    'lenErr' : '新密码长度应为5~63位',
    'charErr' : "新密码包含非法字符",
    'matchErr' : '两次密码输入不一致',
    'pwdSameErr' : '新密码与原密码相同，请重新输入',
    'oldPwdBlankErr' : '请输入原密码',
    'newPwdBlankErr' : '请输入新密码'
}

# 5. 检查输入的数据合法性
def checkData(data):#检查顺序跟页面顺序相同
    #pwd = loginPwd
    pwd='admin'
    #'oldPwdBlankErr'
    if data['pwdOld'] == "":
        return errcode[5]
    #newPwdBlankErr
    if data['pwdNew'] == "":
        return errcode[6]
    #charErr
    strTmp = data['pwdNew']
    for x in range(0,len(data['pwdNew'])):
        if ord(strTmp[x]) < 33 or ord(strTmp[x]) > 127:#ASCII表示范围:32-127
            return errcode[2]
    #lenErr
    if len(data['pwdNew']) > 63 or len(data['pwdNew']) < 5:
        return errcode[1]
    #oldPwdErr
    if pwd != data['pwdOld']:
        return errcode[0]
    #pwdSameErr
    if data['pwdNew'] == data['pwdOld']:
        return errcode[4]
    #no error
    return None

# 6. 获取输入错误数据之后的页面提示语
def checkResponse(error):
    if error == None:
        return
    # webText = driver.find_element_by_xpath('//*[@id="PwdTip"]').text
    webText = getText('//*[@id="PwdTip"]')
    if webText == False:#没有提示
        print('###Error: no tips on web!')
    else:
        webText = webText.decode('UTF-8')
    waitandClick('//*[@id="ModifyPwd"]/i')
    return webText

# 8.单元测试类
class TestCase(unittest.TestCase):
    # 7. 编写测试用例
    data = [
        {"pwdNew" : "12345678","pwdOld" : '8dadla'},#"oldPwdErr"
        {"pwdNew" : "admi","pwdOld" : 'admin'},#lenErr
        {'pwdNew' : '1  2  3','pwdOld' : 'admin'},#charErr
        {'pwdNew' : 'admin','pwdOld' : 'admin'},#pwdSameErr
        {'pwdNew' : "",'pwdOld' : ""},#oldPwdBlank
        {'pwdNew' : "",'pwdOld' : "admin"}#newPwdBlank
    ]

    def commonAction(self, arg):
        error = checkData(arg)
        changeUserPwd_main(arg)
        self.assertEqual(checkResponse(error), errTips[error])
        time.sleep(1)

    def test_oldPwdErr(self):
        self.commonAction(self.data[0])
    def test_lenErr(self):
        self.commonAction(self.data[1])
    def test_charErr(self):
        self.commonAction(self.data[2])
    def test_pwdSameErr(self):
        self.commonAction(self.data[3])
    def test_oldPwdBlank(self):
        self.commonAction(self.data[4])
    def test_newPwdBlank(self):
        self.commonAction(self.data[5])

# 10. 关闭浏览器
def closeDriver():
    time.sleep(3)
    driver.quit()
    os.system('killall chromedriver')
    os.system('killall geckodriver')

# 11. 异常处理
## 11.1 点击函数
def waitandClick(xpath):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except TimeoutException as e:
        print('Error:waitandClick, TimeoutException, xpath = %s\n' % xpath)
    else:
        driver.find_element_by_xpath(xpath).click()

## 11.2 填写表单
def waitandSendkeys(xpath, keys):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except TimeoutException as e:
        print('Error:waitandSendkeys, TimeoutException, xpath = %s\n' % xpath)
    else:
        driver.find_element_by_xpath(xpath).clear()
        driver.find_element_by_xpath(xpath).send_keys(keys)

## 11.3 元素加载
def waitforDisplay(xpath):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except TimeoutException as e:
        print('Error:waitforDisplay, TimeoutException, xpath = %s\n' % xpath)
    else:
        try:
            process = driver.find_element_by_xpath(xpath)
            WebDriverWait(driver, 10).until(lambda driver: process.is_displayed())
        except NoSuchElementException as e:
            print('Error:waitforDisplay, NoSuchElementException, xpath = %s\n' % xpath)

def elementIsDisplayed(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException as e:
        return False

def getText(xpath):
    time.sleep(1)
    return driver.find_element_by_xpath(xpath).text

if __name__ == '__main__':
    openDriver()
    login('admin')
    #data = {'pwdNew'='admin', 'pwdOld'='12345678'}
    #changeUserPwd_main(data)
    #9. 进行单元测试并生成测试报告
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_report',report_title='修改管理员密码试报告'))
    closeDriver()
