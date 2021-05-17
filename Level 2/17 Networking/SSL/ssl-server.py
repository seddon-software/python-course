import traceback
import socket
import ssl
import http.server

PORT = 8443

def do_request(tcp_stream, from_addr):
    filename = tcp_stream.read()
    filename = filename.decode('UTF-8')
    filename = "files/" + filename
    try:
        f = open(filename,"r")
        all = "".join(f.readlines())
        f.close()
    except Exception as e:
        all = "Invalid File"
        
    tcp_stream.write(all.encode('UTF-8'))
    
    
sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sd.bind(('', PORT))
sd.listen(5)


print(("serving on port", PORT))

while True:
    try:
        newsocket, from_addr = sd.accept()
        ssl_socket = ssl.wrap_socket(newsocket,
                                     server_side=True,
                                     keyfile='certificates/server.key',
                                     certfile='certificates/server.crt',
                                     ssl_version=ssl.PROTOCOL_TLSv1_2)
        
        do_request(ssl_socket, from_addr)
        
    except Exception:
        traceback.print_exc()

