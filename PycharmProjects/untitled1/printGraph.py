# 第一行一个*，第二行两个*........  共十行
# 打印乘法口诀
n = 1
while n <= 10:
    n1 = n
    while n1:
        print("*", end = "")
        n1 -= 1
    print()
    n += 1

n2 = 1
n3 = 1
while n2 < 10:
    while n3 <= n2:
        print(f"{n3}*{n2}={n3*n2}",end="\t")
        n3 += 1
    print()
    n2 += 1
    n3 = 1

n4 = 0
while n4 < 40:
    n5 = 0
    if n4 < 20:
        while n5 < n4:
            print(' ',end='')
            n5 += 1
        print('*')
    else:
        n5 = 39 - n4
        while n5:
            print(' ',end='')
            n5 -= 1
        print('*')
    n4 += 1

