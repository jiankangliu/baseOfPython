# list1 = [1, 2, 3, 4, 0]
# sum = 0
# for i, element1 in enumerate(list1):
#     for j, element2 in enumerate(list1):
#         for k, element3 in enumerate(list1):
#             if i != j and i != k and j != k and list1[i] != 0:
#                 sum += 1
#                 print(list1[i] * 100 + list1[j] * 10 + list1[k])
# print(f'共{sum}个组合')


def free_combination(list1, m):
    # 递归函数
    global sum, list2      # 全局变量
    if m == 1:      # 递归出口
        for i, element in enumerate(list1):
            # enumerate()函数：返回下标（索引）和值
            if i in list2:
                # 因为已经加入组合的数字不能重复加入，所以跳出循环
                continue
            list2.append(i)         # 未使用的数字可以加入组合
            if n == len(list2):     # 如果组合的长度符合要求，则符合规则的组合数量+1
                sum += 1
                for j in list2:     # 打印
                    print(list1[j], end='\t')
            list2.pop()     # 删除最后一个元素。 （pop()返回删除的值，我们这里用不到）
            print()     # 换行
        return 0
    else:
        for i, element in enumerate(list1):
            if i in list2:
                # 因为已经加入组合的数字不能重复加入，所以跳出循环
                continue
            list2.append(i)     # 未使用的数字可以加入组合
            free_combination(list1, m - 1)  # 递归调用
            list2.pop()     # 删除最后一个元素。 （pop()返回删除的值，我们这里用不到）


list1 = eval(input('请输入自由组合的序列(形如[1, 2, 3，...])：'))
n = int(input('请输入自由组合的长度：'))
m = n
sum = 0
list2 = list()      # 建立一个空列表，存储已经加入组合的下标值
free_combination(list1, m)
print(f'{list1}{n}个数的排列共有{sum}种排列组合')


