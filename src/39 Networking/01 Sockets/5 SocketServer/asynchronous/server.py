############################################################
#
#    server (asynchronous - with threading)
#
############################################################


'''
Adding threading or forking support to a server is as simple as 
including the appropriate mix-in in the class hierarchy for the
server. The mix-in classes override process_request() to start
a new thread or process when a request is ready to be handled, 
and the work is done in the new child.
'''

import socketserver
import socket
import threading

class MyRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        try:
            while(True):
                message = self.request.recv(100).rstrip()
                message = message.decode("UTF-8")
                print("SERVER: ", message)
                if message == "exit": break
                # echo request back to client
                message = message.encode("UTF-8")
                self.wfile.write(message)
        except socket.error as e:
            print("error ...")

# specify ThreadingMixIn first because otherwise it will override 
# methods in TCPServer 
class MyServer(socketserver.ThreadingMixIn, 
               socketserver.TCPServer): pass

server = MyServer(("localhost", 8001), MyRequestHandler)
print("Server on port 8001")

server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()


