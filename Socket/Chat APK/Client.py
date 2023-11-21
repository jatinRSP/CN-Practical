import socket

c = socket.socket()

c.connect(('localhost',49152))
name = input("Enter your name: ")
c.send(bytes (name , "utf-8"))
while True:
    print("Msg From Server: ",c.recv(1024).decode())

    send = input("Enter you message: ")

    c.send(bytes(send,"utf-8"))
    
    if(send == "bye"):
        break