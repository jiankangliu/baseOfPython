#3.4.1 等差数列的循环遍历
#range函数可以用来产生一个等差数列。如果m和n是整数，并且m<n，则函数range(m,n)会产生一系列的整数m,m+1,...,n-1

#3.4.2 range函数的步长值
#range(m,n,s)   s为步长

#3.4.3 for的循环嵌套
for m in range(1,6):
    for n in range(1,6):
        print(m,"*",n,"=",m*n,"\t",end="")
    print()

#3.4.4 字符串字符的循环遍历
#for ch in str1：
#   indented block of statements
#这个循环执行len（str1）遍

#例6 逆序单词
word=input("Enter a word: ")
reverseWord=''
for ch in word:
    reverseWord=ch+reverseWord
print("Reverse word is:",reverseWord)

#3.4.5 遍历列表或元组元素的循环遍历
#for item in listO人Tuple：
#   indented block of statements
#循环执行len（listOrTuple）遍

#3.4.6 文本文件的行循环遍历
#例10 美国总统
firstName=input("Enter a first name: ")
foundFlag=False
infile=open("USPres.txt",'r')
for line in infile:
    if line.startswith(firstName+' '):
        print(line.rstrip())
        foundFlag=True
infile.close()
if not foundFlag:
    print("No president had the first name",firstName)

#3.4.7 pass语句
#for循环头后面至少要跟着一条缩进语句块。当你什么也不想做时就用pass补充

#例11 文件的最后一行移除文本文件行尾的换行符
infile=open("3.4例11.txt",'r')
for line in infile:
    pass
line.rstrip()
infile.close()

#3.4.8使用文本文件的内容创建列表
dataList=[]
infile=open("Data.txt",'r')
for line in infile:
    dataList.append(line.rstrip())
print(dataList)

infile=open("Data.txt",'r')                     #更高效
dataList=[line.strip() for line in infile]
infile.close()

#以数字的形式存入列表dataList[]                       更高效
# infile=open("Data.txt",'r')
# dataList=[eval(line) for line in infile]
# infile.close()
