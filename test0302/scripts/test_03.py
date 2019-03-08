import pytest


def abb():
    with open("./scripts/data.txt","r") as f:
        if '5' in f.read():
            return True
        else:
            return False

class Test_pas:


    def test_a(self):
        print("aaaaaaaa")
        return True


    # @pytest.mark.skipif(abb(),reason="必须写")
    @pytest.mark.xfail(abb(),reason="123")
    def test_b(self):
        print("bbbbbbbbbbb")
        assert False