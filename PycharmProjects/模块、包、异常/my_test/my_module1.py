__all__ = ['a', 'info_print1']  # 设置通过xxx * 导入模块的时候的导入列表

a = 1


def info_print():
    print(10)


def info_print1():
    print(100)


if __name__ == '__main__':
    info_print()
    info_print1()

# print(globals())
# print(__name__)