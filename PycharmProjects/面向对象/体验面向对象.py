class Washer(object):   # 默认继承object类
    def wash(self):     # self 表示将来的对象
        print('我会洗衣服')
        print(self)
    def info_print(self):
        print(f'这台洗衣机的宽度是：{self.width}')        # 类内部访问属性

# self 和 haier 是同一个对象
haier = Washer()
haier.wash()
haier.high = 120        # 类外部定义属性值
haier.width = 130       # 类外部定义属性值
print(haier)
print(haier.width)      # 类外部访问属性名
print(haier.high)
print(haier.info_print())   # 类内部访问实例属性

