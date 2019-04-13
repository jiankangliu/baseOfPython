class A(object):
    def __init__(self):
        self.num = 1
    def __str__(self):
        return 'haha'


class B(A):     # B类继承A类
    pass


b = B()
print(b)
print(b.num)
