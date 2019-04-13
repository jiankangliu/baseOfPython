import socket
def main():
    pass
    # 输入网址，DNS解析，连接服务器
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(("tlias3.boxuegu.com", 80))
    http_request_data =
    # 拼接请求报文，发送服务器
    # 接收响应报文
    # 关闭连接


if __name__ == '__main__':
    main()