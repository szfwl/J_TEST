import pytest


class test_st:

    def setup_class(self):
        print("setup")

    def teardown_class(self):
        # self.driver.quit()
        print("teardown")

    @pytest.mark.run(order=5)
    def test01(self):
        print("aaaaa")
        assert True

    @pytest.mark.run(order=1)
    def test02(self):
        print("bbbbb")
        assert False



# if __name__ == '__main__':
#     pytest.main()
