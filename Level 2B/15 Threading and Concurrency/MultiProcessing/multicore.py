############################################################
#
#    using multiple cores
#
############################################################

''' Note: this program runs indefinitely '''

from multiprocessing import Pool, cpu_count

def random_calculation(x):
    while True:
        x * x

# try this with various numbers of processes
# and monitor activity on each cpu
p = Pool(processes=cpu_count())
p.map(random_calculation, range(cpu_count()))

