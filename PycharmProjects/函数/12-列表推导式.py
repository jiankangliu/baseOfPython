# # [1, 2, 3, 4... 9]
#
# # while
# # list1 = []
# # i = 1
# # while i <= 9:
# #     # print(i)
# #     list1.append(i)
# #     i += 1
# #
# # print(list1)
#
# # for
# # list1 = []
# # for i in range(1, 10):
# #     # print(i)
# #     list1.append(i)
# #
# # print(list1)
#
# # [返回值 for i in range(1, 10)]
#
# # Pythonic
#
# list2 = [i for i in range(1, 10)]
# print(list2)
#
# list3 = [j for j in range(1, 11) if j % 2 == 0]
# print(list3)
#
# list4 = [(i, j) for i in range(1, 3) for j in range(3)]
# print(list4)
# #list5 = [(j, i) for i in range(1, 3) for j in range(3)]True
# #print(list5)
# print('_'*33)
# list6 = [2, 1, 4]
# list7 = list6.sort()
# print(list7)
list1 = [3, 9, 6, 1]
list2 = list1
list3 = [i for i in list1]
list1.sort()
print(list1)
print(list2)
print(list3)
print(id(list1))
print(id(list2))
print(id(list3))
a = 1
b = a
print(a)
print(id(a))
print(id(b))
a = 2
print(a)
print(id(a))
print('*'*88)
list4 = [0, 1, 2, 3, 4]
print(id(list4))
list4[1] = 9
print(list4)
print(id(list4))
