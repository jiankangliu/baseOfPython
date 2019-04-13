def prime_num(m, n):
    while m <= n:
        i = 2
        while i < m:
            if m % i == 0:
                break
            i += 1
        if i == m and m > 2:
            print(f'{m}是素数')
        m += 1


m = int(input('请输入素数下限：'))
n = int(input('请输入素数上线：'))
prime_num(m, n)
