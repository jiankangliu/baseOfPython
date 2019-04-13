class Master(object):
    def __init__(self):
        super().__init__()
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
    def __init__(self):     # 子类重写父类同名方法
        self.kongfu = '原创配方'
        self.money = 9999999999

    def make_cake(self):
        self.__init__()
        print(f'使用{self.kongfu}制作煎饼')

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)


class Student(Prentice):
    pass


liu = Prentice()
print(liu.kongfu)
liu.make_master_cake()
liu.make_school_cake()
liu.make_cake()
zhang = Student()
zhang.make_school_cake()
zhang.make_master_cake()
zhang.make_cake()
print(Student.mro())        # 检查继承类，返回一个列表
print(Student.__mro__)      # 检查继承类，返回一个元组





