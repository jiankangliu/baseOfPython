list1 = ['name', 'age', 'sex']
list2 = ['Tom', 100, '男']
dict1 = {list1[i]: list2[i] for i in range(3)}
dict3 = {'id': '110', 'class': 'math'}
print(dict3)
print(dict1)


list3 = [1, 2, 3]           # 两个列表合并成字典
list4 = [4, 5, 6]
print(dict(zip(list3, list4)))


counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
dict2 = {i: j for i, j in counts.items() if j >= 200}
print(dict2)


list3 = [1, 1, 4]
set1 = {i ** 2 for i in list3}
print(set1)      # 集合有去重功能
