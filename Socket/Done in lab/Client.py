#CLIENT

import socket

c = socket.socket()

c.connect(('localhost', 60001))

name = input("Enter your name: ")

c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())

c.close()