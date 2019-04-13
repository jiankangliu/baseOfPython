import socket
import threading
# 处理客⼾端的请求操作


def handle_client_request(service_client_socket, ip_port):
    # 循环接收客⼾端发送的数据
    while True:
        # 接收客⼾端发送的数据
        recv_data = service_client_socket.recv(1024)
        # 容器类型判断是否有数据可以直接使⽤if语句进⾏判断，如果容器类型⾥⾯有数据表⽰条件成⽴，否则条件失败
        # 容器类型: 列表、字典、元组、字符串、set、range、⼆进制数据
        if recv_data:
            print(recv_data.decode("gbk"), ip_port)
            # 回复
            send_data = input("请回复：")
            send_content = send_data.encode("utf-8")
            service_client_socket.send(send_content)
        else:
            print("客⼾端下线了:", ip_port)
            service_client_socket.close()
            break
            # 终⽌和客⼾端进⾏通信
if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端⼝号复⽤，让程序退出端⼝号⽴即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端⼝号
    tcp_server_socket.bind(("", 9090))
    # 设置监听, listen后的套接字是被动套接字，只负责接收客⼾端的连接请求
    tcp_server_socket.listen(128)
    # 循环等待接收客⼾端的连接请求
    while True:
        # 等待接收客⼾端的连接请求
        service_client_socket, ip_port = tcp_server_socket.accept()
        # 案例-多任务版TCP服务端程序开发
        print("客⼾端连接成功:", ip_port)
        # 当客⼾端和服务端建⽴连接成功以后，需要创建⼀个⼦线程，不同⼦线程负责接收不同客⼾端的消息
        sub_thread = threading.Thread(target=handle_client_request, args=(service_client_socket, ip_port))
        # 设置守护主线程
        sub_thread.setDaemon(True)
        # 启动⼦线程
        sub_thread.start()
