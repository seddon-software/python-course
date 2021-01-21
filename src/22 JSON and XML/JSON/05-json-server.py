############################################################
#
#    fine control
#
############################################################

import http.server
import cgi, random, sys
import cgitb, urllib.parse
import urllib.parse
import json
cgitb.enable()

class Handler(http.server.BaseHTTPRequestHandler):
    def incrementBy(self, data, n):
        d = {}
        for key, values in data.items():
            d[key] = []
            for value in values:
                value = str(int(value) + n)
                d[key].append(value)
        return d

    def do_GET(self):
        print("request: ", self.requestline)
        parsedUrl = urllib.parse.urlparse(self.path) # returns a 6-tuple
        queryString = parsedUrl[4]  # query string is 5th component
        print("queryString:", queryString)
        data = urllib.parse.parse_qs(queryString)
        
        # the query string will be a dictionary
        # keys are the ids
        # values are lists of the values assigned to the ids
        # note query strings can repeat ids as in:
        #    x=1&y=2&z=3&x=4
        try:
            data = self.incrementBy(data, 100)
        except:
            self.send_error(404, "Error in query string: non numeric values found")
            return
            
        # convert Python dictionary to JSON
        jsonString = json.dumps(data)

        # send JSON response            
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
            
        jsonAsBytes = jsonString.encode("UTF-8")
        self.wfile.write(jsonAsBytes)

PORT = 8002
SERVER = "localhost"
httpd = http.server.HTTPServer((SERVER, PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()


"""
try the following URL's
    http://localhost:8002/f1.html
    http://localhost:8002/f2.html
    http://localhost:8002/f3.html
"""
