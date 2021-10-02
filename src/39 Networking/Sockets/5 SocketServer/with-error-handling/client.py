############################################################
#
#    client
#
############################################################

import socket
import time

def SendAndReceive(message):
    message = message.encode('UTF-8')
    mySocket.sendall(message)
    response = mySocket.recv(100)
    response = response.decode('UTF-8')
    print(response)
    

print("Client")
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('localhost', 7001))

# client must send a legal Python expression or server will close connection
try:
    SendAndReceive('25 * 40')
    SendAndReceive('15 + 33 + 127')
    SendAndReceive('junk....')
except:
    mySocket.close()


