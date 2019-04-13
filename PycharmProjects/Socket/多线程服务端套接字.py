import socket
import threading


def handel_client_socket(tcp_server_socket):
    client_socket, ip_inport = tcp_server_socket.accept()
    print("客户端的IP地址和端口：", ip_inport)
    th1 = threading.Thread(target=handel_client_socket, args=(tcp_server_socket,))
    th1.daemon = True
    th1.start()
    while True:
        receive_data = client_socket.recv(128)
        if not receive_data:
            client_socket.send("客户端关闭。".encode("utf-8"))
            client_socket.close()
            break
        receive_content = receive_data.decode("GBK")
        print(f"客户端{ip_inport}发送的数据为:  {receive_content}")
        send_content = input(f"请回复{ip_inport}：")
        client_socket.send(send_content.encode("utf-8"))


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 8082))
    tcp_server_socket.listen(122)
    while True:
        handel_client_socket(tcp_server_socket)



