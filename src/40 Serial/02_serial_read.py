import serial

import subprocess, os


pts = int(input("pts number: "))

with serial.Serial(f'/dev/pts/{pts}', 19200, timeout=10) as ser:
    x = ser.read()          # read one byte
    print(x)
    s = ser.read(12)        # read up to twelve bytes
    print(s)
    line = ser.readline()   # read a '\n' terminated line
    print(line)
