myList = [1, 2, 3, 4, 5]


def fun(a):
    return a ** 2


result = map(fun, myList)
print(list(result))
print(list(result))

print(id(result))
print('*'*88)


list1 = ["liu", 'jian', 'kang']
def fun1(a):
    return a[0].upper() + a[1:]
result1 = map(fun1, list1)
print(list(result1))

print(list(result))
print(id(result))


