import socket
if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.6.128', 8080))
    content = input('请输入发送内容：')
    send_data = content.encode('utf-8')
    client_socket.send(send_data)
    recv_data = client_socket.recv(1024)
    print(recv_data)
    client_socket.close()




