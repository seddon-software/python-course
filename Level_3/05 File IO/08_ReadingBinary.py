############################################################
#
#    binary data
#
############################################################

# use 'array' for formatting large amounts binary data
# use 'struct' for smaller (fixed size) amounts
import array
import os

def readBinary(filename):
    try:
        size = os.stat(filename).st_size
        f = open(filename, "rb")
        ints = array.array('B')    # sets up a unsigned integer buffer
        ints.fromfile(f, size)     # populates the buffer
        return ints.tolist()       # return list of ints
    except Exception as e:
        print(e)
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws

intList = readBinary('data/myfile-1.bin')

print(("{:>10s}{:>10s}".format("Decimal", "Hex")))
for i in intList:
    print(("{:10d}{:>10s}".format(i, hex(i))))


1