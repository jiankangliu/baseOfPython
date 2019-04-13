# eval()函数将表达式转换为原本类型
s = "lsjfoisd"
l=list(s)
t=tuple(s)
print(l)
print(t)
a=input("数字1：")
b=input("数字2：")
print(eval(a)+eval(b))
username=input("请输入您的用户名：")
age=int(input("请输入您的年龄："))          #强制转型
print(type(age))
password=input("请输入您的密码：")
print(type(password))
'''
    input("提示信息")
    age=int(input("提示信息"))          强制转型为int类型
'''