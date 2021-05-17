############################################################
#
#    fine control
#
############################################################

import http.server
import cgi, random, sys

class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        f = None
        try:
            f = open("cgi" + self.path, "r")
        except:
            self.send_error(404, "File name missing")
            return
            
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # download file
        for line in f:
            line = line.encode('UTF-8')
            self.wfile.write(line)

PORT = 8002
httpd = http.server.HTTPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()


"""
try the following URL's
    http://localhost:8002/f1.html
    http://localhost:8002/f2.html
    http://localhost:8002/f3.html
"""
