import pytest
import time


"""
多进程执行

  -n：，也就是cpu个数 可以指定个数，最大值为当前机器cpu个数，也可以设置为auto，自动识别cpu个数。需要 pip install pytest-c
  
多进程，线程执行

　　--workers=n：多进程运行需要加此参数，  n是进程数。默认为1

　　--tests-per-worker=n：多线程需要添加此参数，n是线程数
　　
    pytest.main(['-vs', __file__, '--workers=2', '--tests-per-worker=3'])
    
    pytest test_case/test_xdist.py --workers 2 --tests-per-worker=3

"""

def test_xdist_01():
    time.sleep(4)
    print('这里是test_xdist_01')


def test_xdist_02():
    time.sleep(4)
    print('这里是test_xdist_02')


def test_xdist_03():
    time.sleep(4)
    print('这里是test_xdist_03')


def test_xdist_04():
    time.sleep(4)
    print('这里是test_xdist_04')


def test_xdist_05():
    time.sleep(4)
    print('这里是test_xdist_05')


def test_xdist_06():
    time.sleep(4)
    print('这里是test_xdist_06')


if __name__ == '__main__':
    # pytest.main(['-s', __file__, '-n=3'])
    pytest.main(['-vs', "test_case/test_xdist.py", '--workers=2', '--tests-per-worker=3'])

    # pytest test_case/test_xdist.py --workers 2 --tests-per-worker=3
