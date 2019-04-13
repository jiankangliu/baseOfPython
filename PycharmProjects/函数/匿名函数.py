# 对元素为字典的列表排序
list1 = [{'name': 'liu', 'age': 18}, {'name': 'li', 'age': 19}]
list1.sort(key=lambda x: x['name'])
print(list1)


def my_add(a, b):
    return a + b
# 定义的函数没有名字就是匿名函数
# 语法格式 lambda 形参1， 形参2，.....: 单行表达式 或者 函数调用
my_fun = lambda :10 + 20
my_add = lambda a, b:a + b
print(my_add(1, 2))

def my_function(start, end):
    my_sum = 0
    while start <= end:
        my_sum += start
        start += 1
    return my_sum

# 1、匿名函数不能使用if语句，while循环，for循环，只能编写单行的表达式，或者函数调用，普通函数都可以
# 2、匿名函数中返回结果不需要使用return，表达式的运行结果就是返回结果，普通函数的返回必须使用return返回
# 3、匿名函数也可以不反回结果。   例如：lambda：print('Hello world!')
# 定义简单的匿名函数


my_function = lambda a, b: a + b

fun1 = lambda **kwargs: kwargs
print(fun1(name='liu', age=18, ph='17802597956'))

fun2 = lambda *args: args
print(fun2('1', 2, 3))
