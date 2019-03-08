import pytest
import allure

class Test_abc:

    # def setup(self):
    #     pass
    #
    # def teardown(self):
    #     pass

    @allure.step(title="第一个测试")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_0l(self):
        allure.attach("这是一个描述","test一下")
        assert 1
