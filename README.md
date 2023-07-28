# TCP Socket Programming with Python

This is a simple Python example that shows how to use TCP sockets for network communication between a server and clients. The server listens for incoming connections from clients and handles each client in a separate thread. The client connects to the server and runs two threads to receive and send messages over the network. It consists of four Python files, `server.py` and `client1.py`, `client2.py` and `client3.py` that communicate with each other over a network using TCP sockets.

## Running

1. Clone the repository or download the files to your local.

2. In one terminal, run the `server.py` first.
```
python server.py
```
This will start the server and it will be ready to accept connections from clients (listen on `127.0.0.1:9999`). 

3. In the other terminal, run the `client1.py`, `client2.py` and `client3.py`.
```
python client1.py
```
This will start the client and it will connect to the server at `127.0.0.1:9999`.

4. To communicate between clients, enter the messages in the console. The server will act as a mediator between clients by receiving messages from one client and sending them to another client.

## How it Works

The `server.py` creates a socket and binds it to a specific port number. It then listens for incoming connections from clients. When a client connects, it accepts the connection and each client is handled in a separate thread. Then, it starts a loop to receive messages from the client. And it sends back them to all clients(broadcast). 

The `client.py` creates a socket and connects to the server using the server's IP address and port number. It starts a loop where it listens for incoming messages and user input continuously. It consists of two functions, `send()` and `recv()`, which run in separate threads to handle sending and receiving messages over the network.

## TCP flow
![TCP flow](sockets-tcp-flow.webp)


