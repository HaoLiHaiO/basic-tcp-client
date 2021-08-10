#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host='192.168.1.22'
host = socket.gethostname()
port = 50000
serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket,address = serversocket.accept()

    print("Connection received from %s " %str(address))

    message = 'Thank you for connecting to the server. Test data.' + '\r\n'
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()