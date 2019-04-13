import socket
service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
service_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
service_socket.bind(("", 8888))
service_socket.listen(128)
while True:
    client_socket, ip_port = service_socket.accept()
    print("客户端连接：", ip_port)
    recv_data = client_socket.recv(1024)
    print(recv_data.decode("gbk"))
    # response报文
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server: PWS1.0\r\n"
    with open("index.html", "rb") as f:
        response_body = f.read()
    # send_data = "hello world"
    send_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
    client_socket.send(send_data)
    client_socket.close()






