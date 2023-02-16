'''
Demo with Multiple Clients
==========================
Here we show how the server can interact with multiple clients.  Note that the server will create a separate
thread for each client; this is called thread affinity.  Thread affinity is simple to program, but is not the
most effecient way for the server to operate because of the large overhead of creating so many threads.

Dedicating a thread to each client leads to inefficiences particularly when the client has periods where it 
doesn't contact the server.  At such times, the server thread could be used to communicate with a different
client, leading to what is called thread pooling.  Recall that the GIL will make cpu intensive operations
inefficient, but here we are IO intensive, so thread pooling will give a performance boost (see later examples).
'''

import subprocess, sys
from threading import Thread

# python executable is given by: sys.executable

def startServer():
    # server keeps running, so start in on a separate thread 
    params = [sys.executable, "server.py"]
    serverThread = Thread(target=subprocess.call, args=(params,))
    serverThread.start()

def startClients(n):
    for i in range(n):
        subprocess.call([sys.executable, "client.py"])
   
startServer()
startClients(20)

