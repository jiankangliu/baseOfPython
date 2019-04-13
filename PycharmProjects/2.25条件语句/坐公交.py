money = int(input("请输入钱(1代表有钱，0代表没钱)："))
while 1 > 0:
    if money != 0 and money != 1:
        print("钱数输入错误请重新输入：", end="")
        money = int(input())
        continue
    break
if money == 1:
    print("欢迎乘车！")
    seat = int(input("请输入是否有座位（1代表有座位，0代表没座位）:"))
    while 1 > 0:
        if seat != 0 and seat != 1:
            print("座位状态输入错误，请重新输入：", end="")
            seat = int(input())
            continue
        break
    if seat == 1:
        print("请坐下！")
    elif seat == 0:
        print("无座位，请等待座位。")
else:
    print("没钱不能坐公交车！")
