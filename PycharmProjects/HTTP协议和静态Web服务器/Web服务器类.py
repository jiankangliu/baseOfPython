import socket
import threading
import sys

class HttpWebServer(object):
    def __init__(self, port):
        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口复用，程序退出端口立即释放
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        tcp_server_socket.bind(("", port))
        tcp_server_socket.listen(128)
        # 保存常见成功的服务端套接字
        self.tcp_server_socket = tcp_server_socket

    # 处理客户端请求
    @staticmethod
    def handle_client_request(new_socket):
        # 代码执行到此说明连接建立成功
        recv_client_data = new_socket.recv(4096)
        if len(recv_client_data) == 0:
            print("关闭浏览器了")
            new_socket.close()
            return
        recv_client_content = recv_client_data.decode("gbk")
        print(recv_client_content)
        # 根据指定字符长进行分割，最大分割次数指定2
        request_list = recv_client_content.split(" ", maxsplit=2)
        # 获取资源请求路径
        request_path = request_list[1]
        print("资源请求路径：", request_path)
        # 判断请求的是否是根目录，如果条件成立，指定首页数据返回
        if request_path == "/":
            request_path = "/index.html"
        try:
            # 动态打开指定文件
            with open("static" + request_path, "rb") as file:
                file_data = file.read()
        except Exception as e:
            # 请求资源不再，返回 404 数据
            # 响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server:PWS1.0\r\n"
            with open("staric/error.html", "rb") as file:
                file_data = file.read()
            response_bady = file_data
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_bady
            new_socket.send(response_data)
        else:
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server:PWS1.0\r\n"
            # 相应体
            response_body = file_data
            # 拼接响应报文
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_bady
        finally:
            # 关闭服务与客户端的套接字
            new_socket.close()
    def start(self):
        while True:
            # 等待接受客户端请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 当客户端和服务器建立连接，创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            # 设置守护主线程
            sub_thread.daemon = True
            # 启动子线程执行对应的任务
            sub_thread.start()


def main():
    print(sys.argv)
    # 判断命令行参数知否等于 2
    if len(sys.argv) != 2:
        print("执行命令如下：python3 xxx.py 8000")
        return
    # 获取终端命令行参数
    port = int(sys.argv[1])
    # 创建Web服务器对象
    Web_server = HttpWebServer(port)
    # 启动Web服务器进行工作
    Web_server.start()















