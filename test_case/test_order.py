"""
改变执行顺序，mark标记,需要：pip install pytest-ordering
装饰器：@pytest.mark.run(order=n)
order越小，优先级越高
pytest test_case/test_order.py -vs

"""

import pytest


def test_order_01():
    print('这里是test_order_01')


@pytest.mark.run(order=9)
def test_order_02():
    print('这里是test_order_02')


@pytest.mark.run(order=1)
def test_order_03():
    print('这里是test_order_03')


@pytest.mark.run(order=2)
def test_order_04():
    print('这里是test_order_04')


if __name__ == '__main__':
    pytest.main(["-vs"])
