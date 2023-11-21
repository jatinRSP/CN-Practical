import socket

# Create a socket object
s = socket.socket()

# Get local machine name
host = socket.gethostname()

port = 9999

# Connect to the server on local computer
s.connect((host, port))

# Receive no more than 1024 bytes
msg = s.recv(1024)

s.close()
print(msg.decode('ascii'))