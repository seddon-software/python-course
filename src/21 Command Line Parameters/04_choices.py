'''
Choices
=======

Argparse can allow a coice of value for a parameter.  In this example, the parser accepts a single parameter,
but it can have one of 3 possible values:
            'Monday','Tuesday','Wednesday'

On success, the value is added to the dictionary key 'days'.  Note that you can only pass a single prameter
for a choice.  If you try:
            ['Monday', 'Tuesday', 'Wednesday']

you will get an error.
'''

import argparse 
 
# With choices you are only allowed to supply ONE of the alternatives 
parser = argparse.ArgumentParser() 
parser.add_argument('days', choices=['Monday','Tuesday','Wednesday']) 

def doParse(text):
    print(f"\nparsing: {text.split()}")
    args = parser.parse_args(text.split()) 
    print(args.__dict__)

doParse('Monday') 
doParse('Tuesday') 
doParse('Wednesday') 

try:
    doParse('Monday Tuesday Wednesday') 
except SystemExit as e: 
    pass

