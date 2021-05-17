############################################################
#
#    server
#
############################################################

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

# specify THreadingMixIn first because otherwise it will override 
# methods in TCPServer 
class MyServer(socketserver.ThreadingMixIn, 
               socketserver.TCPServer): pass

server = MyServer(("localhost", 7001), MyRequestHandler)
print("Server on port 7001")

server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()


