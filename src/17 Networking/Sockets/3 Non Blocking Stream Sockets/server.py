# taken from
# http://pymotw.com/2/select/

import logging
import select
import socket
import sys
import time
#import Queue

PORT = 7002

def main():
    print("Server starting on port: ", PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(0)   # non blocking
    server.bind(('', PORT))
    server.listen(5)    # set up backlog buffer

    inputs = [ server ] # sockets from which we expect to read
    outputs = [ ]       # sockets to which we expect to write
    exceptions = [ server ]
    timeout = 100.0      # in seconds

    while(True):
        readList, writeList, exceptionsList = select.select(inputs, outputs, exceptions, timeout)
        for s in readList:
            if s is server:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
            if s is connection:
                data = connection.recv(1024)
                if data:
                    print(data.decode("UTF-8"), flush="true")
                else:
                    print(".", end="", flush="true")
        time.sleep(0.25)
        
main()