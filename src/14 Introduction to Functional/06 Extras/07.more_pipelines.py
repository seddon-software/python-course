import os; os.system("clear")
'''
More Pipelines
==============

In this more realistic example we use coroutines to filter output from the "ps -ef" command.  You will be 
prompted to search for a string that appears in the output from this command and the program then behaves 
like "grep".  For example, at the prompt enter "bash" and you will see all the bash processes currently running.

First we create a coroutine "mygrep" with
            g = mygrep(pattern)

Now we loop using our "getLine()" coroutine with 
            for line in getLine():
                match = g.send(line)

and then "send" the line to the "mygrep" coroutine.  This coroutine reads the line with
            line = f"{yield}"
            
since yield is on the right hand side of the assignment.  After checking for a pattern match, the coroutine
returns the first 120 characters of a matching line with
            yield line[:120]
'''

import subprocess, sys
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

# create a coroutine that returns lines from 'ps -ef'
def getLine():
    ps = findProcesses('ps -ef')

    line = []
    for c in ps:
        if c == '\n': 
            yield "".join(line)
            line = []
        else:
            line.append(c)

# this coroutine returns matched lines from 'ps -ef' truncated to 120 chars
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
