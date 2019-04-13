"""
 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
sum = 0
n = 18
num1, num2, num3, num4 = 1, 2, 2, 3
sum += num3/num1
sum += num4/num2
while n > 0:
    num1 = num1 + num2
    num1, num2 = num2, num1
    num3 = num3 + num4
    num3, num4 = num4, num3
    sum += num3/num1
    n -= 1
print(sum)
