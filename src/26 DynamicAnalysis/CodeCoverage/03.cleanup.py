'''
This program removes the tempory files created earlier
'''

def cleanDirectory(d):
    try:
        shutil.rmtree(d)
    except:
        pass

import os, shutil
os.chdir("tests")
cleanDirectory("test_part1")
cleanDirectory("test_part2")
cleanDirectory("test_part3")
cleanDirectory("test_part4")

