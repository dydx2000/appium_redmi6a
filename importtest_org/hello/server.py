import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8090))
sk.listen()

con, addr = sk.accept()
while True:

    msg = con.recv(1024)

    msg = msg.decode('utf-8')

    print("clent: {}".format(msg))
    if msg == "bye":
        break

    reply = input("server: ").encode('utf-8')
    con.send(reply)

con.close()
sk.close()
