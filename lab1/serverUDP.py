import socket
import threading

# python serverUDP.py
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = '127.0.0.1'
port = 2023
s.bind((ip, port))
print('Server is waiting for client.......')
recvIP = '127.0.0.1'
recvPort = 2020

def receiveMessages():
    while(True):
            data = s.recvfrom(1024)
            data = data[0].decode()
            print(f'\nClient: {data}')
       

def sendMessages():
    while(True):
        message = input("Server: ")
        s.sendto(message.encode(), (recvIP, recvPort))


receive = threading.Thread(target=receiveMessages)
send = threading.Thread(target=sendMessages)
    
receive.start()
send.start()