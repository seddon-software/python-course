# convert negative numbers to 32 bit unsigned hex
def toHex(n):
    n = n + 2**32
    n = n % 2**32
    return hex(n)

# because ints have infinite precision, using ~ will generate
# an infinite set of F's for negative numbers, so we need something
# like the above to similate a finite number of bits

x = 0xAE53FE13
print(" x   = {}".format( toHex(x) ))
print("~x   = {}".format( toHex(~x) ))
print("~x+x = {}".format( toHex(~x+x) ))


