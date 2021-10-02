############################################################
#
#    stream socket client
#
############################################################

import socket, time

PORT = 7002

def sendMessages(PORT, n):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('localhost', PORT))
    message = f"This is a message from client {n}"
    clientSocket.send(message.encode("UTF-8"))
    clientSocket.close()

for n in range(10):
    sendMessages(PORT, n)
    time.sleep(5)
