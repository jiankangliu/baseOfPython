# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
def number_sum():
    a = input('请输入一个数子a：')
    b = int(input('请输入重复的数字b：'))
    sum = 0
    n = 2
    while b > 0:
        num = int(a * b)
        sum += num
        if b > 1:
            print(f'{a * b}+', end='')
        else:
            print(f'{a}=', end='')
        b -= 1
    print(sum)


number_sum()