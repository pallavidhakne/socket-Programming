import socket
import threading

port = 9999 # high number
ip = '127.0.0.1' # localhost

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((ip, port))  # bind the socket to address
server_sock.listen()
print('server start!!')

clients = []  # list of clients
c_addr = []  # list of clients' address

def broadcast(msg):   # send data to all clients connected to the server
    for c in clients:
        c.send(msg)


def event_check(client):  # event check, if the client enter 'exit', close the client
    # else, broadcast that message
    while True:
        try:
            msg = client.recv(1024)
            # broadcast(msg)
            if msg.decode('utf-8') == "exit":
                index = clients.index(client)
                clients.remove(client)
                temp = c_addr[index]
                del c_addr[index]
                client.close()
                broadcast("{} disconnected!".format(temp).encode('utf-8'))
                break
            else:
                broadcast(msg)

        except:
            index = clients.index(client)
            clients.remove(client)
            temp = c_addr[index]
            del c_addr[index]
            client.close()
            broadcast("{} disconnected!".format(temp).encode('utf-8'))
            break


while True:
    clientsock, addr = server_sock.accept()
    print("connected by", addr)
    clients.append(clientsock)
    c_addr.append(addr)
    clientsock.send('Connected to server'.encode('utf-8'))
    thread = threading.Thread(target=event_check, args=(clientsock,))
    thread.start()
