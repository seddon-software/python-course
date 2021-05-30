#! /home/chris/anaconda3/bin/python

import re, sys
import time
import datetime
import calendar
import pyttsx3
from datetime import date
import time
from pyttsx3.voice import Voice

# already done lines 1-66, restarted on line 67

codes = {
    'd' : "dark",
    'o' : "orange",
    'p' : "pink",
    'l' : "lime",
    'b' : "beige",
    'w' : "white",
    'g' : "green",
    'y' : "yellow",
    't' : "teal",
    'm' : "mid",
    ' ' : "-"
}

STATUS_FILE = "data/nextLine.txt"
LOG_FILE = "data/log.txt"
FILENAME = "data/RugPattern"


statusFile = open(STATUS_FILE, "r")
start = int(statusFile.readline())
statusFile.close()

def estimateEndDate(start):
    startDate = datetime.date(year=2021, month=4, day=15) # line 100
    todaysDate = datetime.date.today() # line 'start'
    begin = startDate.toordinal()
    now = todaysDate.toordinal()
    rowsPerDay = (start - 100) / (now - begin)
    finish = begin +  219 / rowsPerDay
    finishDate = datetime.date.fromordinal(int(finish))
    print(f"Estimated end date: {finishDate.day}/{finishDate.month}/{finishDate.year}")
inFile = open(FILENAME, "r")
lines = inFile.readlines()
lines = "".join(lines)

ROWS = 320
COLS = 198

print(f"Starting on line number {start}")


for lineNumber in range(start, ROWS+1):
    def logging(rowTime):
        logFile = open(LOG_FILE, "a")
        today = date.today()
        logFile.writelines([f"{today}: {lineNumber-1}, {rowTime:.0f}\n"])
        logFile.close()
    def displayAverageStichTime():
        interimTime = time.time()
        stich = batch+BATCH
        print(f"{stich}, {(interimTime - startTime)/stich:.2f}")
    def writeToStatusFile():
        statusFile = open(STATUS_FILE, "w")
        statusFile.writelines([f"{lineNumber}"])
        statusFile.close()
        estimateEndDate(lineNumber)
        sys.exit()
    continuing = input("Continue (yes/no): ")
    try:
        finishTime = time.time()
        rowTime = (finishTime-startTime)/60
        print(f"row took {rowTime:.0f} minutes")
        logging(rowTime)
    except:
        pass # just started
    startTime = time.time()
    if continuing == "no": writeToStatusFile()
    print(f"Line Number: {lineNumber}")
    pattern = "{lineNumber:0>3}.*\\n.*\\n.*\\n".format(lineNumber=lineNumber)
    pattern = re.compile(pattern)

    match = pattern.search(lines, re.MULTILINE)
    line = match.group()
    line = line[4:]
    line = re.sub("[\n]", "", line)
    line = re.sub("[ ]+", "", line)
    
    BATCH = 3
    halfWay = len(line)//2
    for batch in range(0, len(line), BATCH):
        input("\n<")
        print(f"{line[batch:batch+BATCH]}", flush=True)
        dashes = ''.join(['-' for char in line])
        if batch >= halfWay:
            print(f"{lineNumber}: {line[:halfWay]}", flush=True)
            reversedLine = line[halfWay:batch+BATCH][::-1]
            print(f"{lineNumber}: {dashes[:2*halfWay-batch-BATCH]}{reversedLine}", flush=True)
        else:
            modifiedLine = line[:batch+BATCH] + dashes[batch+BATCH:halfWay]
            print(f"{lineNumber}: {modifiedLine[:halfWay]}", flush=True)
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)

        for c in line[batch:batch+BATCH]:
            color = codes[c]
            engine.say(color)
        engine.runAndWait()

        displayAverageStichTime()
estimateEndDate()

