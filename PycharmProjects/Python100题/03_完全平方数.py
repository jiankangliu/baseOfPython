# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
def wanquanpinggang():
    i = 1
    while True:
        m = 1
        n = 1
        while m ** 2 <= i + 100:
            if m ** 2 == i + 100:
                while n ** 2 <= i + 168:
                    if n ** 2 == i + 168:
                        print(f'该数为{i}')
                        return i
                    n += 1
            m += 1
        i += 1


wanquanpinggang()

