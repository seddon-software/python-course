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

