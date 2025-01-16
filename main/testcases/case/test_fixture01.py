import pytest as pytest


class TestFixture:
    def a1(self):
        print()
        print("--------before--------")

    def a2(self):
        print()
        print("--------after---------")

    @pytest.fixture()
    def my_fixture(self):
        self.a1()

        yield

        self.a2()

    '''
    ---- 用法 1
    '''
    @pytest.mark.ui
    def test_my_fixture01(self, my_fixture):
        assert 1 == 1

    '''
    ---- 用法 2
    '''
    @pytest.mark.usefixtures('my_fixture')
    @pytest.mark.ui
    def test_my_fixture02(self):
        assert 1 == 1




