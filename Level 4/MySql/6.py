import http.server
import socketserver, os

os.chdir("templates")
PORT = 7003

# Set the handler to use SimpleHTTPRequestHandler
Handler = http.server.SimpleHTTPRequestHandler

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
