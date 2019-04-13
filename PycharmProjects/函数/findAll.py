def find_all():
    li = []
    s = input('请输入字符串：')
    s1 = input('请输入子串：')
    c = s.count(s1)
    m = 0
    while c:
        index1 = s.index(s1, m, len(s))
        m = index1 + 1
        li.append(index1)
        c -= 1
    tu = tuple(li)
    print(tu)
    return 0


find_all()


