# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
list1 = []
num1 = int(input('请输入第一个数：'))
list1.append(num1)
num2 = int(input('请输入第二个数：'))
list1.append(num2)
num3 = int(input('请输入第三个数：'))
list1.append(num3)
list1.sort()            # 对list1进行排序
for i in list1:
    print(i)


