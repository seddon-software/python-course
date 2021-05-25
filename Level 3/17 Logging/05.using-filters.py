import logging
import re

class ContextFilter(logging.Filter):
    def __init__(self):
        self.ip = ""
        self.user = ""
    def setIp(self, ip): self.ip = ip 
    def setUser(self, user): self.user = user 
    def filter(self, record):
        record.ip = self.ip
        record.user = self.user
        return True

LOG_FILENAME = 'logs/example3.log'
myFormat = '''%(levelname)-8s 
              %(asctime)-15s 
              %(name)-5s 
              IP: %(ip)-15s 
              User: %(user)-8s 
              %(message)s'''
pattern = re.compile(r'\s+')
myFormat = re.sub(pattern, ' ', myFormat) # strip spaces
print(myFormat)

levels = (logging.DEBUG, 
          logging.INFO, 
          logging.WARNING, 
          logging.ERROR, 
          logging.CRITICAL)
logging.basicConfig(filename = LOG_FILENAME,
                    level = logging.DEBUG,
                    format = myFormat)

myLogger = logging.getLogger("FILTER")
myFilter = ContextFilter()
myLogger.addFilter(myFilter)

myFilter.setIp("192.2.2.53")
myFilter.setUser("Sheila")
myLogger.debug('A debug message')
myFilter.setIp("192.1.1.13")
myFilter.setUser("Tom")
myLogger.info('An info message')
# output appended to 'logs/example3.log'