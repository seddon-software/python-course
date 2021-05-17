############################################################
#
#    bytearray
#
############################################################

import array

f = open("../data/mytest2.bin", "wb")
a = bytearray([0x2F, 0x17, 0xBB, 0xCC, 0xFF, 0x1F, 0xDD, 0xEE, 0xFF])
a.extend([1] * 100)
b = array.array('B', [65]*100)
a.extend(b)
f.write(a)
f.close()

import subprocess
subprocess.call("hexdump -x ../data/mytest2.bin".split())
1