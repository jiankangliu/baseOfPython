import my_test.my_module2

my_test.my_module2.info_print2()


# from my_test import my_module2
# my_module2.info_print()


# 如果是*的导入包的方法  切记你的包里面必须有一个文件 __init__.py 代码 __all__ = [] -- 允许导入的模块的列表
# from my_test import *
# my_module2.info_print()
# print(my_module1.a)