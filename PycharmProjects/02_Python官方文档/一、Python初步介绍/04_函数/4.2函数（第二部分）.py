#4.2.1 调用其它函数的函数
#例1 函数的调用
def main():
    firstPart()
    print(str(4)+":from function main")
def firstPart():
    print(str(1)+":from function main")
    secondPart()
    print(str(3)+":from function main")
def secondPart():
    print(str(2)+":from function main")
main()

#4.2.2 返回多个值的函数
#函数可以返回任何类型的对象，不仅仅是数字、字符串、或布尔值。例如函数可以返回一个元组。
#例2 返回多个值的函数
INTEREST_RATE=0.04
def main():
    principal=eval(input("Enter amount of the deposit: "))
    numberOfYears=eval(input("Enter the number of years: "))
    (bal,intEarned)=balanceAndInterest(principal,numberOfYears)
    print("Balance: ${0:,.2f}   Interest Earned: ${1:,.2f}".format(bal,intEarned))

def balanceAndInterest(prin,numYears):
    balance=prin*((1+INTEREST_RATE)**numYears)
    interstEarned=balance-prin
    return(balance,interstEarned)
main()

#4.2.3 列表解析
#当我们想要对列表中的每个元素执行一个特定的函数时，一个常见的for循环可以完成这项工作。但是
#更加方便的方式时使用列表解析
list1=['1','2','3','4','5']
list2=[eval(x) for x in list1]
def g(x):
    return int(x)**2
list3=[g(x) for x in list2]
print(list3)

#4.2.4 默认值
#一个函数的某些（或者全部）参数可以有默认值——当没有值传递给它们时而赋给的值。
#def functionName(par1,par2,par3=value3,par4=value4):
#functionName(arg1,arg2)的形式会将arg1的值赋给par1，arg2的值赋给par2

#4.2.5 按参数名传递
def total(w,x,y=10,z=20):
    return (w**x)+y+z
#total(w=2,x=3)     total(x=3,w=2)
#total(x=3,2)

pass

#4.2.6 自定义排序
#例6 单词排序
def main():
    list1=["democratic","sequoia","equals","brrr","break","twoooooooo"]
    list1.sort(key=len)
    print("Sorted by length in ascending order: ")
    print(list1,'\n')
    list1.sort(key=lastCharacter)
    print("Sorted by last character in descending order: ")
    print(list1,'\n')
    list1.sort(key=numberOfVowels,reverse=True)
    print("Sorted by number of vowels in descending order: ")
    print(list1)

def lastCharacter(word):
    return word[-1]

def numberOfVowels(word):
    vowels=['a','e','i','o','u']
    total=0
    for vowel in vowels:
        total +=word.count(vowel)
    return total
main()

#4.2.7 Lambda表达式
#Lambda表达式时一行代码构成的微型函数，经常在需要一个简单函数的地方使用。
#lambda par1,par2,......:expression

#例7 姓名排序
names=["Dennis Ritchie","Alan Kay","John Backus","James Gosling"]
names.sort(key=lambda name:name.split()[-1])
nameString=','.join(names)
print(nameString)

#4.2.8 sorted函数
#sort方法改变了列表中所有元素的顺序。
#sorted函数则返回一个新的已排序的列表。
list1=["white","blue","red"]
list2=sorted(list1)
print(list2)
list2=sorted(list1,reverse=True)
print(list2)
list2=sorted("spam")
print(list2)