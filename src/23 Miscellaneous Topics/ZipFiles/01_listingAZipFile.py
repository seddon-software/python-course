import zipfile
import time

# note zlib is used for compression
fileName = "zips/Perl.zip"
theZip = zipfile.ZipFile(fileName, "r")

# check if valid zipfile
if zipfile.is_zipfile(fileName):
    print(fileName + " is a valid zip")
else:
    print(fileName + " is NOT a valid zip")
    
# list filenames
for name in theZip.namelist():
    print(name)
print()


# date_time has 6 fields:
# Index    Value
# 0    Year (>= 1980)
# 1    Month (one-based)
# 2    Day of month (one-based)
# 3    Hours (zero-based)
# 4    Minutes (zero-based)
# 5    Seconds (zero-based)

# strftime needs 3 additional fields (msec)
def formatTime(t):
    t = list(t)
    t.append(0)
    t.append(0)
    t.append(0)
    return time.strftime("%Y-%m-%d %H:%M:%S", tuple(t))

    
# list file information
print("{0:32} {1:10} {2}".format("filename", "date+time", "file size"))
print("{0:32} {1:10} {2}".format("========", "=========", "========="))
for info in theZip.infolist():
    print("{0:32} {1:10} {2:6d}".format(info.filename, formatTime(info.date_time), info.file_size))

    
    
    
