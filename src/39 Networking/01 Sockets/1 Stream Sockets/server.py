'''
Stream Socket Server
====================
When we start up the server it first creates a raw 'socket' and then 'binds' the socket to an end point.  The end 
point is in reality and internet facing buffer inside the kernel capable of receiving data from a client.  The 
server then issues a 'listen' call which converts the raw socket into a listening socket.  Next the server performs 
an 'accept' call.  This is a blocking call and will not return until a client connects.

The client is then started and also creates a raw 'socket'.  The client then issues a 'connect' call.  This converts 
the client socket into a data transfer socket, automatically binds to a kernel buffer on the client machine and sends
a connect message to the server.

The server then returns from the blocking 'accept' call and creates a second socket for transfering data between the server
and the client.  The listening socket is retained to allow further clients to connect.  The server can now either
send and receive data with the client or accept further connections.  To allow the server to both it is normal to 
create a new server thread at this point to communicate with the first client.  The original thread continues to
wait for further client connections.

Data transfer between server and client proceeds using 'send' and 'recv' calls.  Note that all data sent across
the network has to be converted to bytes for transmission.  You then need to decode the bytes at the receiving
end for interpretation.  It is common to use UTF-8 as the encoding.

              SERVER                CLIENT
            ┌─────────┐
            │ socket  │
            ├─────────┤
            │  bind   │
            ├─────────┤
            │ listen  │
            ├─────────┤
            │ accept  │<
            ├─────────┤ \
                |       \          ┌─────────┐
                |        \         │ socket  │
                |         \        ├─────────┤
                |          \-------│ connect │
            (new thread)           ├─────────┤
                |                 /│ send    │
                |                / ├─────────┤
            ├─────────┤         /
            │  recv   │<-------/  
            ├─────────┤             
            │  send   │\            
            ├─────────┤ \             
                |        \         ├─────────┤
                |         \------->│  recv   │
                |                  ├─────────┤
                |                  │  close  │
                |                  └─────────┘
            ├─────────┤
            │  close  │
            └─────────┘
'''


import socket, sys
from threading import Thread

PORT = 7002

def communicateWithClient(newsocket, messageNo):
    # wait for message and echo
    message = newsocket.recv(100)       # receive bytes
    print("SERVER:", message.decode("UTF-8"))   # decode the bytes
    sys.stdout.flush()
    
    # send response and close socket immediately
    response = f"message {messageNo} - {message.decode('UTF-8')}"
    newsocket.send(response.encode("UTF-8"))
    print(f"closing {newsocket}")
    newsocket.close()

listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listenSocket.bind(('', PORT))
listenSocket.listen(5)    # set up backlog buffer
messageNo = 1

print(f"Server starting on port {PORT}")
while True:
    # block until we accept a client connection and then create a second socket
    newsocket, remoteIPandPORT = listenSocket.accept()
    print("SERVER: opened a new connection:", remoteIPandPORT)
    sys.stdout.flush()    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        perror("socket failed")
        exit(1);
    }
    
    # create a thread to communicate with client leaving original thread to accept further connections
    clientThread = Thread(target=communicateWithClient, args=(newsocket, messageNo))
    messageNo = messageNo + 1
    clientThread.start()
