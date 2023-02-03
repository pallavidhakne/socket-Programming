import threading
import socket
host = '127.0.0.1'
port = 2022
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
nicknames = []


def display(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            display(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            display(f'{nickname} has left the chat room!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        print('Server is listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('nickname?'.encode('utf-8'))
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)
        print(f"The nickname of this client is: {nickname}")
        display(f"{nickname} has entered the chat room".encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()