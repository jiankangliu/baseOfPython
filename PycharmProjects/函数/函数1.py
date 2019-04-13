# def information():
#     print('My name is Liu')
#     print('My major is Python')
#
#
# def add(a, b):
#     return a + b
#
#
# print(add(2, 3))
#
# def add_minus(a, b, c):
#     print(f"{a}+{b}={a+b}")
#     print(f"{a+b}-{c}={a+b-c}")
#     return a + b - c
# result = add_minus(2,3,1)
# print(result)
#
#
# def recursion(a):
#     if a == 1:
#         return a
#     else:
#         return a * recursion(a-1)
#
#
# print(recursion(5))
#
#
# def divid(a, b):
#     return a//b, a%b        # return 返回多个数据，默认返回元组
# # return 后面可以是元组，字典，列表，只要是能存储多个数据的类型就能返回多个数组
# a = divid(4,3)
# print(a)
#
#
# # 缺省参数
# # 在形参中默认有值的参数是缺省参数
# # 带有默认值的参数一定位于参数列表的最后面
# def prinformation (name,age = 35):
#     print(f'姓名{name}，年龄{age}')
#
#
# prinformation(name='Liu')
# prinformation(name='Liu', age= 9)
#
#
# # 不会
# # 不定长参数
# # 形式def function(a, b, *args, **kwargs):
# # *args代表数组， **kwargs会存放命名参数， 形如key = value, kwargs为字典
# # args = (7, 8, 9)
# # kwargs = {'a': 5, 'b': 6}
# # def function(a, b, c, *args, **kwargs):
# #     print(a)
# #     print(b)
# #     print(c)
# #     print(args)
# #     print(kwargs)
# print()
#
#
# # 拆包交换变量的值
# def get_my_information():
#     high = 170
#     wight = 60
#     age = 22
#     return high, wight, age             # 返回一个元组
#
#
# high, wight, age = get_my_information()     # 同时赋值多个变量
# # 拆包时需要注意需要拆的数据个数与变量的个数相同，否则程序会异常
# # 除了对元组拆包外，还可以对列表字典进行拆包
# print(f'我的身高{high}，体重{wight}，年龄{age}')
#
#
# def get_my_information1():
#     high = 170
#     wight = 60
#     age = 22
#     return (high, wight, age)
#
#
# high, wight, age = get_my_information()
# print(f'我的身高{high}，体重{wight}，年龄{age}')
#
#
# def get_my_information2():
#     high = 170
#     wight = 60
#     age = 22
#     return {'high': 170, 'wight': 60, 'age': 22}
#
#
# high, wight, age = get_my_information()
# print(f'我的身高{high}，体重{wight}，年龄{age}')
#
def add(a, b):
    return a + b


def abc(a, b, c):
    print(b * c)
    return


# print(add(1, 2))
print(abc(1, 2, 3))


def my_print():
    print('hello world')



print(my_print)
# print(id(my_print()))
# # print(my_print())


