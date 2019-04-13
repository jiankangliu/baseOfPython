class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼配方]'

    def make_cake(self):
        print(f'师傅运用{self.kongfu}')


class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
        self.peifang = '辣椒'

    def make_cake(self):
        print(f'学校运用{self.kongfu}制作')


class Prentice(School, Master):     # 同名属性，同名方法，默认继承第一个
    pass


class Student(Prentice):
    pass


daqiu = Prentice()
print(daqiu.peifang)
print(daqiu.kongfu)
daqiu.make_cake()
s = Student()
s.make_cake()
print(s.kongfu)
