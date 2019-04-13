#Python的核心对象是数值，字符串，列表，元组，文件，集合和字典
#2.4.1列表对象。     列表是Python对象的一个有序序列。其中对象可以是任意类型，并不要求类型必须一致。
team=["Seahawks",2014,"CenturyLink Field"]
nums=[5,10,4,5]
words=["spam","ni"]
#列表操作
len(words)
max(nums)           #最大值（元素必须是相同类型）
min(nums)
sum(nums)           #元素必须是数字
nums.count(5)       #一个对象出现的次数
nums.index(4)       #一个对象首次出现的索引位置
words.reverse()     #所有元素的逆序
#team.clear()        #清空列表
nums.append(7)      #在末端插入元素
del team[-1]        #移除给定索引位置上的元素
nums.remove(5)      #移除一个对象的首次出现
words.insert(1,"wink")  #在给定索引位置插入新元素
print(team+nums)        #+连接两个列表，等同于List1.extend(List2)
print(team*3)           #*可以是列表重复

#例1 成绩
# grade=[]
# num=float(input("Enter the first grade: "))
# grade.append(num)
# num=float(input("Enter the second grade: "))
# grade.append(num)
# num=float(input("Enter the third grade: "))
# grade.append(num)
# num=float(input("Enter the fourth grade: "))
# grade.append(num)
# num=float(input("Enter the fifth grade: "))
# grade.append(num)
# max=max(grade)
# min=min(grade)
# grade.remove(max)
# grade.remove(min)
# len=len(grade)
# sum=sum(grade)
# print("Average Grade:{0:.2f}".format(sum/len))

#索引i对应的值可通过下面的方式修改。     Listname[i]=newValue
words[1]="eggs"

#一堆封闭括号中的任何代码都可以在多行显示
# team["Seahawks",2014,"CenturyLink Field"]       #可以写成如下形式
# team["Seahaws",
# 2014,"CenturyLink Field"]

#切片
List=[0,1,2,3,4,5,6,7,8,9]
print(List[1:4])    #List[m:n]      得到一个ist中从索引m到n-1的所有元素
print(List[:])      #List[:]        得到一个与List一样的新列表
print(List[2:])     #List[m:]       得到一个从索引m到列表末尾的列表
print(List[:4])     #List[:m]       得到一个从列表第0个元素到m-1个元素的列表


#2.4.3split和join方法
#split方法将字符串变成其子串组成的列表
#join方法将一个字符串列表变成一个字符串
str="a,b,c,d,e,f,g"
strList=["a","b","c","d","e","f","g"]
print(str.split(","))
print("".join(strList))     #""号间的内容为连接符号


#2.4.4文本文件
#Python程序中使用的数据都存储在内存之中，当程序终止时就消失了。
# 然而，如果程序将数据写入到存储设备（如硬盘或者闪存盘）上的文件中，任何程序都可以稍后继续访问这些数据。
#也就是说文件建立了长期存储的数据
#我那本文件是由没有任何格式（即粗体或者斜体）的文本行组成的简单文件，可以通过Notepad（PC）或TextEdit（Mac）进行创建和阅读
#一般情况文本文件有txt的后缀
# infile=open("Data.txt",'r')
# listName=[line.rstrip() for line in infile]
# infile.close()
#
# infile=open("Data.txt",'r')
# listName=[line.rstrip() for line in infile]
# infile.close()

#2.4.5元组对象
#元组与列表类似，是元素的有序序列。
#元组与列表的主要区别在于元组不可以直接修改，即元组没有append，extend和insert方法，
#元组中的元素也不可以直接删除或者修改
#例4元组函数
t=5,7,6,3       #等价于t=(5,7,6,3)
print(t)
print(len(t),max(t),min(t),sum(t))
print(t[0],t[-1],t[:2])

(x,y,z)=(5,6,7)     #等价于x,y,z=5,6,7     可以看作用一个语句同时给三个变量赋值

#例5 交换数值
x=5
y=6
x,y=y,x     #将元组（6，5）赋值给元组（x，y）
print(x,y)

#2.4.6嵌套列表
regions=[("Northeast",55.3),("Midwest",66.9),("South",114.6),("West",71.9)]
print("The 2010 population of the",regions[1][0],"was",regions[1][1],"million.")
totalPop=regions[0][1]+regions[1][1]+regions[2][1]+regions[3][1]
print("Total 2010 population of the U.S. {0:.1f} million.".format(totalPop))

#2.4.7不可变和可变对象
#列表能够原地修改，但是数值，字符串和元组不可以。
#能够原地修改的对象称为可变的，而不能原地修改的对象称为不可变的。

#2.4.8列表的复制
#如果变量var1是一个可变数据（如列表），那么var2=var1的这种语句形式会将var2和var1一样引用同一个对象。
#因此任何一个的改变都会影响另外一个的值。
list1=["a","b"]
list2=list1         #list2引用的是和list1一样的内存位置。
list2[1]="c"
print(list1)        #输出['a','c']

list1=["a","b"]
list2=list1[:]      #list2指向一个与list1值相同，但与list1不同位置上的对象
list2[1]="c"
print(list1)

#2.4.9索引、删除和切片越界
#Python不允许列表和元组单个元素的索引越界，但在切片中可以允许索引越界
list1=[1,2,3,4,5]
print(list1[-2:1])
#单个元素组成的元组有一个末尾的","。如（0,）

#list函数可以将元组或字符串转化为列表。例如：
print(list(("a","b")))
print(list("Python"))

#tuple函数可以将列表或字符串转化为元组。例如：
print(tuple(["a","b"]))
print(tuple("Python"))

#元组比列表更加高效，因此应该在元素不发生变化的情况下使用元组。它们执行的更快，内存占用更少。
# 而且能够”写保护“数据。

#实践问题2.4
companies=[("Apple","Cupertino","CA"),("Anazom.com","Seattle","WA"),
           ("Google","Mountain View","CA")]
(name,city,state)=(companies[1][0],companies[1][1],companies[1][2])
print(name,"is located in",city,",",state,'.')

a=2
b=3
print((a+b,))
print((a+b))
print(())

s='a'+'b'
print(len(s))
s="".join(['a','b'])
print(s)


#习题2.4
#101
sentence=(input("Enter the sentence: "))
list=sentence.split()
len=len(list)
print("Number of worlds:{0:d}".format(len))

#102
sentence=input("Enter the sentence:")
list=sentence.split()
firstWord=list[0]
lastWord=list[-1]
print("First word:{0}\nLast word:{1}".format(firstWord,lastWord))

#103
twoPartName=input("Enter a 2-part name:")
nameList=twoPartName.split()
print("Revised form: ",nameList[0],", ",nameList[1],sep="")

#104
threePartName=input("Enter a 3-part name:")
list=threePartName.split()
print("Middle name: ",list[1],sep="")












