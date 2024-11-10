#!/usr/bin/env python3

import socket

HOST = ''    # same as 127.0.0.1 standard loopback interface address (localhost)
PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # SOCK_STREAM for TCP / SOCK_DGRAM for UDP
    s.bind((HOST, PORT))
    s.listen()    # make a queue for client connection we can define max otherwise max is defined by system 
    print(f"Now server is Listening on port : {PORT}")
    print(f"DEBUG: socket -> {s}")
    (conn, addr) = s.accept()    # Block untill receive something
    print(f"DEBUG: con: {conn}")
    with conn:
        print(f"connected by: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)