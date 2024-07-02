'''
Barriers
========

Barriers are yet another synchronization object.  

A barrier is created with a count and a timeout:
            b = Barrier(5, timeout=10)

In this example a server and 4 clients synchronize by waiting on this barrier in their respective threads:
            b.wait()
            
When all five threads are waiting, the barrier is satisfied and the Python interpreter removes the barrier and 
all 5 threads continue.
'''

from threading import Thread, Barrier
import time

b = Barrier(5, timeout=10)

class Server:
    def __init__(self):
        print("server initializing ...")
        self.thread = Thread(target=self)
        self.thread.start()

    def __call__(self):
        time.sleep(5)
        b.wait()
        print("server ready to accept connections")
        
    def connect(self, client):
        print(f"{client.name} has connected")
        
class Client:
    def __init__(self, name, server):
        self.name = name
        self.server = server
        print(f"{self.name} waiting to connect")
        self.thread = Thread(target=self)
        self.thread.start()
    
    def __call__(self):
        b.wait()
        self.server.connect(self)

def main():
    server = Server()
    client1 = Client("client1", server)
    client2 = Client("client2", server)
    client3 = Client("client3", server)
    client4 = Client("client4", server)
    
    server.thread.join()
    client1.thread.join()
    client2.thread.join()
    client3.thread.join()
    client4.thread.join()
    
main()
