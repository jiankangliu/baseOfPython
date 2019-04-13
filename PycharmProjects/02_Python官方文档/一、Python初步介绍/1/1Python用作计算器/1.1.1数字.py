print(2+2)
number=(50-5*6)/4   #"/"用作整数相除时，分数不会丢失
print(number)
print(7//3)         #"//"用作整数相除时，分数会丢失

width=20            #"="符号用来把一个特定值赋值给一个变量
height=5*9
s=width*height
print(s)

x=y=z=0             #一个值可以同时赋给好多个变量
print(x)            #变量在它们使用之前必须被定义（或者赋值），否则会抛出错误

print(10.0/2)       #这里完全支持浮点运算，包含多种类型操作数会把整数整数操作数变为浮点数
print(10/2)         #结果也为5.0

#虚数的表示（实数+虚数j）或者complex（实数，虚数）
print(1j*1j)
print((0+2j)*(0+2j))
print(complex(0,2)*complex(0,2))
a=(1+2j)
print(a.real)       #输出a的实数部分
print(a.imag)       #输出a的虚数部分
#获取复数的大小，用abs（）函数
b=abs(a)            #abs(a)=sqrt(a.real**2+a.imag**2)
print(b)



