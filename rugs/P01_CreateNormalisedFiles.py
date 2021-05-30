'''
This program converts raw data files int normalised files
CANVAS colors are converted to WOOL colors
and the info at the front of the file is changed accordingly (TYPE=WOOL)
'''
import numpy as np
import sys, re
import matplotlib.pyplot as plt
plt.subplots(dpi=72*2)
np.set_printoptions(threshold=sys.maxsize)

def convertArray(data):
    line = []
    rows = len(data)
    cols = len(data[0])
    for r in range(rows):
        for c in range(cols):
            ch = data[r][c][0]
            if TYPE == "WOOL":
                line.append(ch)
            if TYPE == "CANVAS":
                if   ch == 'g': line.append('d')
                elif ch == 'p': line.append('o')
                elif ch == 'o': line.append('p')
                elif ch == 'l': line.append('l')
                elif ch == 'b': line.append('b')
                elif ch == 'w': line.append('w')
                elif ch == 's': line.append('g')
                elif ch == 'y': line.append('y')
                elif ch == 't': line.append('t')
                elif ch == 'c': line.append('m')
                elif ch == 'x': line.append('x')
                else:
                    print("unknown color")
        line.append('\n')
    return "".join(line)

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
    global FIG, COLS, TYPE, FLIP, X, Y
    result = []
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
        if line[0] != "#" and line[0] != "\n":
            result.append(line)
    return result

def copyParametersToOutputFile(lines, FILENAME):
    # copy parameters in first 6 lines of input file to output file
    inFile = open(FILENAME, "r")
    outFile = open(f"{FILENAME}.norm", "w")
    outFile.write(inFile.readline())
    outFile.write(inFile.readline())
    inFile.readline()  # replace with next line
    outFile.write("TYPE=WOOL\n")
    outFile.write(inFile.readline())
    outFile.write(inFile.readline())
    outFile.write(inFile.readline())
    inFile.close()
    outFile.writelines(lines)

def master(FILENAME):
    try: 
        f = open(FILENAME, "r")
        lines = removeCommentsAndEmptyLines(f)
        try:
            ROWS = len(lines)
            data = np.empty(shape=(ROWS, COLS, 1), dtype=object)
            for n, line in enumerate(lines):
                try:
                    data[n] = processLine(line)
                except:
                    print(n, line)
            print(f"{FILENAME}: size of numpy array: {data.shape}")
        finally:
            f.close()
    except IOError as e:
        print(e)
    lines = convertArray(data)
    copyParametersToOutputFile(lines, FILENAME)

for RUG in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11):
#for RUG in (3, 4, 10):
    master(f"data/rug{RUG}")
