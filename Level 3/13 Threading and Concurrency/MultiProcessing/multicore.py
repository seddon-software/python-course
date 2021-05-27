############################################################
#
#    using multiple cores
#
############################################################

''' 
Note: this program runs indefinitely 
use htop to monitor cpus utilisation
'''

from multiprocessing import Pool, cpu_count

def random_calculation(x):
    while True:
        x * x

# try this with various numbers of processes
# and monitor activity on each cpu
print(cpu_count())
p = Pool(processes=cpu_count())
p.map(random_calculation, range(cpu_count()))

