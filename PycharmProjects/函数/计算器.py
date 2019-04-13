a = int(input('请输入第一个数：'))
operation = input('请输入运算符：')
b = int(input('请输入第二个数：'))


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:
    if operation == '+':
        print(add(a, b))
        a = add(a, b)
        operation = input('请输入运算符：')
        b = int(input('请输入第二个数：'))
        continue
    elif operation == '-':
        print(minus(a, b))
        a = minus(a, b)
        operation = input('请输入运算符：')
        b = int(input('请输入第二个数：'))
        continue
    elif operation == '*':
        print(multiply(a, b))
        a = multiply(a, b)
        operation = input('请输入运算符：')
        b = int(input('请输入第二个数：'))
        continue
    elif operation == '/':
        print(divide(a, b))
        a = divide(a, b)
        operation = input('请输入运算符：')
        b = int(input('请输入第二个数：'))
        continue
    else:
        break

