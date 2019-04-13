head = int(input("请输入头数："))
leg = int(input("请输入腿数："))

chicken = 0
while chicken <= head:
    if (chicken << 1) + ((head - chicken) << 2) == leg:
        print(f"有鸡{chicken}只，兔子{head - chicken}只")
        break
    else:
        chicken += 1
if chicken > head:
    print("输入有误！")

