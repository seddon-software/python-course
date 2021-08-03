############################################################
#
#    dictionary
#
############################################################

# set up a dictionary
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
1
