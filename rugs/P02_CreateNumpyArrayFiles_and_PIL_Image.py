'''
This program takes in a normalised file and builds
Numpy arrays corresponding to the images (saved in ".npy" files)
Optionally, the routine can produce an image.
'''

import numpy as np
import sys
import re
import matplotlib.pyplot as plt
import re
from scipy import ndimage

def convertArrayToColor(data):
    rows = len(data)
    cols = len(data[0])
    for r in range(rows):
        for c in range(cols):
            ch = data[r][c][0]
            if ch == 'd': data[r][c] = [101,  67,  33]
            elif ch == 'o': data[r][c] = [255, 165,   0]
            elif ch == 'p': data[r][c] = [255, 182, 193]
            elif ch == 'l': data[r][c] = [152, 251, 152]
            elif ch == 'b': data[r][c] = [185, 185, 185]
            elif ch == 'w': data[r][c] = [255, 255, 255]
            elif ch == 'g': data[r][c] = [ 34, 139,  34]
            elif ch == 'y': data[r][c] = [255, 255,   0]
            elif ch == 't': data[r][c] = [  0,   0, 255]
            elif ch == 'm': data[r][c] = [165,  42,  42]
            elif ch == 'x': data[r][c] = [  0,   0,   0] # black for don't know
            else:
                print(f"error on row={r}, col={c}")
    return data

def convertToNumpyArray(line):
    array = np.empty((0,1), dtype=object)
    for c in line:
        array = np.vstack([array, [c]])
    return array

def readLines(filename):
    global FIG, COLS, TYPE, FLIP, X, Y
    try:
        f = open(filename, "r")
        result = []
        # pick up parameters
        matcher = re.compile(r"^FIG=(.*)$").search(f.readline())
        FIG = matcher.group(1)
        matcher = re.compile(r"^COLS=(.*)$").search(f.readline())
        COLS = int(matcher.group(1))
        matcher = re.compile(r"^TYPE=(.*)$").search(f.readline())
        TYPE = matcher.group(1)
        matcher = re.compile(r"^FLIP=(.*)$").search(f.readline())
        FLIP = matcher.group(1)
        matcher = re.compile(r"^X=(.*)$").search(f.readline())
        X = matcher.group(1)
        matcher = re.compile(r"^Y=(.*)$").search(f.readline())
        Y = matcher.group(1)

        for line in f:
            result.append(line[:-1])
    except IOError as e:
        print(e)
    finally:
        f.close()
    return result

def computeNumpyArray(filename):
    lines = readLines(filename)
    ROWS = len(lines)
    COLS = len(lines[0])
    data = np.empty(shape=(ROWS, COLS, 3), dtype=object)
    for n, line in enumerate(lines):
        data[n] = convertToNumpyArray(line)
    data = convertArrayToColor(data)
    data = data.astype(int)  # convert from object to int
    data = np.flip(data, axis=0)  # data is from RHS of rug
    if FLIP == "TRUE":
        data = np.flip(data, axis=1)
    data = np.transpose(data, axes=(1,0,2))
    np.save(f"data/{FIG}", data)
    print(f"data/{FIG}: {data.shape}")
    return data

def plotAndSaveImage(data):
    plt.imshow(data, cmap="gray")
    plt.savefig(f"data/{FIG}")
    plt.gcf().suptitle(f"{FIG}")
    plt.show()

np.set_printoptions(threshold=sys.maxsize)

for RUG in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11):
#for RUG in (3, 4, 10):
    data = computeNumpyArray(f"data/rug{RUG}.norm")
    # plotAndSaveImage(data)
