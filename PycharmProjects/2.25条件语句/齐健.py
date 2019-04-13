while True:
    start = input("请输入要进行的操作【q】退出程序【w】开始程序：")
    if start == "q":
        print("退出程序，计算结束")
        break
    elif start == "w":
        print("计算开始")
        num1 = int(input("请输入第一个数字："))
        a = input("请输入运算符 + - * / ：")
        num2 = int(input("请输入第二个数字："))
        if a == "+":
            print(f"{num1}+{num2}={num1+num2}")
        elif a == "-":
            print(f"{num1}-{num2}={num1-num2}")
        elif a == "*":
            print(f"{num1}*{num2}={num1*num2}")
        elif a == "/":
            print(f"{num1}/{num2}={num1/num2}")
        else:
            print("输入错误，请重新输入")
