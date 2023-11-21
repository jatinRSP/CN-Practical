
import socket

s = socket.socket()

print("Socket Created")

s.bind(('localhost',49152))

s.listen(5)

print("Waiting for connection")

# clients = list

c,addr = s.accept()
name = c.recv(1024).decode()
print("Connected with",addr,name)

while True:
    send = input("Enter you message: ")
    c.send(bytes(send,"utf-8"))
    
    msg = c.recv(1024).decode()

    if(msg == "bye"):
        break

    print("Msg From Client: ",msg)