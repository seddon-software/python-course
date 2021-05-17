import time
from myprogram import *

start_cpu = time.clock()  # ok for unix, but same as time.time on windows
start_real= time.time()

foo()

end_cpu = time.clock()
end_real = time.time()
print(("%f Real Seconds" % (end_real - start_real)))
print(("%f CPU seconds" % (end_cpu - start_cpu)))
