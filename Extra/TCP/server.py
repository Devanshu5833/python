#!/usr/bin/env python

import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('',8090))

serversocket.listen(5)

while True:
    # Wait for a connection
    print 'waiting for a connection'
    connection, client_address = serversocket.accept()
    print connection
    print client_address
    print connection.recv(1024)
    connection.send("Hello this is from server");
    connection.close();