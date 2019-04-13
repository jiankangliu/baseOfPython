try:
    print(1)
except Exception as e:
    print(e)
else:
    print('没有异常真开心')
finally:
    print('无论是否有异常都执行，一般都是都是书写文件关闭的代码')
