############################################################
#
#    datagram client
#
############################################################

# datagrams are like emails - you send and receive
# this is not really a client - it sends first and receives later

import socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send a message to the server
mySocket.sendto(b'This is a message from the client', ('localhost', 7002))

# pick up the (optional) response
data, server = mySocket.recvfrom(100)
data = data.decode()
print(data)