import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

client_socket.connect((host, port))

message = 'Hello, World!'
client_socket.send(message.encode('utf-8'))

client_socket.close()