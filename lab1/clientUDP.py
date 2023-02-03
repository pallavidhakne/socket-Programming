import socket
import threading

#python clientUDP.py
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip =  '127.0.0.1' 
port = 2020
client.bind((ip, port))

recvIP ='127.0.0.1'
recvPort = 2023

def receiveMessages(client):
    while(True):
        try:
            data = client.recvfrom(1024)
            data = data[0].decode()
            print(f'\nServer: {data}')
        except:
            print('Try reconnecting.....')
            break

def sendMessages(client):
    message = input("Client: ")
    while message.lower()!='bye':
        client.sendto(message.encode(), (recvIP, recvPort))
        message = input("Client: ")
    client.sendto('\n........Client has left!'.encode(), (recvIP, recvPort))
    client.close()
    msg=input('Enter r to reconnect: ')
    if(msg.lower()=='r'):
        client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.bind((ip,port))
        client.sendto('\n..........Client has reconnected.....'.encode(), (recvIP, recvPort))
        print('You are reconnected...........')
        send= threading.Thread(target=sendMessages,args=(client,))
        send.start()
        receive= threading.Thread(target=receiveMessages,args=(client,))
        receive.start()

receive = threading.Thread(target=receiveMessages,args=(client,))
send = threading.Thread(target=sendMessages,args=(client,))
receive.start()
send.start()