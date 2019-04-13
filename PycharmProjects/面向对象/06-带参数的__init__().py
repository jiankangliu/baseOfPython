class Washer(object):
    def __init__(self, a, b):   # 带参数的__init__(),可以让类更加灵活，能创建出不同属性值的对象
        self.width = a
        self.height = b
    def info_print(self):
        print(f'宽度是{self.width},高度是{self.height}')


haier1 = Washer(100, 200)   # 若__init__带形参，创建对象时要带参数，否则报错
haier1.info_print()
