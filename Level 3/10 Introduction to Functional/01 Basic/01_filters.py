############################################################
#
#    filters
#
############################################################

def primesFilter(x):
    if x % 2 == 0: return False
    if x % 3 == 0: return False
    if x % 5 == 0: return False
    if x % 7 == 0: return False
    if x % 11 == 0: return False
    if x % 13 == 0: return False
    return True

# set up a sequence
sequence = list(range(14, 200))

# filter out all non primes
primes = list(filter(primesFilter, sequence))
print(primes)




1
