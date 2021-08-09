#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.1.22'
host = socket.gethostname()
port = 3300
print(host)
clientsocket.connect((host, port))

# max amount of data client accepts at once
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode("ascii"))