myStr = "LIUjiankang heimachangxu"
str = 'a'
print(myStr.find('ian', 0, 7))              # find()函数
print(myStr.find('i', 2, 9))                # find('索引目标', index1, index2)     在index1至index2上索引，不包括index2
print(myStr.index(str, 0, len(myStr)))      # index('索引目标', index1, index2)    在index1至index2上索引，不包括index2
                                            # 用法与find()相同，找不到目标时报一个异常
print(myStr.count('a', 0, len(myStr)))      # 统计索引目标出现次数
print(myStr.replace("i", "a", myStr.count('i')))           # ######replace()只是一个临时替换
print(myStr)
print(myStr.split('a', 2))                  # 用a分割，分割两次
print(myStr.capitalize())                   # 首字母大写
print(myStr.title())                        # 每个首字母都大写
print(myStr.startswith("liu"))              # 检查字符串是否以目标字符串开头，返回True或者False
print(myStr.endswith("xu"))                 # 检查字符串是否以目标字符串结尾，返回True或者False
print(myStr.lower())                        # 字符串中大写变小写
print(myStr.upper())                        # 字符串中小写变大写
print(myStr.lower().upper())                # 字符串中大写变小写
print(myStr.ljust(30))                      # 左对齐，定义长度
print(myStr.rjust(30))                      # 右对齐
myStr1 = '    liu     '
print(myStr1.lstrip())  # 消去左边的空格
print(myStr1)
print(myStr1.rstrip())  # 消去右边的空格
print(myStr1.strip())   # 消去两边的空格
name = "abcdefghijklm"
print(name.rfind('k'))  # 从右边开始查找，返回的结果与find（）相同
print(name.rindex('klm'))   # 从右边开始找，返回结果与index（）相同
print(name.index('klm'))
str = 'liualiefalsjfialsdfi'
print(str.partition('a'))   # 从左到右将str用参数字符串分为三部分
print(str.rpartition('a'))
str2 = 'liujiankang\nliu'
print(str2.splitlines())    # 返回一个以各行为元素的列表
str3 = 'liu'
print(str3.isalpha())       # 判断所有字符是否都是字母
str4 = '123'
print(str4.isdigit())       # 判断所有的字符是否都是数字
str5 = 'liu123'
print(str5.isalnum())       # 判断所有字符是否都是数字或者字母
str6 = '     '
print(str6.isspace())       # 判断所有字符是否都是空格
li = ['liu', 'jian', 'kang']
space = ' '
space2 = '_'
print(space.join(li))       # li每个元素后面插入一个space元素
print(space2.join(li))
example = 'liu jian kang hei\tma\nliu'
print(example.rsplit())         # 默认以' '和 '\t'和'\n'为分隔符
print(example.split('\t'))
nameList = ['zhao', 'qian', 'sun', 'li']
exampleList = [1, 'liu']        # Python列表中的元素可以是不同的类型
print(nameList[0])
print(nameList[1])
print(nameList[2])

# 列表的遍历
for aaa in nameList:        # 使用for循环遍历
    print(aaa)

length = len(nameList)
m = 0
while m < length:           # 使用while循环
    print(nameList[m])
    m += 1

list2 = [1, 2, 'liu', 'zh']
list3 = ['panda', 'monkey']
list2.append('li')      # 添加元素
print(list2)
list2.append(list3)
print(list2)
list2.extend(list3)     # 可将一个集合中的元素逐一添加至列表中
print(list2)
list2.insert(2, 'ha')   # 在特定位置添加元素
print(list2)
list2[2] = 'xi'         # 通过下标修改元素
print(list2)

# 查找元素in 、 not in 、 index 、 count
# in 返回True或者False
# not in 返回True或者False
list4 = ['dog', 'cat', 'pig', 'dog']
print('dog' in list4)
print('dog' not in list4)
print(list4.index('cat', 0, 2))     # index()方法，在的话返回下标，不再的话返回一个异常
print(list4.count('dog'))           # 返回列表中出现的次数

# 删除元素，del 、 pop 、 remove
# del根据下表进行删除
# pop删除最后一个元素
# remove根据元素的值进行删除
list5 = [1, 2, 3, 4, 'liu', 'li']
del list5[2]
print(list5)
list5.pop()
print(list5)
list5.remove(4)
print(list5)


# 排序sort 、 reverse
list6 = [1, 2, 8, 6, 0, 3]
list6.sort()            # sort()，排序，默认从小到大
print(list6)
list6.reverse()         # reverse()，倒置
print(list6)


# 列表的嵌套：一个列表中的元素是列表
import random
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]
n = 0
while n < len(names):
    m = random.randint(0, 2)
    offices[m].append(names[n])
    n += 1
q = 1
for office in offices:
    print(f"办公室{q}有{len(office)}人", end='')
    print(office)


# tuple元组 ， 元组的元素不能修改
uTuple = (1, 2, 3, 2)
print(uTuple)
print(uTuple[0])        # 访问元组中的元素
print(uTuple.index(3))  # 定位元素 3 的位置
print(uTuple.count(1))  # 统计元组中元素 1 出现的次数

info = {'name': 'Tom', 'ID': 100, 'address': '黑马程序'}
print(info['name'])
info['name'] = 'Liu'        # 修改元素的值
print(info['name'])
print(info['name'])         # 查看元素
print(info.get('ID'))       # 查看元素
print(info.get('phone', 17802597956))       # 若 info 不存在'phone'键，就返回默认值17802597956
info['name'] = 'Liu'
print(info['name'])         # 修改元素
info['class'] = 'python'    # 添加元素，如果 'class' 不再info中则添加词元素
del info['name']            # 删除元素
print(info)
del info                    # 删除整个字典
info = {'name': 'Tom', 'age': 18, 'class': 'python'}
print(len(info))            # 输出字典长度
print(info.keys())          # 返回一个包含字典所有KEY的列表
print(info.values())        # 返回一个包含所有value的列表
print(info.items())         # 返回一个包含所有元组（键，值）的列表
for key in info.keys():     # 遍历关键词
    print(key, end='\t')
for value in info.values():     # 遍历值
    print(value, end='\t')
for item in info.items():       # 遍历字典的项
    print(item, end='\t')
print()
for key, value in info.items():     # 遍历字典的键值对
    print(f'{key}:{value}')

for i, value in enumerate(info):
    print(f"{i}:{value}")

# 创建无序字典
my_dict = dict()
my_dict['one'] = 1
my_dict['there'] = 3
my_dict['two'] = 2
my_dict['four'] = 4
print(my_dict)
