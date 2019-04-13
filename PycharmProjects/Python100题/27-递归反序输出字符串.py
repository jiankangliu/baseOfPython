def recursion(s):
    if len(s) == 1:
        print(s, end='')
        return 0
    else:
        print(s[len(s) - 1], end='')
        s1 = s[:-1]
        recursion(s1)


recursion('liu')
