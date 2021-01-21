############################################################
#
#    simple http server
#
############################################################

import http.server
import socketserver

# minimal web server.  
# serves files relative to the current directory.

PORT = 8001
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()

"""
try the following URL's
    http://localhost:8001/cgi/f1.html
    http://localhost:8001/cgi/f2.html
    http://localhost:8001/cgi/f3.html
"""
