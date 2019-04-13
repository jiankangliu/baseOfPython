# 判断101-200之间有多少个素数，并输出所有素数。


def prime_num(m, n):
    while m <= n:
        p = 2
        while p < m:
            if m % p == 0:
                break
            p += 1
        if p == m:
            print(m)
        m += 1


m = int(input("请输入下限："))
n = int(input('请输入上限'))
prime_num(m, n)
