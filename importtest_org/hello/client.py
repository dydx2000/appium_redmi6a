import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8090))

while True:
    send_msg = input("client: ").encode('utf-8')

    sk.send(send_msg)
    if send_msg.decode('utf-8') == 'bye':
        break

    res = sk.recv(1024)
    print("server: {}".format(res.decode('utf-8')))

    if res.decode('utf-8') == 'bye':
        break

sk.close()
