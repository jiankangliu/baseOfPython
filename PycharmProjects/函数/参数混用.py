def info_print(name, age, sex='男', *args, **kwargs):
    print(name)
    print(age)
    print(sex)
    print(args)
    print(kwargs)


info_print('健康', 18)
# info_print('健康', 'nan', age=18)       要对应，关键字参数要放最后
# info_print('健康', 18, 1, 22, sex='nv')

