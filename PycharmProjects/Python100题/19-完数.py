# 一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
# 找出1000以内的所有完数。
i = 6
while i <= 1000:
    j = 2
    sum = 0
    while j <= i ** 0.5:
        if i % j == 0:
            sum += j
            sum += (i / j)
        j += 1
    if j - 1 == i ** 0.5:
        sum -= (j - 1)
    sum += 1
    if sum == i:
        print(i)
    i += 1