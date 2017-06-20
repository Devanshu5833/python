#!/usr/bin/env python

#import modules
import socket
import sys

socketclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketclient.connect(('localhost',8090))

socketclient.send("HI my name is devanshu oza")

print socketclient.recv(15)

socketclient.close()

