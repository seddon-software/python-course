#! /home/chris/anaconda3/bin/python

import re

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

PACK = 160

# remaining packs of wool (17 March 2021)
remaining = {
    'b':	33,
    't': 	11.5,
    'o':   31,
    'w':	65,
    'p': 	28,
    'm':   59,
    'd': 	60,
    'y':	16.5,
    'l': 	14.5,
    'g':	15
}

# remaining packs of wool (14 April 2021)
remaining = {
    'b':	28,
    't': 	9 + 100/PACK,
    'o':   26,
    'w':	57 + 150/PACK,
    'p': 	23,
    'm':   50,
    'd': 	53,
    'y':	14,
    'l': 	12 + 130/PACK,
    'g':	12 + 140/PACK
}

# remaining packs of wool (31 May 2021)
remaining = {
    'b':	20,
    't': 	 7.8,
    'o':    20.8,
    'w':	34.8,
    'p': 	18.3,
    'm':    36.9,
    'd': 	40,
    'y':	11.1,
    'l': 	 9.1,
    'g':	 9.2
}

FILENAME = "data/RugPattern"
inFile = open(FILENAME, "r")
lines = inFile.readlines()
lines = "".join(lines)

nextLineNumber = 167
pattern = "{nextLineNumber:0>3}.*".format(nextLineNumber=nextLineNumber)
pattern = re.compile(pattern, re.DOTALL)
match = pattern.search(lines)
remainingLines = match.group()

total = 0
d = {x: remainingLines.count(x) for x in remainingLines if x not in "0123456789 \n"}

print(f"{'color':10}{'have':>6}{'want':>6}{'have-want':>12}{'stitches':>10}")
print(f"{'=====':10}{'====':>6}{'====':>6}{'=========':>12}{'========':>10}")

for key, value in d.items():
    have = remaining[key]
    want = value/PACK
    print(f"{codes[key]:10}{have:6.1f}{want:6.1f}{have-want:9.1f}{value:12}")
    total += value

ROWS = 160*2
COLS = 99*2

print()
print(f"Total stitches to finish: {total}")
print(f"ROWS * COLS to finish: {(ROWS-nextLineNumber+1)} * {COLS} = {(ROWS-nextLineNumber+1)*COLS}")
