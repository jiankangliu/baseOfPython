def info_print(name, age, sex):
    print(f'名字是{name},年龄{age}，性别{sex}')
    return 0


info_print('健康', 18, '男')
info_print(age=18, name='健康', sex='男')
info_print('健康', age=18, sex='男')


def info_print1(name, age, sex='男'):            # 参数带有默认值
    print(f'名字是{name}，年龄{age}，性别{sex}')
    return 0


info_print1('健康', 18)

