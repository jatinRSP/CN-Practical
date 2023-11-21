import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

server_socket.bind((host, port))
server_socket.listen(1)

print(f'Listening on port {host}:{port}...')
client_socket, addr = server_socket.accept()
print(f'Got a connection from {addr}')

data = client_socket.recv(1024)
print(f'Received: {data}')

client_socket.close()
