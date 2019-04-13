def tongji(s):
    num = 0
    alp = 0
    space = 0
    for i in s:
        if i.isalpha():
            alp += 1
        if i.isdigit():
            num += 1
        if i == ' ':
            space += 1

        else:
            continue
    print(f'数字{num}个，字母{alp}个,空格{space}个')


s = 'liu jian kang iiiii123 456'
tongji(s)


