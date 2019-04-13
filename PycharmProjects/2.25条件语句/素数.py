sum = 0
for i in range(3, 9999999999999999999999999999):
    n = 2
    while n < i:
        if i % n == 0:
            break
        n += 1
    if n == i:
        sum += 1
        print(f'{i}是素数,第{sum}个')

