dict1 = {'name': 'liu', 'age': 18}
a, b = dict1
print(a)                # 存储的是key值
print(b)
print(dict1[a])         # 打印value的值
print(dict1[b])
print(dict1['name'])
for i in dict1.keys():
    print(i)
for i in dict1.values():
    print(i)
for i in dict1.items():
    print(i)

