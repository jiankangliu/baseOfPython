import socket
if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 8082))
    tcp_server_socket.listen(122)
    while True:
        client_socket, ip_inport = tcp_server_socket.accept()
        print("客户端的IP地址和端口：", ip_inport)
        while True:
            recv_data = client_socket.recv(128)
            if not recv_data:
                client_socket.close()
                break
            recv_content = recv_data.decode('GBK')
            print("客户端发送的数据为：", recv_content)
            send_content = input("请输入：")
            send_data = send_content.encode("utf-8")
            client_socket.send(send_data)




