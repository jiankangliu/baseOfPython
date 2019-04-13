import functools
list1 = [1, 2, 3, 4, 5]


def fun(a, b):
    return a*b


reslut = functools.reduce(fun, list1)
a = reslut
print(a)
print(reslut)
print(id(a))
print(id(reslut))
a = 8
print(id(a))


list2 = [2, 44, 6567, 89]


def fun1(a, b):
    return a if a > b else b


print(functools.reduce(fun1, list2))
