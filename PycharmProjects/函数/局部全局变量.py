a = 11


def add():
    global a
    a = 22
    print(a)
    return 0


add()
print(a)



