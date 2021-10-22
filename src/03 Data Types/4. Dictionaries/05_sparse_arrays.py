############################################################
#
#    dictionary
#
############################################################

import sys

# set up a dictionary with 'int' keys
hash = { 
            2507: ('Red', 'Green', 'Blue'),
             672: ('Black', 'White', 'Grey'),
            3496: ('Orange', 'Purple', 'Yellow')
       }

print(hash[672])

try:
    print(hash[7845])
except KeyError as e:
    print("Key error: " + str(e))

print(f"size of hash = {sys.getsizeof(hash)} bytes")
