############################################################
#
#    stream socket server
#
############################################################

# unicode_string.encode(encoding) is also more Pythonic because its inverse is 
# byte_string.decode(encoding) and symmetry is nice.
# default encoding is UTF-8


import socket, sys
from threading import Thread

PORT = 7002

def communicateWithClient(newsocket, messageNo):
    # wait for message and echo
    message = newsocket.recv(100)
    print("SERVER:", message.decode("UTF-8"))
    sys.stdout.flush()
    
    # send response and close socket immediately
    response = "message {0} - {1}".format(messageNo, message.decode("UTF-8"))
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
    # accept client connections
    newsocket, remoteIPandPORT = listenSocket.accept()
    print("SERVER: opened a new connection:", remoteIPandPORT)
    sys.stdout.flush()
    clientThread = Thread(target=communicateWithClient, args=(newsocket, messageNo))
    messageNo = messageNo + 1
    clientThread.start()
