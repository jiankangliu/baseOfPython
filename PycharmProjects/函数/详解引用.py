list1 = [11, 22]            # 列表是可变类型
list2 = list1
list3 = list1.copy()        # list3是重新开辟的存储空间，改变list1，list3不随之改变
list1.append(33)            # 改变list1，list2也随之改变
print(list1)
print(list2)
print(id(list1))
print(id(list2))
print(id(list3))





a = 2       # 整型，浮点型是不可变类型
b = a
a = 3       # 修改a，b不随之改变
