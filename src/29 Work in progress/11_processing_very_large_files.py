import os

inFile = "/Users/seddon/data/z4.dat"
size = os.stat(f'{inFile}').st_size
print(f"size of {inFile} = {size/1024**3:.2f} GB")
total = 0
chars = 0
oldProgress = 0

with open(f'{inFile}', 'r') as f:
    for line in f:
        total += sum([int(n) for n in line.split()])
        chars += len(line)
        progress = chars // 1024**3
        if progress > oldProgress:
            gb_remaining = size//1024**3 - chars//1024**3 
            print(f">{gb_remaining} GB to go ...")
        oldProgress = progress
print(f"sum of all integers in file = {total}")
