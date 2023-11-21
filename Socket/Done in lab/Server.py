# SERVER

import socket

s = socket.socket()

print("Socket successfully created")

s.bind(('localhost', 60001))

s.listen(5)

print("socket is listening")

while True:
    c, addr = s.accept()

    name = c.recv(1024).decode()

    print("Connected with", addr, name)

    c.send(bytes("Welcome to the server", 'utf-8'))

    c.close()