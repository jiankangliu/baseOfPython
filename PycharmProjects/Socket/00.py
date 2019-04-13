import threading
import socket


def handler_client(service_socket):
    client_socket, ip_port = service_socket.accept()
    print("客户端IP和端口", ip_port)


def tansmit_data():
    receive_data = client_socket.recv()
    receive_content = receive_data.decode("gbk")
    send_content = input("请回复：")
    send_data = send_content.encode("utf-8")
    client_socket.send(send_data)
    pass

if __name__ == '__main__':
    service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    service_socket.bind(("", 7777))
    client_socket, ip_port = service_socket.accept()
    print("客户端IP和端口：", ip_port)
    while True:
        thd = threading.Thread(target=handler_client, args=(service_socket,))
        thd.start()
        tansmit_data()


