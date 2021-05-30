'''
This program takes in a raw file and converts it to real colors
The entries will be rotated (transposed) and sometimes flipped
The file has info on first 4 lines:
    FIG=fig2            # name of output file
    COLS=20             # columns in source file
    TYPE=CANVAS         # CANVAS or WOOL colors
    FLIP=FALSE          # do we need to flip lines
The Numpy arrays corresponding to the images are saved in ".npy" files
  to be used by "00_combine_rugs.py"
'''

import numpy as np
import sys
import re
import matplotlib.pyplot as plt
import re
from scipy import ndimage
plt.subplots(dpi=72*2)
np.set_printoptions(threshold=sys.maxsize)

FILENAME="rugs/rug5.norm"
TYPE = 1
figure = ""     # TBD
COLS = 0        # TBD
FLIP = ""       # TBD

#
# grey          (d) dark brown
# purple        (o) orange
# orange        (p) pink
# lime          (l) pale green
# beige         (b) beige
# white         (w) white
# sage          (g) dark green
# yellow        (y) yellow
# teal          (t) blue
# chestnut      (m) mid brown

def convertArrayToColor(data):
    # if FLIP == "TRUE":
    #     data = np.flip(data, axis=0)
    print(data.shape)
    rows = len(data)
    cols = len(data[0])
    for r in range(rows):
        for c in range(cols):
            ch = data[r][c][0]
            if TYPE == "WOOL":
                    if ch == 'd': data[r][c] = [101,  67,  33]
                    if ch == 'o': data[r][c] = [255, 165,   0]
                    if ch == 'p': data[r][c] = [255, 182, 193]
                    if ch == 'l': data[r][c] = [152, 251, 152]
                    if ch == 'b': data[r][c] = [245, 245, 220]
                    if ch == 'w': data[r][c] = [255, 255, 255]
                    if ch == 'g': data[r][c] = [ 34, 139,  34]
                    if ch == 'y': data[r][c] = [255, 255,   0]
                    if ch == 't': data[r][c] = [  0,   0, 255]
                    if ch == 'm': data[r][c] = [165,  42,  42]
                    if ch == 'x': data[r][c] = [  0,   0,   0] # black for don't know
            if TYPE == "CANVAS":
                    if ch == 'g': data[r][c] = [101,  67,  33]
                    elif ch == 'p': data[r][c] = [255, 165,   0]
                    elif ch == 'o': data[r][c] = [255, 182, 193]
                    elif ch == 'l': data[r][c] = [152, 251, 152]
                    elif ch == 'b': data[r][c] = [245, 245, 220]
                    elif ch == 'w': data[r][c] = [255, 255, 255]
                    elif ch == 's': data[r][c] = [ 34, 139,  34]
                    elif ch == 'y': data[r][c] = [255, 255,   0]
                    elif ch == 't': data[r][c] = [  0,   0, 255]
                    elif ch == 'c': data[r][c] = [165,  42,  42]
                    elif ch == 'x':
                        data[r][c] = [  0,   0,   0] # black for don't know
                    else:
                        print(r, c)
    return data

def processLine(line):
    processedLine = np.empty((0,1), dtype=object)
    number = ""
    for c in line:
        if c in '0123456789':
            number += c
            continue
        if number:
            n = int(number)
            number = ""
            # if repeat count
            for _ in range(n-1):  # already printed one character
                processedLine = np.vstack([processedLine, [lastChar]])
        if c in 'abcdefghijklmnopqrstuvwxyz':
            lastChar = c
            processedLine = np.vstack([processedLine, [c]])
    return processedLine

def removeCommentsAndEmptyLines(f):
    global FIG, COLS, TYPE, FLIP
    result = []
    matcher = re.compile(r"^FIG=(.*)$").search(f.readline())
    FIG = matcher.group(1)
    matcher = re.compile(r"^COLS=(.*)$").search(f.readline())
    COLS = int(matcher.group(1))
    matcher = re.compile(r"^TYPE=(.*)$").search(f.readline())
    TYPE = matcher.group(1)
    matcher = re.compile(r"^FLIP=(.*)$").search(f.readline())
    FLIP = matcher.group(1)

    for line in f:
        if line[0] != "#" and line[0] != "\n":
            result.append(line)
    return result


try: 
    f = open(FILENAME, "r")
    lines = removeCommentsAndEmptyLines(f)
    try:
        ROWS = len(lines)
        data = np.empty(shape=(ROWS, COLS, 3), dtype=object)
        for n, line in enumerate(lines):
            z = processLine(line)
            print(z.shape)
            data[n] = processLine(line)
    finally:
        f.close()
except IOError as e:
    print(e)
data = convertArrayToColor(data)
data = data.astype(int)


data = np.transpose(data, axes=(1,0,2))
if FLIP == "TRUE":
    data = np.flip(data, axis=0)
print(data.shape)
np.save(f"rugs/{FIG}", data)
plt.imshow(data, cmap="gray")
plt.savefig(f"rugs/{FIG}")
plt.gcf().suptitle(f"{FIG}")
plt.show()