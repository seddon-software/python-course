'''
Stream Socket Client
====================

The client code is quite a bit simpler than the server because the client only interacts with a single server,
whereas the server has to interact with multiple clients.  Note this simplicity means the client can be written
as a single threaded application, whereas the server will be multi-threaded.

In this example, the client sends a message to the server and awaits a reply.  On receiving the reply the client
shuts down immediately.  In practice, it is important to realise that the client could continue to send and
receive messages with the server for as long as the application wanted.  In this example, we shutdown immediately
merely to simplify the example. 
'''

import socket
PORT = 7002

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', PORT))    

message = "This is a message from a client."
clientSocket.send(message.encode("UTF-8"))   
response = clientSocket.recv(100) # blocking call
print("Response from server: {}".format(response.decode("UTF-8")), flush="true")

clientSocket.close()
