import threading
import os
import time


def sing(sname, singer):
    while True:
        print(f'{singer}在唱{sname}。')
        time.sleep(2)


def dance(dname, dancer):
    while True:
        print(f'{dancer}在跳{dname}。')
        time.sleep(2)


def main():
    thd1 = threading.Thread(target=sing, args=('荷塘月色', '梨花'))
    thd1.start()
    thd2 = threading.Thread(target=dance, kwargs={'dname': 'dangerous', 'dancer': '迈克尔杰克逊'})
    thd2.start()
    pass


if __name__ == '__main__':
    main()



