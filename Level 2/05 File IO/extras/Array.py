############################################################
#
#    array
#
############################################################

import array

# open a binary file and add 300 bytes: [65]*100, [1]*100, [66]*100

f = open("../data/mytest1.bin", "wb")
a = array.array('B', [65]*100)
a.extend([1] * 100)
b = array.array('B', [66]*100)
a.extend(b)
a.tofile(f)
f.close()

import subprocess
subprocess.call("hexdump -x ../data/mytest1.bin".split())
1