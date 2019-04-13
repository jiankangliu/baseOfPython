"""
1.尝试打开文件
    1.1 尝试：循环读取数据并打印数据 -- 一次性读取一行 暂停2秒钟再打印

如果没有这个文件，捕获异常并提示没有这个文件
"""
import time
try:
    f = open('1.txt')

    try:
        while True:
            con = f.readline()
            # 如果读取的数据的长度是0表示没有其他数据 -- 退出循环即可
            if len(con) == 0:
                break

            time.sleep(2)
            print(con)
    except:
        print('意外终止了')  # 命令提示符 按快捷键ctrl+c
    finally:
        f.close()
        print('文件已经关闭')

except:
    print('没有这个文件')





