############################################################
#
#    Bridge
#
############################################################

#        Logging ------------------- Service
#          ^                            ^
#          |                            |
#      ----------------            ------------
#      |       |      |            |          |
#     File  Terminal Null         Http       Ftp
#   Logging Logging Logging


from abc import ABCMeta, abstractmethod

#####
# logging hierarchy
#####

class logging(object):
    @abstractmethod
    def write(self, s): pass


class file_logging(logging):
    def write(self, s):
        print("file: ", s)

class terminal_logging(logging):
    def write(self, s):
        print("terminal: ", s)

class null_logging(logging):
    def write(self, s):
        print("null:")

#####
# service hierarchy
#####

class service(object):
    def __init__(self):
        self.log = null_logging()

    def trace(self, newLogger):
        self.log = newLogger;

    def shutdown(self):
        self.log.write("shutdown")


class http(service):
    def get(self):
        self.log.write("http get")

    def put(self):
        self.log.write("http put")

class ftp(service):
    def get(self):
        self.log.write("ftp get")

    def put(self):
        self.log.write("ftp put")


####

service1 = http()
service2 = ftp()

service1.get()
service1.put()
service1.trace(file_logging());
service1.get()
service1.put()
service1.get()
service1.put()
service1.shutdown()

service2.get()
service2.put()
service2.trace(file_logging());
service2.get();
service2.put();
service2.trace(terminal_logging());
service2.get();
service2.put();
service2.shutdown();

