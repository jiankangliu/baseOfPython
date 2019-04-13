def panduansanjao():
    print('请输入三角形的三条边长：')
    a = float(input())
    b = float(input())
    c = float(input())
    if (a + b) > c and (a + c) > b and (b + c) > a:
        print('是三角形')
        return 0
    else:
        print('不是三角形')
        return 0


print(panduansanjao())