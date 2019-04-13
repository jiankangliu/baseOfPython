# 题目：对10个数进行排序题目：对10个数进行排序
list1 = list()
i = 1
while i < 11:
    list1.append(int(input(f'请输入第{i}个数字：')))
    i += 1
for j in range(1, 10):
    k = j - 1
    while True:
        if list1[j] < list1[k] and k >= 0:
            temp = list1[j]
            list1[j] = list1[k]
            list1[k] = temp
            j = k
            k -= 1
        else:
            break
print(list1)
