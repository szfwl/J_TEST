# coding=utf-8
import sys,os
sys.path.append(os.getcwd())
from Test_Yaml.Page.Page import Page_Obj
from Base.Base import Base
import pytest
from Test_Yaml.Base.read_data import ret_yaml

def test_data():
    data_list = []
    data = ret_yaml("search_data").get("search_data")
    for i in data.keys():
        data_list.append((i,data.get(i).get("test")))
    return data_list

class Test_search:
    def setup_class(self,driver):
        self.driver = Base.__init__(self,driver)
        self.search_obj = Page_Obj(self.driver).re_seach()
        self.search_obj.cli_search_btn()

    def teardown_class(self):
        self.driver.quit()
        self.search_obj.retrun_search()


    @pytest.mark.parametrize("test_num,text",test_data())
    def test_search(self,test_num,text):
        print("用例编号：",test_num)
        self.search_obj.inp_search(text)
        self.driver.get_scrrenshot_as_flie("./screen/%s" %test_num)