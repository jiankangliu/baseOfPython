import operator
a = 1
b = 2
print(operator.lt(a, b))        # lt()函数，a>b
print(operator.le(a, b))        # le()函数，a>=b
print(operator.eq(a, b))        # eq()函数，a==b
print(operator.gt(a, b))        # gt()函数，a>b
print(operator.ge(a, b))        # ge()函数，a>=b

alphabet = 'lsjfoifjafjz'
print(max(alphabet))
print(min(alphabet))

# del()函数有两种形式
# 一种是del加空格， 另一种是del()
a = ['a', 'b']
b = ['c', 'd']
del a           # 删除a数组
# print(a)
del(b[1])       # 删除b数组下标为1的元素
print(b)

