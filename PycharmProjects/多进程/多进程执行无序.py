import multiprocessing
import time


def func():
    while True:
        print('这是子进程ID：', multiprocessing.current_process().name)
        time.sleep(1)


def main():
    for i in range(5):
        pro = multiprocessing.Process(target=func)
        pro.start()


if __name__ == '__main__':
    main()







