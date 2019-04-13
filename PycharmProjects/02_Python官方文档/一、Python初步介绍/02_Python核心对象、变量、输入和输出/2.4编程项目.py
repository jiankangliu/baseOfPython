#1找零钱
strMoney=input("Enter amount of change:")
money=int(strMoney)
Quarters=money//25
money=money%25
Dimes=money//10
money=money%10
Nickels=money//5
money=money%5
Cents=money
print("Quarter: ",Quarters,"\t","Dimes: ",Dimes,"\n","Nickels: ",
      Nickels,"\t","Cents: ",Cents,sep="")

#2汽车贷款
loan=float(input("Enter amount of loan:"))
rate=float(input("Enter interest rate (%):"))
years=float(input("Enter number of years:"))
payment=(rate/1200)/(1-(1+rate/1200)**(-12*years))*loan
print("Monthly payment: ${0:.2f}".format(payment))

#3债券收益
faceValue=float(input("Enter face value of bond: "))
interestRate=float(input("Enter coupon interest rate: "))
currentMarketPrice=float(input("Enter current market price: "))
untilMaturity=float(input("Enter years until maturity: "))
a=(faceValue-currentMarketPrice)/untilMaturity
b=(faceValue+currentMarketPrice)/2
intr=faceValue*interestRate
YTM=(intr+a)/b
print("Approximate YTM: {0:.2%}".format(YTM))

#单位价格




