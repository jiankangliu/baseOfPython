class Washer():
    def print_info(self):
 # 类⾥⾯获取实例属性
        print(f'haier1洗⾐机的宽度是{self.width}')
        print(f'haier1洗⾐机的⾼度是{self.height}')
# 创建对象
haier1 = Washer()
# 添加实例属性
haier1.width = 500
haier1.height = 800
haier1.print_info()
