from socket import *

HOST = gethostname()
PORT = 9999

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))
print
'...waiting for message..'
while True:
    data, address = s.recvfrom(1024)
    print(address, "=>>", data.decode())
    s.sendto(b'UDP server get you message: ' + data, address)
s.close()
