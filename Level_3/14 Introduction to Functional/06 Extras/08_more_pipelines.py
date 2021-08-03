import subprocess
import regex as re

# run a unix command in child process and return output
def findProcesses(cmd):
    try:
        p = subprocess.Popen(
            cmd, 
            stdout = subprocess.PIPE, 
            stderr = subprocess.PIPE, 
            shell=True)
        p.wait()        # wait for child process to terminate
        (out, err) = p.communicate()        
    except subprocess.CalledProcessError as e:
        print(e)
        sys.exit()
    return out.decode()

# create a generator that returns lines from 'ps -ef'
def getLine():
    ps = findProcesses('ps -ef')

    line = []
    for c in ps:
        if c == '\n': 
            yield "".join(line)
            line = []
        else:
            line.append(c)

# this generator returns match lines from 'ps -ef' truncated to 120 chars
def mygrep(pattern):
    pattern = re.compile(pattern)
    while True:
        line = f"{yield}"    # if input is None it gets converted to a string "None"
        if pattern.search(line):
            yield line[:120]
        # else the generator will return None

# ask for a search pattern
pattern = input("search for: ")

# create the generator
g = mygrep(pattern)
g.send(None)    # start generator

# use the getLine generator and send its output to the mygrep generator
for line in getLine():
    match = g.send(line)    # returns None if no match
    if match: print(match)
