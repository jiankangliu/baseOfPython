#5.1.1读取文本文件
#infile = open(fileName,'r')
#创建一个程序和文件的连接，能够让程序从文件中读取数据。
#文件称作为了读取文件而打开（open for reading）
#或者为了输入而打开（open for input）
#open函数返回一个文件对象（file object）
#变量infile被用于从文件中读取行以及最终终端和文件连接。
#在文件为读取而被打开后，一个具有如下头部的for循环：
#for line in infile：
#用来连续访问文件中的行。

#例1 最初三任总统
def main():
    file="FirstPresidents.txt"
    displayWithForLoop(file)
    print()
    displayWithListComperhension(file)
def displayWithForLoop(file):
    infile=open(file,'r')
    for line in infile:
        print(line,end='')                  ###只使用for循环，换行符(\n)会出现在每一行的结尾
    infile.close()
def displayWithListComperhension(file):
    infile=open(file,'r')
    listPres=[line.rstrip() for line in infile]
    print(listPres)
    infile.close()
main()

#一个为了读取而被打开的文件也能使用read和reading方法访问
#strVar = infile.read()     将文件的全部内容置于一个字符串中

#当一个文本文件为了输入而被打开时，指针置于文件第一行的开始。
#每次，语句strVar=infile.readline()执行后，当前行被赋给strVar，指针前进到改行的结尾。
#所有的行读取后，readline方法返回空字符串。


#5.1.2 创建文本文件
#outfile = open(fileName, 'w')
#使用指定名字创建一个新的文本文件。这个文件被指定成为了写入而打开（opened for writing）。
#变量outfile用来向文中写入行，并且用来在最后关闭文件。
#如果list1代表一个字符串的列表，其中每一个字符串都以换行符（\n）结尾，
#下面这个语句outfile.writelines(list1)
#将列表中每一个元素作为一行写入文件。
#如果strVar的值为一个字符串，那么语句outfile.write(strVar)会将strVar的值追加到文件中

#例2 美国总统
def main():
    outfile=open("FirstPresidents2.txt",'w')
    createWithWritelines(outfile)
    outfile=open("FirstPresidents3.txt",'w')
    createWithWrite(outfile)

def createWithWritelines(outfile):
    list1=["George Washington","John Adams","Thomas Jefferson"]
    for i in range(len(list1)):
        list1[i]=list1[i]+"\n"
    outfile.writelines(list1)
    outfile.close()

def createWithWrite(outfile):
    outfile.write("George Washington\n")
    outfile.write("John Adams\n")
    outfile.write("Thomas Jefferson\n")
    outfile.close()
main()

#例3 美国州
def main():
    statesList=createListFromFile("States.txt")
    createSorteFile(statesList,"StatesAlpha.txt")

def createListFromFile(fileName):
    infile=open(fileName,'r')
    desiredList=[line.rstrip() for line in infile]
    infile.close()
    return desiredList

def createSorteFile(listName,fileName):
    listName.sort()
    for i in range(len(listName)):
        listName[i]=listName[i]+"\n"
    outfile=open(fileName,'w')
    outfile.writelines(listName)
    outfile.close()

main()







