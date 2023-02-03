import socket
import threading
#python clientTCP.py

host='127.0.0.1'
port=2022
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))
print("Successfully connected to server!!")

        
def client_receive(client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                print(message)
            except:
                print('\nDisconnected!')
                break


def client_send(client):
        message =input()
        while message.lower()!='bye':
            try:
                client.send(f'Client: {message}'.encode('utf-8'))
                message =input()
            except:
                print('You need to reconnect...')
                break
        client.close()
        msg=input('Enter r to reconnect: ')
        if(msg.lower()=='r'):
            client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host,port))
            print('You are reconnected...........')
            receive_thread = threading.Thread(target=client_receive,args=(client,))
            receive_thread.start()
            send_thread = threading.Thread(target=client_send,args=(client,))
            send_thread.start()


receive_thread = threading.Thread(target=client_receive,args=(client,))
receive_thread.start()

send_thread = threading.Thread(target=client_send,args=(client,))
send_thread.start()
