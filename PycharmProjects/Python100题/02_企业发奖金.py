profit = int(input('请输入利润额：'))
if profit <= 100000:
    bonus = profit/10
elif profit <= 200000:
    bonus = 10000 + (profit - 100000) * 0.075
elif profit <= 400000:
    bonus = 17500 + (profit - 200000) * 0.05
elif profit <= 600000:
    bonus = 27500 + (profit - 400000) * 0.03
elif profit <= 1000000:
    bonus = 33500 + (profit - 600000) * 0.015
else:
    bonus = 39500 + (profit - 1000000) * 0.01
print(f'奖金为：{bonus}')
