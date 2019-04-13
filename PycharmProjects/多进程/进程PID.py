import multiprocessing
import os


def func():
    print('这是子进程：%s' % os.getpid())
    print('这是父进程：%s' % os.getppid())


def main():
    for i in range(5):
        pro = multiprocessing.Process(target=func)
        pro.start()
        pro.join()
    print('这是主进程：%s' % os.getpid())


if __name__ == '__main__':
    main()


