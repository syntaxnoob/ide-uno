#!/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2205))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f'Connection from{address} has been established.')
    clientsocket.send(bytes("Welcome!", "utf-8"))
