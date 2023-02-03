import socket
import threading

port=2022
host='127.0.0.1'
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host,port))
serverSocket.listen()
print("Server is waiting for client......")
client , clientAddress = serverSocket.accept()
print("Connected to Client with IP:" +clientAddress[0] + " and Port:" +str(clientAddress[1]))

def receive(client):
    while True:
            try:
                message = client.recv(1024).decode('utf-8')
                print(message)
            except:
                # client.close()
                print('\nClient Disconnected!')
                break
def send(client):
       while True:
            message =input()
            try:
                client.send(f'Server: {message}'.encode('utf-8'))
            except:
                    client , clientAddress = serverSocket.accept()
                    print('\nClient Reconnected......')
                    client.send(f'Server: {message}'.encode('utf-8'))
                    thread = threading.Thread(target=receive,args=(client,))
                    thread.start()
                    thread = threading.Thread(target=send,args=(client,))
                    thread.start()
                    break
    
        
    
thread = threading.Thread(target=receive,args=(client,))
thread.start()
thread = threading.Thread(target=send,args=(client,))
thread.start()