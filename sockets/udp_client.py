#!/usr/bin/env python

from socket import *

HOST = gethostname()
PORT = 9999

s = socket(AF_INET, SOCK_DGRAM)
s.bind(("",9998))
s.connect((HOST, PORT))
while True:
    message = input('send message:>>')
    s.sendall(message.encode())
    data = s.recv(1024).decode()
    print(data)
s.close()