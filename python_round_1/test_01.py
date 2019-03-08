import pytest


class Test1:
    @pytest.fixture()
    def test01(self):
        return 1

    @pytest.fixture(params=[1,2,3,4])
    def more(self,request):

        print(request.param)
        return request.param



    def test02(self,test01):#可拿参数
        assert test01 == 1

    @pytest.mark.usefixtures("test01")#不可取到参数
    def test03(self):
        assert False

    def test_use(self,more):
        assert more == 2

    @pytest.mark.parametrize("a,s,d",[(1,2,3),(4,5,6)])
    def test_p(self,a,s,d):
        assert a+s+d == 6



if __name__ == '__main__':

    pytest.main()
