class Dog(object):
    __tooth = 10        # 私有属性

    @classmethod        # 类方法
    def get_tooth(cls): # 类方法
        return cls.__tooth


wangcai = Dog()
result = wangcai.get_tooth()


