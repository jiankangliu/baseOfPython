import random
teacher = list(input('请输入老师：'))
num = int(input('请输入办公室：'))
l = list()
while num > 0:
    list1 = list()
    l.append(list1)
    num -= 1

def average_office(teacher, l):
    m = 0
    while True:
        if len(teacher) == 0:
            break
        t = random.choice(teacher)
        teacher.remove(t)
        l[m].append(t)
        m += 1
        m %= len(l)
    for office in l:
        print(f'{l.index(office)}办公室，有{len(office)}人{office}')
    return


average_office(teacher, l)