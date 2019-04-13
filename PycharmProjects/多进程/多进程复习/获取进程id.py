import multiprocessing
import os


def sing():
    print("sing_ID:", os.getpid())
    print("sing_name:", multiprocessing.current_process())
    print("sing_pro父进程ID：", os.getppid())
    pass


def dance():
    print("dance_ID:", os.getpid())
    print("dance_name:", multiprocessing.current_process())
    pass


if __name__ == '__main__':
    print("main_ID：", os.getpid())
    print("main_name:", multiprocessing.current_process())
    sing_pro = multiprocessing.Process(target=sing, name="sing")
    dance_pro = multiprocessing.Process(target=dance, name="dance")
    sing_pro.start()
    print("sing_pro_name", sing_pro.name)
    dance_pro.start()
    print("dance_pro_name", dance_pro.name)






