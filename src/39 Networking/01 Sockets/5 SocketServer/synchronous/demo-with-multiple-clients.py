import subprocess, time, sys
from threading import Thread
from subprocess import Popen

def startServer():
    # server keeps running, so start in on a separate thread 
    params = [ sys.executable, "server.py" ]
    serverThread = Thread(target=subprocess.call, args=(params,))
    serverThread.start()

def startClients(n):
    for i in range(n):
        cmd = "{} client.py {}".format(sys.executable, i)        
        p = Popen(cmd.split()) # clients run asynchronously
   
startServer()
time.sleep(5)
startClients(3)

