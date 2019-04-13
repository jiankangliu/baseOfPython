age = int(input("请输入您的年龄："))
while 1 > 0:
    if age <= 0:
        print("输入年龄有误，请重新输入：", end="")
        age = int(input())
        continue
    break
if age < 18:
    print(f"您的年龄是{age}岁，属于童工，不能上班！")
elif age <= 60:
    print(f"您的年龄是{age}岁，可以上班。")
else:
    print(f"您的年龄是{age}岁，属于退休年龄，不能上班！")
