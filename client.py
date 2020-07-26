#!/bin/python3.8

import socket

HEADERSIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2208))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new message lenght = {msg[:HEADERSIZE]}")
            msglenght = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg.decode('utf-8')
        if len(full_msg)-HEADERSIZE == msglenght:
            print('the full message is reseaved.')
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''
    print(full_msg)
