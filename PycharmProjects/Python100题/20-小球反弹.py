# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
# 第10次落地时，共经过多少米？第10次反弹多高？
bound = 0
high = 100
path = 100
n = int(input('请输入第几次落地：'))
if n == 1:
    path = 100
    bound = high / 2
else:
    m = n
    while m > 1:
        path += high
        high /= 2
        bound = high / 2
        m -= 1
print(f'路程{path}')
print(f'第{n}次反弹{bound}米')