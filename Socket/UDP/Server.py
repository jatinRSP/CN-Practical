
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(data.decode())

    response = "Hello, client!"
    server_socket.sendto(response.encode(), client_address)