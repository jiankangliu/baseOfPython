print("a","b",sep=" ")  #通过sep参数将分隔符改变为任意想要的字符串
print("Hello",end=" liujiankang ")      #通过end参数将结束操作进行改变
print("world!")

#2.2.3转义序列
print("a\tb\tc")    #\t在下一制表符输出，产生一个水平制表符
print("e\nf")       #\n在下一行输出，产生一个换行操作
str1="a\nb"
print(len(str1))    #\t和\n被看作一个字符

#2.3.4区域内输出对齐
#ljust(n)，rjust（n）和center（n）
#n代表宽度为n的域，如果一个字符串没有达到域制定的宽度，则用空格补充
print("0123456789"*4)
print("Rank".ljust(5),"Player".ljust(20),"HR".rjust(3),sep="")
print("liu".center(23))

#2.3.5使用format方法对齐输出
str1="liu"
w=len(str1)
print("0123456789"*3)
print("{0:<5s}".format(str1))   #等价于print(str1.ljust(5))
print("{0:^6s}".format(str1))   #等价于print（str1.center（6））
print("{0:>5s}".format(str1))   #等价于print（str1.rjust（5））

num1=123
print("{0:<3n}".format(num1))   #等价于print（num1.ljust（w））
print("{0:^3n}".format(num1))   #等价于print（num1.center（w））
print("{0:>3n}".format(num1))   #等价于print（num1.人just（w））

#例3输出对齐
print("0123456789"*3)
print("{0:^5s}{1:<20s}{2:>3s}".format("Rank","Player","HR"))
print("{0:^5n}{1:<20s}{2:>3n}".format(1,"Barry Bonds",726))
print("{0:^5n}{1:<20s}{2:>3n}".format(3,"Babe Ruth",714))

#展示格式化数字
print("{0:10d}".format(123))        #print("{0:m}"),m表示宽度
print("{0:10,d}".format(12345678))  #,表示添加千位符
print("{0:10,.2f}".format(12345.123))#保留两位小数四舍五入，并添加千位符
print("{0:10,.2%}".format(12234.168))

#例4 P46
print("The area of {0:s} is {1:d} square miles".format("Texas",268820))
str1="The population of {0:s} is {1:.2%} of the U.S. population."
print(str1.format("Texas",26448000/309000000))
str1="abcasd\n"
str2="liu"
print(str1+str2)
print(str1.rstrip()+str2)       #rstrip()得以移除字符串末尾的空格符、换行符、制表符和转义序列

#实践问题2.3
print("{0:s}{1:s}".format("spam","eggs"))
str1="Ask not what {0:s} {1:s} you,ask what you {1:s} {0:s}"
print(str1.format("your country","can you do"))

print("He said \"How ya doin?\" to me.")
print('He said "How ya doin?" to me.')      #不使用转义序列重写上行语句

