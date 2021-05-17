# taken from
# http://pymotw.com/2/select/

import socket
import sys
import logging
import time
import random

def myGenerator(clientId):
    for n in range(1,4): 
        yield "{0}: line {1}".format(clientId, n)
    return

def main():
    time.sleep(random.randint(5, 10))   # random delay
    if(len(sys.argv) == 2):
        clientId = sys.argv[1]
    else:
        clientId = "1"
    
    # as no logfile specified, use the console
    FORMAT = "CLIENT: %(message)s"
    #logging.basicConfig(level=logging.INFO, format=FORMAT)
    #logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    logging.basicConfig(level=logging.WARNING)
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('localhost', 10000))    
    
    for message in myGenerator(clientId):
    # send message
        logging.debug('{0}: sending "{1}"'.format(clientSocket.getsockname(), message))
        logging.info('{0}'.format(message))
        time.sleep(random.randint(5, 10)/10.0)
        clientSocket.send(message)
    
    # read response
        data = clientSocket.recv(1024)
        logging.debug('{0}: received "{1}"'.format(clientSocket.getsockname(), data))
        logging.info('{0}'.format(data))
        if not data:
            logging.debug('closing socket {0}'.format(clientSocket.getsockname()))
            clientSocket.close()

main()
