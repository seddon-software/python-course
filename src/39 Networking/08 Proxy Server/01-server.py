# https://www.tutorialspoint.com/creating-a-proxy-webserver-in-python

import SimpleWebSocketServer
import SimpleHTTPSServer
import urllib
PORT = 8261
class JustAProxy(SimpleHTTPSServer.SimpleWebSocketServer):
   def do_GET(self):
      url=self.path[1:]
      self.send_response(200)
      self.end_headers()
      self.copyfile(urllib.urlopen(url), self.wfile)
      print(url)

httpd = SimpleWebSocketServer.SimpleWebSocketServer('localhost',PORT,JustAProxy)
print ("Proxy Server at" , str(PORT))
httpd.serveforever()