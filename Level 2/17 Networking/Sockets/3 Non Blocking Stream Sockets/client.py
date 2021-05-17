############################################################
#
#    stream socket client
#
############################################################

import socket, time

PORT = 7002

def sendMessages(PORT):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('localhost', PORT))
    message = "This is a message from a client"
    clientSocket.send(message.encode("UTF-8"))
    clientSocket.close()

for n in range(10):
    sendMessages(PORT)
    time.sleep(5)
