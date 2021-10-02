import time
import socket

def untilServerRunning(server, port):
    while True:
        try:
            s = socket.socket()
            s.connect((server, port))        
        except:
            if s: s.close()
            time.sleep(1)
        else:
            s.close()
            break
