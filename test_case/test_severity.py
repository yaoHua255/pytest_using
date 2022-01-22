import pytest
import allure

"""
@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷
CRITICAL = 'critical'　严重缺陷
NORMAL = 'normal'　　  一般缺陷
MINOR = 'minor'　　    次要缺陷
TRIVIAL = 'trivial'　　轻微缺陷　
"""


@allure.severity("blocker")
def test_severity_1():
    """blocker阻塞缺陷"""
    print("test case 11111111")
    assert False


@allure.severity("critical")
def test_severity_2():
    """critical严重缺陷"""
    print("test case 222222222")
    assert True


@allure.severity("minor")
def test_severity_3():
    """minor次要缺陷"""
    print("test case 333333333")


@allure.severity("trivial")
def test_severity_4():
    """trivial轻微缺陷"""
    print("test case 4444444")


def test_severity_5():
    """没标记severity的用例默认为normal"""
    print("test case 5555555555")


@allure.severity("blocker")
def test_severity_6():
    """blocker阻塞缺陷"""
    print("test case 666666")


if __name__ == '__main__':
    pytest.main('[-vs]', './testcase/test_day1.py')
