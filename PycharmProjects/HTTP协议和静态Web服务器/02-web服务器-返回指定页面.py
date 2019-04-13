import socket


# 1.0 不管用户请求哪个 URL 始终返回一个网页即可 面向对象
# 2.0 返回用户需要的页面数据

class HTTPServer(object):
    """HTTP 服务器"""
    def __init__(self, port):
        """初始化属性 创建服务器套接字"""
        object.__init__(self)  # 构造父类的属性
        # super().__init__()
        # 1 创建一个服务器套接字对象
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2 端口复用
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 3 绑定端口
        server_socket.bind(('', port))
        # 4 监听
        server_socket.listen(128)

        # 将服务器套接字保存为当前对象的实例属性
        self.server_socket = server_socket


    def start(self):
        """启动服务器"""
        while True:
            # 5 开始接受客户端的连接请求
            client_socket, client_address = self.server_socket.accept()
            print("接受到了来自%s的连接请求" % str(client_address))
            # 6 当用户连接时 调用方法 处理该用户请求
            self.client_handler(client_socket)


    def client_handler(self, client_socket):
        """处理该用户请求"""
        # 6.1 接收用户的数据-请求报文  不收可能会有问题(返回用户需要的网页 首先应该知道用户请求的资源路径是哪个)
        # 得到用户请求路径之后 可以根据该路径返回对应的网页资源 给用户即可
        # 6.1.1 收请求报文
        request_data = client_socket.recv(4096)

        # 6.1.2 判断用户是否已经下线了
        if not request_data:
            print("客户端下线了")
            client_socket.close()
            return

        # 6.1.3 拆分请求报文 得到 用户的资源请求路径 ("GET 资源路径 版本\r\n头名:值\r\n\r\n")
        # request_str_data = request_data.decode()
        # request_line = request_str_data.split("\r\n")[0]
        # path_info = request_line.split(" ")[1]

        path_info = request_data.decode().split("\r\n")[0].split(" ")[1]
        print("获取用户的资源请求 %s" % path_info)
        # static + /index.html /index2.html

        # 6.1.4 判断用户的资源路径是否是/表示主页    static + /
        if path_info == '/':
            path_info = '/index.html'

        # 6.1.5 拼接响应报文-HTTP响应报文格式 响应行 + 头 + 空行 + 响应体

        # 6.1.6 根据用户的资源请求路径 读取对应的文件数据 作为响应体发送给用户
        # with open('index.html', "rb") as file:
        # with open('web.jpg', "rb") as file:
        try:
            with open("static" + path_info, "rb") as file:
                file_data = file.read()  # 字节类型
        except Exception as e:
            # 如果异常执行这里 状态码设置为404 Not Found
            respose_data = "HTTP/1.1 404 Not Found\r\n" + "Server: PWS1.0\r\n" + "\r\n"
            with open("static/404.html", "rb") as file:
                file_data = file.read()  # 字节类型
        else:
            # 如果政策执行这里 状态码设置为200 OK
            respose_data = "HTTP/1.1 200 OK\r\n" + "Server: PWS1.0\r\n" + "\r\n"
        finally:
            # 正常与否都执行这里
            print(respose_data)
            http_respose_data = respose_data.encode() + file_data
            # 6.3 发送给浏览器
            client_socket.send(http_respose_data)

            # 6.4 关闭连接-短连接
            client_socket.close()


def main():
    # 1 创建1HTTPServer 对象
    http_server = HTTPServer(8888)

    # 2 启动 HTTP 服务器
    http_server.start()


if __name__ == '__main__':
    main()


