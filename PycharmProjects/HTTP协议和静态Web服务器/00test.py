num = 3                         # 第一步    num = 3


def fang(fun):                  # 第二步
    print("fang"*7)             # 第九步

    def inner1():               # 第十步
        global num
        num *= num              # 第十三步          num = 9
        fun()                   # 第十四步          fun()  等价于执行  inner2()
        print('fang', num)      # 第十九步          打印  fang 18
    return inner1               # 第十一步


def add(fun):                   # 第三步
    print("add"*9)              # 第六步

    def inner2():               # 第七步
        global num
        num += num              # 第十五步          num = 18
        fun()                   # 第十六步          fun() 等价于执行 func()
        print('add', num)       # 第十八步          打印  add 18
    return inner2               # 第八步


def func():                     # 第四步
    global num
    print('func', num)          # 第十七步          打印  func 18


# func = add(func)
func = fang(add(func))          # 第五步
func()                          # 十二步


