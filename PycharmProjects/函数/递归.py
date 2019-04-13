# 递归打印乘法口诀
def recurtion(a):
    if a == 9:
        n = 1
        while n < 10:
            print(f'{n}*{a}={n*a}', end='\t')
            n += 1
        return 00
    else:
        n = 1
        while n <= a:
            print(f'{n}*{a}={n*a}', end='\t')
            n += 1
        print()
        recurtion(a+1)
        return 00


recurtion(1)
print()


def reculation2(m):
    if m == 1:
        return 1
    else:
        return m * reculation2(m - 1)


print(reculation2(5))


def abc(num):
    if num == 1:
        return 1
    else:
        return num * abc(num - 1)


print(abc(10))

