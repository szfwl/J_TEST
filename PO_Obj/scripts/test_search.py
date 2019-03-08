# coding=utf-8
import os,sys
sys.path.append(os.getcwd())

from Base.init_driver import setup
from Page.Page_obj import Page_obj
import pytest

class Test_Search:
    def setup_class(self):
        self.driver = setup()
        self.po = Page_obj(self.driver).re_seach()
        self.po.cli_search_btn()

    def teardown_class(self):
        self.po.retrun_search()
        self.driver.quit()

    @pytest.mark.parametrize("text", [1,2])
    def test_cl(self,text):
        self.po.inp_search(text)
