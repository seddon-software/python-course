'''
Stream Socket Server
====================
When we start up the server it first creates a raw 'socket' and then 'binds' the socket to an end point.  The end 
point is in reality and internet facing buffer inside the kernel capable of receiving data from a client.  The 
server then issues a 'listen' call which converts the raw socket into a listening socket.  Next the server performs 
an 'accept' call.  This is a blocking call and will not return until a client connects.

The client is then started; it also creates a raw 'socket'.  The client then issues a 'connect' call.  This converts 
the client socket into a data transfer socket, automatically binds to a kernel buffer on the client machine and sends
a connect message to the server.

The server then returns from the blocking 'accept' call and creates a second socket for transfering data between the 
server and the client.  The listening socket is retained to allow further clients to connect.  The server can now 
send and receive data with the client and accept further connections; the server create a new thread at this point 
to communicate with the client whilst the original thread continues to wait for further client connections.

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

Note that we have used send and recv to send and receive data, but there are several similar functons you can use
to achieve the same ends. 
'''

'''
The only difference between send() and write(2) is the presence of flags.  With a zero flags argument, 
send() is equivalent to write.  

Also, the following call
           send(sockfd, buf, len, flags);
is equivalent to
           sendto(sockfd, buf, len, flags, NULL, 0);
'''

'''
ssize_t recv(int sockfd, void buf[.len], size_t len, int flags);
ssize_t recvfrom(int sockfd, void buf[restrict .len], size_t len, int flags, struct sockaddr* src_addr, socklen_t* addrlen);
ssize_t recvmsg(int sockfd, struct msghdr *msg, int flags);


The recv(), recvfrom(), and recvmsg() calls are used to receive
messages from a socket.  They may be used to receive data on both
connectionless and connection-oriented sockets.

    The only difference between recv() and read(2) is the presence of
    flags.  With a zero flags argument, recv() is generally
    equivalent to read(2) (but see NOTES).  Also, the following call

    recv(sockfd, buf, len, flags);
is equivalent to
    recvfrom(sockfd, buf, len, flags, NULL, NULL);
'''

#import socket, sys
import sys
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
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

listenSocket = socket(AF_INET, SOCK_STREAM)
listenSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
listenSocket.bind(('', PORT))
listenSocket.listen(5)    # set up backlog buffer
messageNo = 1

print(f"Server starting on port {PORT}")
while True:
    # block until we accept a client connection and then create a second socket
    newsocket, remoteIPandPORT = listenSocket.accept()
    print("SERVER: opened a new connection:", remoteIPandPORT)
    sys.stdout.flush()    
    sockfd = socket(AF_INET, SOCK_STREAM, 0)
    if (sockfd == -1):
        print("socket failed")
        exit(1)
    
    # create a thread to communicate with client leaving original thread to accept further connections
    clientThread = Thread(target=communicateWithClient, args=(newsocket, messageNo))
    messageNo = messageNo + 1
    clientThread.start()
