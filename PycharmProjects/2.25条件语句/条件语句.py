age = int(input("请输入年龄："))
while 1 > 0:
    if age <= 0:
        print("年龄有误，请重新输入：", end='')
        age = int(input())
        continue
    if age < 18:
        print(f"您的年龄是{age}岁，未成年，关闭系统！")
        break
    else:
        print(f"您的年龄是{age}岁，可以上网。")
        break
