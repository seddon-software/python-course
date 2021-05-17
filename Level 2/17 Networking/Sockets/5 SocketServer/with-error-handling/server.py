############################################################
#
#    server
#
############################################################

import socketserver
PORT = 7001
class MyRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while(True):
            message = self.request.recv(100).rstrip();
            message = message.decode("UTF-8")
            # evaluate message
            response = str(eval(message))
            response = response.encode("UTF-8")
            self.request.sendall(response)
        
class MyServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.allow_reuse_address = True
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)
        
    def handle_error(self, request, client_address):        
        message = "Illegal request, closing connection"
        message = message.encode("UTF-8")
        request.sendall(message)

print("Server on port:", PORT)
server = MyServer(("localhost", PORT), MyRequestHandler)
server.serve_forever()
