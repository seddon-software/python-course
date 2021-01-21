############################################################
#
#    stream socket client
#
############################################################

import socket
PORT = 7002

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', PORT))    

message = "This is a message from a client."
clientSocket.send(message.encode("UTF-8"))   
response = clientSocket.recv(100) # blocking call
print("Response from server: {}".format(response.decode("UTF-8")), flush="true")

clientSocket.close()
