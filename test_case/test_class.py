import pytest
# 注释这个
# @pytest.mark.siem
# def test_demo1():
#     print("这是test_demo1")


class Rizhi:
    @pytest.mark.smoke
    def test_func_01(self):
        print('这里是test_normal_01')

    def test_func_02(self):
        print('这里是test_normal_02')
        # assert 1 == 21


if __name__ == '__main__':
    pytest.main(["-vs", 'test_class.py::TestClass::test_func_01'])
