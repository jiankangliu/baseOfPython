"""
智能烤地瓜 自己烤自己 ——地瓜类——
方法：烤cook_time:0-3生的     3-5半生   5-8刚刚好  >8糊了
属性：烤的状态   烤的时间 ---添加佐料---
"""
class Digua(object):
    def __init__(self):
        self.cook_state = '生的'
        self.cook_time = 0
        self.tiaoliao = []

    def cook(self, time):
        # 改变地瓜状态
        # 烤地瓜的总时间 = 之前烤的时间 + time
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生'
        elif 5 <= self.cook_time  < 8:
            self.cook_state = '刚刚好'
        else:
            self.cook_state = '糊了'


    def add_liao(self, x):
        # 列表追加数据
        self.tiaoliao.append(x)


    def __str__(self):
        return f'这个地瓜烤的时间时{self.cook_time},状态时是{self.cook_state},添加的调料有{self.tiaoliao}'


digua1 = Digua()
digua1.cook(1)
print(digua1)
digua1.cook(5)
digua1.add_liao('糖')
digua1.add_liao('辣椒')
print(digua1)
