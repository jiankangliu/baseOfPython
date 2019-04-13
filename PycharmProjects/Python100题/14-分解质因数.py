# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

num = int(input("请输入要分解的合数："))
list1 = list()
while num != 1:
    m = 2
    while m <= num:
        p = 2
        while p < m:
            if m % p == 0:
                break
            p += 1
        if p == m:
            if num % m == 0:
                num /= m
                list1.append(m)
        m += 1
list1.sort()
print(list1)