#习题2.3
print("Bon"," Voyage",'!',sep="")
print("Price: ",'$',23.45,sep="")
print("Portion: ",90,'%',sep="")
print("Py","th","on",sep="")
print(1,2,3,sep=" x ")
print("tic","tac","toe",sep="-")
print("father","in","law",sep="-")
print("one","two","there",sep=',')
print('T',end="-")
print("shirt")
print("spam",end=" and ")
print("eggs")
print("Py",end="")
print("thon")
print("on","site",sep='-',end='')
print("repair")
print("Hello\n")
print("World")
print("Hello\n",end="")
print("World")
print("one\ttow\tthere\tfour")
print("1\t2\t3")
print("Detroit\tLions")
print("Indianapolis\tColts")
print("NUMBER\tSQUARE")
str1="abcd"
#print(str1(2)+"\t"+str1(2**2))   不懂，P47，17题
print("COUNTRY\t","LAND AREA")
print("India\t",2.5,"million sq km")
print("China\t",9.6,"million sq km")
print("Hello\t\tWorld!")
print("Hello\tWorld!".expandtabs(16))   #expandtabs(m)将\t转换为m个空格
print("STATE\tCAPITAL".expandtabs(15))
print("North Dakota\tBismarck".expandtabs(15))
print("South Dakota\tPierre".expandtabs(15))
print("0123456789")
print("A".rjust(5),"B".center(5),"C".ljust(5),sep="")
print("0123456789012345")
print("one".center(7),"two".ljust(4),"there".rjust(6),sep="")
print("01234567890123456")
print("{0:^7s}{1:4s}{2:>6s}".format("one","two","there"))
print("01234567890")
print("{0:>5s}{1:^5s}{2:<5s}".format("A","B","C"))
print("0123456789")
print("{0:10.2%}".format(.123))
print("{0:^10.1%}".format(1.23))
print("{0:<10,.2%}".format(12.3))
print("0123456789")
print("{0:10,d}".format(1234))
print("{0:^10,d}".format(1234))
print("{0:<10,d}".format(1234))
print("${0:,.2f}".format(1234.567))
print("{0:,.0f}".format(1234.567))
print("{0:,.0f}".format(1.234))
print("${0:,.2f}".format(1234))
print("{0:10s}{1:^16s} {2:s}".format("Language","Native speakers","% of World Pop"))
print("{0:10s}{1:^16,d}{2:10.2%}".format("Mandarin",935000000,.141))
print("{0:10s}{1:^16,d}{2:10.2%}".format("Spanish",387000000,.0585))
print("{0:10s}{1:^16,d}{2:10.2%}".format("English",365000000,.0552))
print("012345678901234")
print("{0:14s}{1:s}".format("Major","Percent of Students"))
print("{0:14s}{1:10.1%}".format("Biology",.062))
print("{0:14s}{1:10.1%}".format("Psychology",.054))
print("{0:14s}{1:10.1%}".format("Nursing",.047))
print("Be {0:s} - {1:s} else is taken".format("yourself","everyone"))
print("Plan {0:s}, code {1:s}.".format("first","later"))
print("Always {0:s} on the bright side of {1:s}.".format("look","life"))
print("And now for {0:s} completely {1:s}.".format("something","different"))

x=3
y=4
print("The product of {0:d} and {1:d} is {2:d}".format(x,y,x*y))

str1="The chances of winning the {0:s} are 1 in {1:,d}"
print(str1.format("Powerball Lottery",175223510))

x=2
print("The square root of {0:d} is about {1:.5f}.".format(x,x**.5))

Pi=3.14159265898
print("Pi is approximately {0:.5f}.".format(Pi))

str1="In a randomly selected group of {0:d} people "+\
    "probability\nis {1:.2f} that 2 people have the same birthday."
print(str1.format(23,.507397))

areaOfAlaska=663267
costOfAlaska=7200000
str1="The cost of Alaska was about ${0:.2f} per square mile."
print(str1.format(areaOfAlaska/costOfAlaska))

str1="You miss {0:.0%} of the shots you never take.-Wayne Gretsky"
print(str1.format(1))

str1="{0:.0%} of the member of the U.S. Senate are from {1:s}"
print(str1.format(12/100,"New England"))

print("{0:.2%} of the UN nations are in {1:}".format(43/193,"Europe"))

str1="The area of {0:s} to {1:.1%} of the area of the U.S."
print(str1.format("Alaska",663267/3794000))

print("{0:s}{1:s}{0:s}".format("abra","cad"))

print("When you have {0:s} to {1:s},{1:s} {0:s}.".format("nothing","say"))

str1="Be {0:s} whenever {1:s}.It is always {1:s}.-Dalai Lama"
print(str1.format("kind","possible"))

str1="If {0:s} dream it,{0:s} do it. -Walt Disney"
print(str1.format("you can"))

print("Hello","aaa",end="\n")
print("Hello")

print("Hello\tWorld")
print("Hello\tWorld".expandtabs(8))

#实践问题2.3的解答
print("{0} and {1}".format("spam","eggs"))  #大括号中的s是默认的指示符，添加s是为了提高可读性

