list1 = list()
list1 = input().split()
print(list1)
for i in list1:
    list1[list1.index(i)] = int(i)
print(list1)