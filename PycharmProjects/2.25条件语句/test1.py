# day = int(input("请输入星期几："))
# while True:
#     if day != 1 and day != 2 and day != 3 and day != 4 and day != 5 and day != 6 and day != 7:
#         print("输入错误，请重新输入：", end="")
#         day = int(input())
#         continue
#     break
# if day == 1:
#     print("今天是周一")
# elif day == 2:
#     print("今天是周二")
# elif day == 3:
#     print("今天是周三")
# elif day == 4:
#     print("今天是周四")
# elif day == 5:
#     print("今天是周五")
# else:
#     print("今天是周末")
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
# num3 = int(input("请输入第三个数字："))
# sum = num1 + num2 + num3
# if sum > 100000:
#     print("您输入的三个数的和忒大了")
# elif sum > 10000:
#     print("您输入的三个数的和挺大")
# elif sum > 1000:
#     print("您输入的三个数的和有点大")
# elif sum > 100:
#     print("您输入的三个数的和不算大")
# else:
#     print("您输入的三个数的和忒小了")
#
# height = int(input("请输入身高（厘米）："))
# weight = int(input("请输入体重（千克）："))
# IBM = weight/((height/100)*(height/100))
# if IBM < 18.5:
#     print(f"IBM{IBM}过轻")
# elif IBM < 25:
#     print(f"IBM{IBM}正常")
# elif IBM < 28:
#     print(f"IBM{IBM}过重")
# elif IBM < 32:
#     print(f"IBM{IBM}肥胖")
# else:
#     print(f"IBM{IBM}严重肥胖")
# name = input("请输入姓名：")
# sex = input("请输入性别：")
# age = int(input("请输入年龄："))
# workPlace = input("请输入工作单位：")
# workerID = int(input("请输入工号："))
# phone = input("请输入联系方式：")
# print(f"您的姓名是：{name}\n性别：{sex}\n年龄是：{age}\n工作单位是：{workPlace}\n工号是：%09d\n联系方式：{phone}" % workerID)

# year = int(input("请输入年份："))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f"{year}是闰年。")
# else:
#     print(f"{year}不是闰年。")
# 定义字符串变量temp1
# temp1 = "hello python"
# # 接收用户的输入
# temp2 = input("请输入：")
# # 定义数字变量temp3
# temp3 = 333
# # 定义字符串变量temp4
# temp4 = int("333")
# # 求和
# temp5 = temp3 + temp4
# # 判断temp5是否等于666
# if temp5 == 666:
#     print("%s + %s = %s, 挺溜啊" % (temp3, temp4, temp5))
# if temp5 != 666:
#     print("一点儿也bu溜")
# print("您刚刚输入的是:%d" % temp2)
while True:
    num1 = input("请输入第一个数字：")
    while True:
        if not num1.isdigit():
            num1 = input("输入错误，请重新输入第一个数字：")
            continue
        break
    operate = input("请输入运算符(q退出)：")
    while True:
        if operate != '+' and operate != '-' and operate != '*' and operate != '/' and operate != '**' and operate != '//'and operate != '%' and operate != 'q':
            operate = input("运算符错误，请重新输入运算符（q退出）：")
            continue
        break
    if operate == 'q':
        print("退出程序！")
        break
    num2 = input("请输入第二个数字：")
    while True:
        if not num2.isdigit():
            num2 = input("输入错误，请重新输入第二个数字：")
            continue
        break
    num1 = int(num1)
    num2 = int(num2)
    if operate == "+":
        print(f"{num1}{operate}{num2}={num1+num2}")
    elif operate == "-":
        print(f"{num1}{operate}{num2}={num1-num2}")
    elif operate == "*":
        print(f"{num1}{operate}{num2}={num1*num2}")
    elif operate == "/":
        print(f"{num1}{operate}{num2}={num1/num2}")
    elif operate == "**":
        print(f"{num1}{operate}{num2}={num1**num2}")
    elif operate == '//':
        print(f"{num1}{operate}{num2}={num1//num2}")
    elif operate == '%':
        print(f"{num1}{operate}{num2}={num1%num2}")
    else:
        print("输入错误。")
