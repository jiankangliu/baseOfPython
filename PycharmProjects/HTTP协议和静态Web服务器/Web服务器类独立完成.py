import socket
import threading


class Web_service_socket(object):
    def __init__(self):
        object.__init__(self)
        service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        service_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        service_socket.bind(('', 8888))
        service_socket.listen(128)
        self.service_socket = service_socket

    def handler(self):
        service_client_socket = self.service_socket.accept()
        recv_data = service_client_socket.recv(4096)
        recv_content = recv_data.decode("gbk")
        print(recv_content)
        # recv_list = recv_content.slipt

service_socket = Web_service_socket()
service_socket.handler()

