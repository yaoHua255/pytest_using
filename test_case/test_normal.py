import pytest

"""
-x   只有有用例执行失败，就退出不在执行后续

--   maxfail=2  失败用例=2时，就退出
    pytest test_case/test_normal.py -vs --maxfail 2
    
--reruns=3  失败用例重跑3次，需要先 pip install pytest-rerunfailures
    pytest -vs test_case/test_normal.py --reruns 3
"""


def test_normal_01():
    print('这里是test_normal_01')


def test_normal_02():
    '''这是测试第二个用例'''
    print('这里是test_normal_02')
    assert 1 == 2


def test_normal_03():
    print('这里是test_normal_03')
    assert 1 == 3


def test_normal_04():
    print('这里是test_normal_04')


def test_normal_05():
    print('这里是test_normal_05')


if __name__ == '__main__':
    # pytest.main(["-vs", "--maxfail=2"])
    pytest.main(["-vs"])
    # pytest.main(["-vs"], "test_normal.py::test_normal_02")
