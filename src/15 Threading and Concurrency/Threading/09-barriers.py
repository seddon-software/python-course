############################################################
#
#    barriers
#
############################################################



from threading import Thread, Barrier
import time


# In this example a server a 4 clients synchronize by waiting on a barrier
# in their respective threads.  When all five threads are waiting, 
# the barrier is removed and all 5 threads continue.

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
