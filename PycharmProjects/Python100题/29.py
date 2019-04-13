# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
num = int(input('请输入一个正整数：'))
str1 = str(num)
str2 = str1[:: -1]
num2 = int(str2)
print(f'{num}是{len(str1)}位数，逆序为{num2}')


