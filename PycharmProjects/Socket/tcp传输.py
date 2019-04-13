import socket
if __name__ == '__main__':
    # AF_INET:表示ipv4    SOCK_STREAM:tcp传输协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(("192.168.6.128", 8999))
    content = input("请输入内容：")
    send_data = content.encode("utf-8")
    tcp_client_socket.send(send_data)
    recv_data = tcp_client_socket.recv(1024)
    print(recv_data.decode("utf-8"))
    tcp_client_socket.close()






