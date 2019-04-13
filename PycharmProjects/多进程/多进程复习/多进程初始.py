import multiprocessing
import time


def sing():
    while True:
        print('正在唱歌。')
        time.sleep(1)


def dance():
    while True:
        print("正在跳舞。")
        time.sleep(1)


if __name__ == '__main__':
    pro1 = multiprocessing.Process(target=sing, name='sing')
    pro1.daemon = True
    pro2 = multiprocessing.Process(target=dance, name='dance')
    pro2.daemon = True
    pro1.start()
    pro2.start()
    time.sleep(0.1179)
    print(pro1.name)







