class Washer(object):
    def wash(self):
        print('我会洗衣服')

    def __str__(self):      # 调用类的解释说明， 不需要手动调用。    调用方式   print(对象)
        return '放类的解释说明，放置未来对象的信息'


haier1 = Washer()
haier1.wash()
print(haier1)
