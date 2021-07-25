import zipfile, zlib
import glob, os
import time
import os

inDirectory = "files/Hashes/"
outDirectory = "files/Compressed/"

if not os.path.exists(outDirectory):
    os.mkdir(outDirectory)
    
for f in glob.glob(inDirectory + "*"):
    try:
        outFileName = outDirectory + os.path.basename(f)
        outFile = open(outFileName, "wb")
        indata = open(f, "rb").read()
        outdata = zlib.compress(indata, zlib.Z_BEST_COMPRESSION)
        outFile.write(outdata)
    except Exception as e:
        print(e)
        
# list file information
formatSpec = "{0:20} {1:>12} {2:>12} {3:>4}%"
print(formatSpec.format("filename", "uncompressed", "compressed", "percent"))
print(formatSpec.format("========", "============", "==========", "======="))

for f in os.listdir(inDirectory):
    inp = os.stat(inDirectory + f)
    out = os.stat(outDirectory + f)
    percent = 100 * out.st_size / inp.st_size
    print(formatSpec.format(f, inp.st_size, out.st_size, percent))
    # this gives an error for the last file - don't understand why - always the last file listed'
    