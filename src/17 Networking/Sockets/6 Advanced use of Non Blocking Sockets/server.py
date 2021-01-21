# taken from
# http://pymotw.com/2/select/

import logging
import select
import socket
import sys
import Queue


def main():
    setupLogging()
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)   # non blocking
    
    # Bind the socket to the port
    server_address = ('localhost', 10000)
    logging.info('starting up on {0} port {1}'.format(server_address[0], server_address[1]))
    server.bind(server_address)
    
    server.listen(5)    # listen for incoming connections
    inputs = [ server ] # sockets from which we expect to read
    outputs = [ ]       # sockets to which we expect to write
    message_queues = {} # outgoing message queues (socket:Queue)
    mainLoop(inputs, outputs, message_queues, server)
    
def setupLogging():
    # as no logfile specified, use the console
    FORMAT = "SERVER: %(message)s"
    #logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    #logging.basicConfig(level=logging.WARNING)

def handleInputs(s, inputs, message_queues):
    connection, client_address = s.accept()
    logging.debug('new connection from {0}:{1}'.format(client_address[0], client_address[1]))
    connection.setblocking(0)
    inputs.append(connection)

    # Give the connection a queue for data we want to send
    message_queues[connection] = Queue.Queue()        
    return connection, client_address

def closeConnection(client_address, s, inputs, outputs, message_queues):
    # Interpret empty result as closed connection
    logging.debug('closing {0}:{1} after reading no data'.format(client_address[0], client_address[1]))
    # Stop listening for input on the connection
    if s in outputs:
        outputs.remove(s)
    inputs.remove(s)
    s.close()    
    # Remove message queue
    del message_queues[s]

def readClientData(s, outputs, message_queues, data):
    # A readable client socket has data
    logging.info('received "{0}" from {1}'.format(data, s.getpeername()))
    message_queues[s].put(data)
    # Add output channel for response
    if s not in outputs:
        outputs.append(s)

def handleOutputs(s, outputs, message_queues):
    try:
        next_msg = message_queues[s].get_nowait()
    except Queue.Empty:
        # No messages waiting so stop checking for writability.
        logging.debug('output queue for {0} is empty'.format(s.getpeername()))
        outputs.remove(s)
    else:
        logging.info('sending "{0}" to {1}'.format(next_msg, s.getpeername()))
        s.send(next_msg)

def handleExceptionalConditions(s, inputs, outputs, message_queues):
    print('handling exceptional condition for {0}', s.getpeername())
    # Stop listening for input on the connection
    inputs.remove(s)
    if s in outputs:
        outputs.remove(s)
    s.close()    
    # Remove message queue
    del message_queues[s]

def mainLoop(inputs, outputs, message_queues, server):
    while inputs:
        # Wait for at least one of the sockets to be ready for processing
#        report('waiting for the next event')
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        
        # Handle inputs
        for s in readable:
            if s is server:
                connection, client_address = handleInputs(s, inputs, message_queues)
#                 # A "readable" server socket is ready to accept a connection
#                 connection, client_address = s.accept()
#                 logging.debug('new connection from {0}:{1}'.format(client_address[0], client_address[1]))
#                 connection.setblocking(0)
#                 inputs.append(connection)
    
#                 # Give the connection a queue for data we want to send
#                 message_queues[connection] = Queue.Queue()        
            else:
                data = s.recv(1024)
                if data:
                    readClientData(s, outputs, message_queues, data)
#                     # A readable client socket has data
#                     logging.info('received "{0}" from {1}'.format(data, s.getpeername()))
#                     message_queues[s].put(data)
#                     # Add output channel for response
#                     if s not in outputs:
#                         outputs.append(s)
                else:
                    closeConnection(client_address, s, inputs, outputs, message_queues)
#                     # Interpret empty result as closed connection
#                     logging.debug('closing {0}:{1} after reading no data'.format(client_address[0], client_address[1]))
#                     # Stop listening for input on the connection
#                     if s in outputs:
#                         outputs.remove(s)
#                     inputs.remove(s)
#                     s.close()
#     
#                     # Remove message queue
#                     del message_queues[s]
        # Handle outputs
        for s in writable:
            handleOutputs(s, outputs, message_queues)
#             try:
#                 next_msg = message_queues[s].get_nowait()
#             except Queue.Empty:
#                 # No messages waiting so stop checking for writability.
#                 logging.debug('output queue for {0} is empty'.format(s.getpeername()))
#                 outputs.remove(s)
#             else:
#                 logging.info('sending "{0}" to {1}'.format(next_msg, s.getpeername()))
#                 s.send(next_msg)
        # Handle "exceptional conditions"
        for s in exceptional:
            handleExceptionalConditions()
#             print('handling exceptional condition for {0}', s.getpeername())
#             # Stop listening for input on the connection
#             inputs.remove(s)
#             if s in outputs:
#                 outputs.remove(s)
#             s.close()
#     
#             # Remove message queue
#             del message_queues[s]
        
main()
