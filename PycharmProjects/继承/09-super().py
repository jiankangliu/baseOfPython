class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'师傅运用{self.kongfu}制作煎饼果子')

    # def xx(self):
    #     print('aaaaa')


# 黑马学校类
class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'学校运用{self.kongfu}制作煎饼果子')
        # 再用super调用这个类的父类方法
        # super(School, self).__init__()
        # super(School, self).make_cake()

        super().__init__()
        super().make_cake()


# 如果一个子类继承了多个父类，如果有同名方法或属性，默认继承书写在括号里面第一个父类的同名属性和方法
class Prentice(School):
    def __init__(self):
        self.kongfu = '[原创煎饼果子配方]'

    def make_cake(self):
        # 做自己的初始化调用: 下面已经执行过其他父类的初始化，这里需要还原成自己
        self.__init__()
        print(f'大秋运用{self.kongfu}制作煎饼果子')

    def make_super_cake(self):
        # 调用父类方法
        # super(自己类的类名, self).目标函数() -- 化简写法就是去掉所有参数，默认它自己可以填充目标参数
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        super().__init__()
        super().make_cake()




# laowang = Master()
# print(laowang.kongfu)
# laowang.make_cake()

daqiu = Prentice()
daqiu.make_super_cake()


# 有个顾客想一次性吃所有
