import threading
import socket
import sys


class HttpWebServer(object):
    def __init__(self, port):
        object.__init__(self)
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", port))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket


    @staticmethod
    def handle_client_request(new_socket):
        recv_client_data = new_socket.recv(4096)
        if not recv_client_data:
            print("客户端关闭。")
            new_socket.close()
            return
        recv_client_content = recv_client_data.decode("gbk")
        print(recv_client_content)
        request_path = recv_client_content.split("\r\n")[0].split(" ", maxsplit=2)[1]
        if request_path == "/":
            request_path = "/index.html"
        try:
            with ("static" + request_path, "rb") as file:
                file_data = file.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server:PWS1.0\r\n"
            with("static/404.html", "rb") as file:
                file_data = file.read()
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + file_data
            new_socket.send(response_data)
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server:PWS1.0\r\n"
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + file_data
            new_socket.send(response_data)
        finally:
            new_socket.close()


    def start(self):
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            sub_thd = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            sub_thd.setDaemon(True)
            sub_thd.start()


def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("执行命令如下：python3 xxx.py 8888")
        return
    if not sys.argv[1].isdigit():
        print("执行命令如下：python3 xxx.py 8888")
        return
    port = int(sys.argv[1])
    tcp_server_socket = HttpWebServer(port)
    tcp_server_socket.start()


main()













