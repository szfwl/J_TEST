import pytest


class test_st:

    def setup_class(self):
        print("setup")

    def teardown_class(self):
        # self.driver.quit()
        print("teardown")

    def test01(self):
        assert True

    def test02(self):
        assert False



if __name__ == '__main__':
    test_st().setup_class()
