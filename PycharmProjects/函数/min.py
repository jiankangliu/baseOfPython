def min_function():
    a = float(input('请输入第一个数：'))
    b = float(input('请输入第二个数：'))
    min = a if a < b else b
    if min % 1 == 0:
        min = int(min)
    return min


print(min_function())
