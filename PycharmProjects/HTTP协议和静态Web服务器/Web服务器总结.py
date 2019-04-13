import socket
import threading


class Web_server():
    def __init__(self):
        object.__init__(self)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        server_socket.bind(("", 8888))
        server_socket.listen(128)
        self.server_socket = server_socket

    @staticmethod
    def handler_server_client_socket(server_client_socket):
        recv_data = server_client_socket.recv(4096)
        recv_content = recv_data.decode("gbk")
        file_path = recv_content.split("\r\n")[0].split(" ", maxsplit=2)[1]
        if file_path == '/':
            file_path = "/index.html"
        try:
            with open("static" + file_path, "rb") as f:
                file_data = f.read()
        except Exception as e:
            with open("static/404.html", "rb") as f:
                file_data = f.read()
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server:PWS1.0\r\n"
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + file_data
            server_client_socket.send(response_data)
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server:PWS1.0\r\n"
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + file_data
            server_client_socket.send(response_data)
        finally:
            server_client_socket.close()

    def start(self):
        while True:
            server_client_socket, ip_port = self.server_socket.accept()
            print("用户的IP和端口：", ip_port)
            # sub_thd = threading.Thread(target=self.handler_server_client_socket, args=(server_client_socket,))
            # sub_thd.start()
            self.handler_server_client_socket(server_client_socket)


def main():
    web_server = Web_server()
    web_server.start()


if __name__ == '__main__':
    main()







