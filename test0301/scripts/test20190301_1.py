import pytest


@pytest.fixture()
def init01():
    print("初始化数据库................")
    with open("./data.txt","w") as f:
        f.write("2")


# @pytest.mark.usefixtures("init01")
class test1():

    def test01(self,init01):
        with open("./data.txt","r") as f:
            assert f.read() == "1"