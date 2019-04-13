"""
房子 -- 初始化数据：家居列表[ ]，使用面积，生于面积，地理位置
家居 -- 初始化数据：作用/名字，占地面积
"""
class House(object):
    def __init__(self, area, address):
        self.jia_list = []
        self.area = area
        self.free_area = area
        self.address = address

    def __str__(self):
        return f'房子位于{self.address},使用面积{self.area},剩余面积{self.free_area},家居有{self.jia_list}'

    def add_jiaju(self, x):
        if self.free_area >= x.area:
            self.jia_list.append(x.name)
            self.free_area -= x.area
        else:
            return 0


class Jiaju(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'家居名字{self.name}，占地面积{self.area}'


house1 = House(500, '意大利农场')
bed1 = Jiaju('床', 100)
print(house1)
print(bed1)
house1.add_jiaju(bed1)
print(house1)

