list1 = ['a', 'b']
for i in enumerate(list1):
    print(i)
fun1 = lambda a: a ** 2
list1 = [1, 2, 3]
result = map(fun1, list1)
print(list(result))
fun2 = lambda *a: a
print(fun2(1, 2, 3))

# map()
# reduce()
# filter()



