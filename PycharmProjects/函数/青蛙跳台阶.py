n = 5
def qingwa(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return qingwa(n - 1) + qingwa(n - 2)

print(qingwa(3))
