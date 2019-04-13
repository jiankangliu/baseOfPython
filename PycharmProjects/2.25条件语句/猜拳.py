import random
while 1 > 0:
    player = input("请输入你猜拳（0代表石头，1代表剪子，2代表布，3退出程序）：")
    while 1 > 0:
        if player != 0 and player != 1 and player != 2 and player != 3:
            print("输入错误，请重新输入：", end="")
            player = input()
            continue
        break
    machine = random.randint(0, 2)
    if player == 0:
        if machine == 0:
            print("平手")
        elif machine == 1:
            print("恭喜胜利！")
        else:
            print("失败，不要气馁！")

    elif player == 1:
        if machine == 0:
            print("失败，不要气馁！")
        elif machine == 1:
            print("平手")
        else:
            print("恭喜胜利！")

    elif player == 2:
        if machine == 0:
            print("恭喜胜利！")
        elif machine == 1:
            print("失败，不要气馁！")
        else:
            print("平手")

    else:
        print("退出游戏。")
        break
