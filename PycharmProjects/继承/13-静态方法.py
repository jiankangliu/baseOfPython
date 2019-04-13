class Dog(object):
    # def xx(self):
    @staticmethod       # 静态方法，不创建实例对象，节省内存空间
    def info_print():
        print('这是一个打印信息的函数 -- 小红注意： 我喜欢你~~~~')


wangcai = Dog()
wangcai.info_print()




