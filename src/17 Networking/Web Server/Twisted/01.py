from twisted.internet.protocol import Protocol

class MyProtocol(Protocol):

    def connectionMade(self):
        self.transport.write(b"An apple a day keeps the doctor away\r\n") 
        self.transport.loseConnection()

from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class MyFactory(Factory):
    def buildProtocol(self, addr):
        return MyProtocol()

# 8007 is the port you want to run under. Choose something >1024
endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(MyFactory())
reactor.run()
