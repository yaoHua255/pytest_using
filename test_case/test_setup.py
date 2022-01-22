import pytest


class TestHook:

    # 这个函数在整个类所有的测试用例执行之前只执行一次
    def setup_class(self):
        print('\nsetup_class：一般用于执行初始化工作，比如创建日志对象、创建数据库连接对象')

    # 这个函数在每个测试函数执行之前都会执行一次
    def setup(self):
        print('\nsetup：可以用于执行浏览器的打开操作')

    # 这个函数在每个测试函数执行完成以后都会执行一次
    def teardown(self):
        print('\nteardown：可以用于关闭浏览器操作')

    # 这个函数在每个测试类执行完成以后会执行一次
    def teardown_class(self):
        print('\nteardown_class：一般用于销毁日志对象，关闭数据库连接等等')

    def test_setup_01(self):
        print('测试test_setup_01')

    def test_setup_02(self):
        print('测试test_setup_02')

    def test_setup_03(self):
        print('测试test_setup_03')


if __name__ == '__main__':
    pytest.main("[-vs]")
