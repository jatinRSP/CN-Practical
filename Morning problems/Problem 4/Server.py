import socket
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Create a socket object
serversocket = socket.socket()

# Get local machine name
host = socket.gethostname()

port = 9999

# Bind to the port
serversocket.bind((host, port))

# Queue up to 5 requests
serversocket.listen(5)

while True:
    # Establish a connection
    clientsocket, addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    clientsocket.send(current_time.encode('ascii'))
    clientsocket.close()

    