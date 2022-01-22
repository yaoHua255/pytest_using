 
##  单元测试框架：
 
 unittest、pytest、junit、testing
     
     1、测试发现：从多个文件中查找
     
     2、测试执行：按一定的顺序和规律执行，生成结果
     
     3、测试判断：断言结果差异
     
     4、测试报告：统计测试进度，耗时，通过率，生成测试报告
 
 
##  自动化测试框架：
 
     单元测试框架是自动化测试框架一部分，
     
     设计模式（POM）
     
     配置文件conf及读写
     
     日志log、截图
     
     报告report
     
     数据库读写
     
     邮件
     
 
 
 
## pytest规则：

- 测试文件以test_开头或 test_结尾
- 测试类以Test开头，测试类不能有__init__方法
- 用例方法test_开头


## 运行方式：

1、主函数模式

    (1)运行所有 pytest.main()
    (2)指定模块 pytest.main(["-vs", "./test_cases/test_level.py"])
    (3)指定目录 pytest.main(["-vs", "./test_cases/"])
    (4)通过nodeid指定用例运行：nodeid由模块名，分隔符，类名，方法名，函数名组成
        #pytest.main(["-vs",'./test_cases/test_class.py::test_demo1'])
        #pytest.main(["-vs", './test_cases/test_class.py::TestClass::test_func_01'])

    
2、命令行模式

    (1)运行所有：pytest
    (2)指定模块 pytest -vs ./test_cases/test_level.py
    (3)指定目录 pytest -vs ./test_cases/
    (4)通过nodeid指定用例运行：nodeid由模块名，分隔符，类名，方法名，函数名组成
    pytest -vs test_cases/test_class.py::test_demo1
    pytest -vs test_cases/test_class.py::TestClass::test_func_01
    



3、读取pytest.ini文件配置执行



## 参数详解：

-s:  表示输出调试信息，包括print打印的信息

-v   显示更详细的信息

-vs  一起使用

-x   只要有用例执行失败，就退出不再执行后续

    pytest test_cases/test_normal.py  -x

--maxfail=2  失败用例=2时，就退出

    pytest test_cases/test_module_01.py -vs --maxfail 2
    

--reruns=3  失败用例重跑3次，需要先 pip install pytest-rerunfailures

    pytest -vs test_cases/test_normal.py --reruns 3




---
###多进程执行

  -n：，也就是cpu个数 可以指定个数，最大值为当前机器cpu个数，也可以设置为auto，自动识别cpu个数。需要 pip install pytest-xdist
  

    test_cases/test_xdist.py
    
     
     pytest -vs test_cases/test_xdist.py -n 3



---

###多进程，线程执行

　　--workers=n：多进程运行需要加此参数，  n是进程数，默认为1（windows上只能为1）

　　--tests-per-worker=n：多线程需要添加此参数，n是线程数
　　
    pytest.main(['-vs', __file__, '--workers=2', '--tests-per-worker=3'])
    
    pytest test_cases/test_xdist.py --workers 2 --tests-per-worker=3 -vs


 多进程，线程执行用例要求：用例相互独立、无关联，没有先后顺序影响（如增删改查同一项）


---

###改变执行顺序，mark标记

需要：pip install pytest-ordering

用法：使用装饰器：@pytest.mark.run(order=n)

order越小，优先级越高
 
    pytest test_cases/test_order.py -vs

---

###用例跳过


    # 直接跳过用例
    @pytest.mark.skip(reason="跳过03")
    
    #有条件跳过用例
    @pytest.mark.skipif(i == 0, reason="i等于0，跳过02")

    # 用例步骤内跳过
        pytest.xfail(reason="功能未完成")
        # 或
        @pytest.mark.xfail(reason="用例未修复")  #会执行，只是结果标记未xfailed或xpassed
        
        
    pytest -vs test_cases/test_skip.py
    
    

    

---

###断言 

pytest断言直接使用python关键字assert

assert 断言语句



---
###pytest前后置


1、setup与teardown，setup_class与teardown_class


2、使用@pytest.fixture()装饰器来实现部分用例的前后置

    https://www.jianshu.com/p/7a5286a84f87
    
    装饰器样例: @pytest.fixture(scope='', params='', autouse='', ids='', name='')
    
    （1） scope表示标记方法的作用域，包含：
    
            function（默认），作用于每个测试函数，等价于setup/teardown
            
            class，作用于每个测试类，等价于setup_class/teardown_class
            
            module，作用于每个py文件之
            
            package/session，多个模块调用1次，通常写在conftest中

    （2）params：参数化（支持列表，元组，字典列表，字典元组）
    
    （3）autouse：自动使用装饰函数，默认是False
    


3. 全局的fixture前后置


- conftest.py和@pytest.fixture结合
- conftest.py文件，固定名称，不可更改，单独存放夹具方法的配置文件（即将@pytest.fixture装饰的函数写在conftest.py中）
- 不需要做import操作


    
---

###报告输出

1、pytest-html
    
    pip install pytest-html
    
    pytest -vs test_cases/test_normal.py --html=report.html


2、allure

安装：brew install allure

pip install allure-pytest


报告生成

     pytest --alluredir=./report/tmp --clean-alluredir     # pytest执行用例，生成测试数据
    
    allure generate ./report/tmp -o ./report/html --clean  # 利用allure,根据测试数据生成测试报告

bug等级

[参考地址](https://www.cnblogs.com/123blog/p/12499785.html)

    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''
    
    @allure.severity("blocker")
    
    只执行堵塞、严重级别用例：
    pytest --alluredir ./report/tmp --clean-alluredir --allure-severities blocker,critical


---

pytest.ini 配置文件

作用：可以修改 pytest 的默认行为

位置：项目根目录

格式要求：不能使用中文符号，包括汉字、空格、引号、冒号等等

运行规则：主函数及命令行模式都采用该配置

    pytest.ini

    [pytest]
    addopts = -vs --html=report.html
    testpaths = testcase
                testcase2
    python_files = test*.py *.py
    python_classes = Test*
    python_functions = test*
    markers = smoke:checklist
              user:userManager
    

---
分组执行
pytest.ini 添加
    
    markers =   smoke:This is smoke testcase
                user:userPage
    用例添加：@pytest.mark.smoke
    
    执行：pytest -vs -m "smoke or user"
