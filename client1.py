import socket
import threading

ip = '127.0.0.1'  # localhost
port = 9999

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((ip, port))  # connect to the socket!!
print('Connected!')


# recv : receive the data, send : send the data
def recv():
    while True:
        try:
            msg1 = clientSock.recv(1024).decode('utf-8')
            print("client1" +msg1)
        except:
            clientSock.close()
            break


def send():
    while True:
        msg = input()
        clientSock.send(msg.encode('utf-8'))


# threading
sender = threading.Thread(target=send)
receiver = threading.Thread(target=recv)

sender.start()
receiver.start()
