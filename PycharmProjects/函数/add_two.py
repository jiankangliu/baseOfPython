def add_two():
    a = float(input('请输入第一个数：'))
    b = float(input('请输入第二个数：'))
    x = (a + b)
    if x % 1 == 0:
        (x) = int(x)
    return x


print(add_two())
