import pytest


@pytest.fixture(params=[1,2,3])
def init01(request):
    return request.param

# @pytest.fixture()
# def init02():
#     return [1,2,3]

#函数引用
class test1():
    def setup_class(self):
        print("111class")

    def teardown_class(self):
        print("222class")

    # @pytest.mark.usefixtures("init_data")
    def test01(self,init_data):
        # for i in init02:
        #     print(i)
            assert init_data == 4

