import socket
import multiprocessing


def hand_client_socket(service_socket):
    client_socket, ip_port = service_socket.accept()
    print("客户端的IP地址和端口：", ip_port)
    pro = multiprocessing.Process(target=hand_client_socket, args=(service_socket,))
    pro.daemon = True
    pro.start()
    while True:
        receive_data = service_socket.recv(1024)
        if receive_data:
            receive_content = receive_data.decode("gbk")
            print(f"客户端回复：{receive_content}")
            send_content = input("请回复：")
            send_data = send_content.encode("utf-8")
            client_socket.send(send_data)
        else:
            print("客户端关闭。")
            client_socket.close()


if __name__ == '__main__':
    service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service_socket.bind(("", 8888))
    service_socket.listen()

    pass


