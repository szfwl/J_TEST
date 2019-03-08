import pytest


@pytest.fixture()
def init01():
    print("tx初始化数据库................")
    with open("./data.txt","w") as f:
        f.write("3")


#函数引用
@pytest.mark.usefixtures("init01")
class test1():
    def setup_class(self):
        print("111class")

    def teardown_class(self):
        print("222class")

    # @pytest.mark.usefixtures("init01")
    def test01(self):
        with open("./data.txt","r") as f:
            assert f.read() == "1"

    def test02(self):
        assert True