def max_function():
    a = float(input('请输入第一个数字：'))
    b = float(input('请输入第二个数字：'))
    max = a if a > b else b
    if max % 1 == 0:
        max = int(max)
    return max


print(max_function())
