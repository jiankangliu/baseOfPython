import random
offices = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for teacher in teachers:
    offices[random.randint(0, 2)].extend(teacher)
for office in offices:
    print(f'{offices.index(office)}办公室有人{len(office)}:{office}')






