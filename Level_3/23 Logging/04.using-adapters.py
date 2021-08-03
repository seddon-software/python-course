import logging
import datetime
import time

class Extras(object):
    def __init__(self, ip, user):
        self.ip = ip
        self.user = user
    def get(self):
        return self.__dict__
        


LOG_FILENAME = 'logs/example2.log'
levels = (logging.DEBUG, 
          logging.INFO, 
          logging.WARNING, 
          logging.ERROR, 
          logging.CRITICAL)
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format='%(levelname)-8s %(asctime)-15s %(name)-5s IP: %(ip)-15s User: %(user)-8s %(message)s')

extras = Extras('192.1.1.52', 'sheila')
myLoggingAdapter = logging.LoggerAdapter(logging.getLogger('USER'), extras.get())
myLoggingAdapter.debug('A debug message')
myLoggingAdapter.debug('Another debug message')

# change extra info
extras.ip = '10.21.15.103'
extras.user = 'tom'
myLoggingAdapter.info('An info message')
myLoggingAdapter.info('Another info message')
# output appended to 'logs/example2.log'