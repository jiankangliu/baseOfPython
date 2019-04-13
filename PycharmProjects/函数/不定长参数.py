# 不定长参数/可变参数，接收任意多个数据
# 不定长位置参数
def info_print(*args):
    # 打印不定长位置参数
    print(args)             # 打印元组
    print(*args)            # 打印参数


info_print('健康', 18, '男')


# 不定长关键字参数
def info_print1(**kwargs):
    # 打印不定长关键字参数
    print(kwargs)           # 返回一个字典
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.items())


info_print1()
info_print1(name='健康', age=18, sex='男')

