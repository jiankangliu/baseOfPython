class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼配方]'

    def make_cake(self):
        print(f'师傅运用{self.kongfu}')


class Prentice(Master):
    pass

daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()