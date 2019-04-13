import multiprocessing
import time
import os


def func():
    while True:
        print('进程在进行。')
        time.sleep(1)


def main():
    pro = multiprocessing.Process(target=func)
    pro.daemon = True
    pro.start()
    time.sleep(4)
    pass


if __name__ == '__main__':
    main()



