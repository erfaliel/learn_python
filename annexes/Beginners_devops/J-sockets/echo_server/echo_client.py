#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))         # connect to the echo server
    s.sendall(b'Hello, world')      # send message
    data = s.recv(1024)             # capture response from the echo server

print(f"Received : {repr(data)}")