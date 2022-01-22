import pytest

i = 2


def test_skip_01():
    print('这里是test_skip_01')
    pytest.xfail(reason="功能未完成")
    print("这里不会打印")
    assert 1 == 1  # 会被标记为xfailed


@pytest.mark.skipif(i == 0, reason="i等于0，跳过02")
def test_skip_02():
    print('这里是test_skip_02')


@pytest.mark.skip(reason="跳过03")
def test_skip_03():
    print('这里是test_skip_03')


@pytest.mark.xfail(reason="用例未修复")
def test_skip_04():
    print('这里是test_skip_04')
    # assert 1 == 2


def test_skip_05():
    print('这里是test_skip_05')


if __name__ == '__main__':
    pytest.main("[-vs]")
