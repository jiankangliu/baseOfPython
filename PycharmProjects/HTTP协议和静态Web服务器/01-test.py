num1 = 3
def chengfa(func):             # func -->  inner1
    print('chengfa正在执行')
    def inner2():
        global num1
        num1 = num1 * num1            #  num1 = 9
        func()                #  inner1()
        return num1           #   18
    return inner2
def sum(func):
    print('sum正在被执行')
    def inner1():
        global num1
        num1 = num1 + num1          # 18
        func()
        return num1
    return inner1
@chengfa
@sum               #   inner1 = sum(number)    inner2 = chengfa(inner1)   ----->  inner2----> number
def number():
    pass
if __name__ == '__main__':
    a = number()  #  inner2
    print(a)
