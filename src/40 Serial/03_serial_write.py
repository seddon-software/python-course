import serial

import subprocess, os


pts = int(input("pts number: "))
ser = serial.Serial(f'/dev/pts/{pts}')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'c12charactersThis is a line of text\n')     # write a string
ser.close()             # close port


