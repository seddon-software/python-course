############################################################
#
#    server
#
############################################################

import socketserver

class MyRequestHandler(socketserver.StreamRequestHandler):
    def handle( self ):
        while(True):
            message = self.request.recv(100).rstrip();
            message = message.decode("UTF-8")
            if message == "exit": break
            # echo back message
            message = message.encode("UTF-8")
            self.request.sendall(message)

print("Server on port 2525")

socketserver.TCPServer.allow_reuse_address = True
server = socketserver.TCPServer(("", 2525), MyRequestHandler)
server.serve_forever()
