############################################################
#
#    client
#
############################################################

import socket
import time

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to well known address
mySocket.connect(('localhost', 2525))

# send and receive messages
for n in range(1, 20):
    message = 'This is message {0} from client'.format(n)
    message = message.encode('UTF-8')
    mySocket.send(message)
    
    response = mySocket.recv(100).rstrip(); 
    response = response.decode("UTF-8") 
    print("{0}:".format(response))
    time.sleep(1)

mySocket.send(b'exit')
mySocket.close()


1
