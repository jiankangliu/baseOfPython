class Washer(object):
    def __init__(self):     # __init__()初始化函数， 创建完对象后系统自动调用
        # 设置对象初始化属性用的
        # 宽度400     高度 600
        self.width = 400
        self.height = 600
    def info_print(self):
        print(f'宽度是{self.width},高度{self.height}')

# __xx__:构造函数，不需要程序员调用，系统自动调用
haier = Washer()
haier.info_print()
