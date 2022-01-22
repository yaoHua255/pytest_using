import pytest


# @pytest.fixture(scope='function')
# def my_fixture():
#     print('前置执行...')
#     yield  # 利用yield可以实现函数的前后置
#     print('后置执行...')


class TestHook:

    def test_01(self):
        print('测试test01')

    # 当需要调用前后置函数时就把函数名传入到测试方法中即可
    def test_02(self):
        print('测试test02')
        # print('测试test02: {}'.format(my_fixture))

    def test_03(self):
        print('测试test03')


if __name__ == '__main__':
    pytest.main()
