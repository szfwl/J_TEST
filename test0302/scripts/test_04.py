import pytest

def re_data():
    lis = []
    with open('/python_work/test0302/scripts/data.txt','r') as f:
        # for i in f.readlines():
        #     print(i)
        # print(f.readlines())
        for i in f.readlines():
            # print(i)
            # print(type(eval(i.split("=")[-1])))
            lis.append(eval(i.split("=")[-1]))
        # print(lis)
        return lis

class Test_p:
    @pytest.mark.parametrize("li,wang",re_data())
    def test_0(self,li,wang):
        print("li:%s,wang:%s"%(li,wang))
        # assert li == 789

# re_data()