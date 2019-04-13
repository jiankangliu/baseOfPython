# 平均分配老师
import random
teacher = ["a","b","c","d","e","f","g","h","i","j",'H']
l = [[],[],[]]

m = 0
while True:
    if len(teacher) == 0:
        break
    t = random.choice(teacher)
    teacher.remove(t)
    l[m].append(t)
    m += 1
    m %= len(l)
for office in l:
    print(f'{l.index(office)}办公室，有{len(office)}人{office}')

# t = random.choice(teacher)
# l[0].append(t)
# teacher.remove(t)
# print(l)
# print(teacher)
# #
# t = random.choice(teacher)
# l[1].append(t)
# teacher.remove(t)
# #
# t = random.choice(teacher)
# l[2].append(t)
# teacher.remove(t)
#
# print(l)

# for i in range(3):
#     t = random.choice(teacher)
#     l[i].append(t)
#     teacher.remove(t)
# #
# print(l)

# while True:
#     if not len(teacher):
#         break
# # for i in range(3):
#     for i in range(3):
#         if not len(teacher):
#             break
#         t = random.choice(teacher)
#         l[i].append(t)
#         teacher.remove(t)
#
# print(l)
