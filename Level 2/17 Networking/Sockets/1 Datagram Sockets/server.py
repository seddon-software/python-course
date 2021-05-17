############################################################
#
#    datagram server
#
############################################################

# datagrams are like emails - you send and receive
# this is not really a server - it receives first and sends later

import socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.bind (( '', 7002))

# get message from client
data, client = mySocket.recvfrom(100)
print('We have received a datagram from', client) 

# send a response
mySocket.sendto(b'This is the response from the server', client )

# remove socket object
del mySocket

1