def add_there():
    a = float(input('请输入第一个数：'))
    b = float(input('请输入第二个数：'))
    c = float(input('请输入第三个数：'))
    x = (a + b + c)
    if x % 1 == 0:
        (x) = int(x)
    return x


print(add_there())