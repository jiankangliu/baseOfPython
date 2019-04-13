# def test1(b):  # 变量b一定是一个局部变量，就看它指向的是谁？可变还是不可变
#     b += b  # += 是直接对b指向的空间进行修改,而不是让b指向一个新的
#     # b = b+b  # xx = xx+yyy 先把=号右边的结果计算出来,然后让b指向这个新的地方,不管原来b指向谁
#                 # 现在b一定指向这个新的地方
a = 0
def test1(b):
    print(id(b))
    b += b
    print(id(b))
    a = b
    print(id(a))
    print(a)

def test2(b):
    print(id(b))
    b = b + b
    a = b
    print(id(b))
    print(id(a))
    print(a)

test1(2)
test2(2)
print('*'*44)
l =[1,2,3,3,4,3,6]
for li in l[:]:
    if li == 3:
        index1 = l.index(3)
        print(index1)
        print(len(l))
        print(l)
        del l[index1]
print(l)
