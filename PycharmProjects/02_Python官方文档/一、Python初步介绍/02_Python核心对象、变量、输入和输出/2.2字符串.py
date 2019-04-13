str1="hello world"
str2="liu jiankang"
print(str1[0:2])
print(str1[-3:-1])
print(str1[:])       #str[m:n]，m、你默认为边界
print(str1[:-1])
print(str1*2)
print(str1+str2)
print(str1.__len__())
print(len(str2))
print(str1.upper())
print(str1.lower())
print(str1.count("l"))  #统计str1中子串为l的个数
print(str1.capitalize())#str1首字母大写
print(str1.title())     #str1中每个单词首字母大写
print(str1.rstrip())    #移除字符串末尾的空白字符

#2.2.10input函数
#town=input("Enter the name of your city")
#Python执行到这个语句时，将显示”Enter the name of your city“,同时程序终止。
# 在用户键入了他的城市名并确定后，变量town才创建
#例4解析姓名
# fullname=input("Enter a full name")
# n=fullname.rfind(" ")       #rfind()函数从右向左搜索字符串，返回正向索引位置
# print("Last name",fullname[n+1:])
# print("First name",fullname[:n])

#2.2.11 int、float、eval和str函数
print(int("22"))
print(int(23.5))
print(float("22.5"))
print(eval("22*3"))

#2.2.13行延续
quotation="Well written code is its own best documentation."
#上行语句可以写成一下形式。通过在行尾使用\分割成两个或者更多行显示
quotation="Well written code "+\
    "is its own best documentation"
#也可以写成如下形式
quotation=("well written code is "+
"its own best cocumentation")

#2.2.14索引和切片越界。
#Pyton不允许单个字符的索引越界，但是在切片中可以允许索引越界。
str1="Python"
#str1[10]   单个字符越界是不允许的
print(str1[0:11])   #切片越界允许


