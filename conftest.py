import pytest


# @pytest.fixture(scope='function', params='', autouse='', ids='', name='')
@pytest.fixture(scope='function')
def my_fixture():
    print('前置执行...')
    yield 123  # 利用yield可以实现函数的前后置
    print('后置执行...')

# @pytest.fixture(scope='function', params=['参数1', '参数2', '参数3'])
# def my_fixture(request):        # request固定写法
#     print(f'{request.param}前置执行..')
#     yield request.param
#     print(f'{request.param}后置执行...')
