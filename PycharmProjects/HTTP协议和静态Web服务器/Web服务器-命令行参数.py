import socket
import threading
import sys
# 定义web服务器类


class HttpWebServer(object):
    def __init__(self, port):
        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端⼝号复⽤, 程序退出端⼝⽴即释放
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端⼝号
        tcp_server_socket.bind(("", port))
        # 设置监听
        tcp_server_socket.listen(128)
        # 保存创建成功的服务器套接字
        self.tcp_server_socket = tcp_server_socket

    # 处理客⼾端的请求
    @staticmethod
    def handle_client_request(new_socket):
        # 代码执⾏到此，说明连接建⽴成功
        recv_client_data = new_socket.recv(4096)
        if len(recv_client_data) == 0:
            print("关闭浏览器了")
            new_socket.close()
            return
        # 对⼆进制数据进⾏解码
        recv_client_content = recv_client_data.decode("utf-8")
        print(recv_client_content)
        # 根据指定字符串进⾏分割， 最⼤分割次数指定2
        request_list = recv_client_content.split(" ", maxsplit=2)
        # 获取请求资源路径
        request_path = request_list[1]
        print(request_path)
        # 判断请求的是否是根⽬录，如果条件成⽴，指定⾸⻚数据返回
        if request_path == "/":
            request_path = "/index.html"
        try:
            # 动态打开指定⽂件
            with open("static" + request_path, "rb") as file:
                # 读取⽂件数据
                file_data = file.read()
        except Exception as e:
            # 请求资源不存在，返回404数据
            # 响应⾏
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            with open("static/error.html", "rb") as file:
                file_data = file.read()
            # 响应体
            response_body = file_data
            # 拼接响应报⽂
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            # 发送数据
            new_socket.send(response_data)
        else:
            # 响应⾏
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            # 响应体
            response_body = file_data
            # 拼接响应报⽂
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            # 发送数据
            new_socket.send(response_data)
        finally:
            # 关闭服务与客⼾端的套接字
            new_socket.close()


    # 启动web服务器进⾏⼯作
    def start(self):
        while True:
            # 等待接受客⼾端的连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 当客⼾端和服务器建⽴连接程，创建⼦线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            # 设置守护主线程
            sub_thread.setDaemon(True)
            # 启动⼦线程执⾏对应的任务
            sub_thread.start()
# 程序⼊⼝函数
def main():
    print(sys.argv)
    # 判断命令⾏参数是否等于2,
    if len(sys.argv) != 2:
        print("执⾏命令如下: python3 xxx.py 8000")
        return
    # 判断字符串是否都是数字组成
    if not sys.argv[1].isdigit():
        print("执⾏命令如下: python3 xxx.py 8000")
        return
    # 获取终端命令⾏参数
    port = int(sys.argv[1])
    # 创建web服务器对象
    web_server = HttpWebServer(port)
    # 启动web服务器进⾏⼯作
    web_server.start()


if __name__ == '__main__':
    main()

