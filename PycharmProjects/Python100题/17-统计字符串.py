# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
def statistics_str():
    num = 0
    alp = 0
    space = 0
    other = 0
    str = input('Enter a string:')
    for i in str:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            alp += 1
        elif i == ' ':
            space += 1
        else:
            other += 1
    print(f'数字{num}个，字母{alp}个，空格{space}个，其它字符{other}个')


statistics_str()