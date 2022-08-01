'''
ArgParse
========

THe argparse module takes it's arguments from sys.argv by default.  However we need to write a runner program
to test.  Alternatively, argparse will accept a set of arguments directly; this means we can test arguments
without a runner program.

Notes:
1) argparse exits the program on error unless you add:
            exit_on_error=False

2) vscode interferes with the above and issues a new SystemExit exception which we need to handle to stop
   the script exiting prematurely (this is not required if you are running outside vscode)

'''

import argparse

# The parser expects two parameters, both of type int
parser = argparse.ArgumentParser(epilog="... and that was the help message", exit_on_error=False)
parser.add_argument("first",  type=int, help="First number")
parser.add_argument("second", type=int, help="Second number")

# try with valid input
text = "123 456"
print(f"\nparsing: {text}")
d = parser.parse_args(text.split())
print(d.__dict__)

# now try with too many args
try:
    text = "123 456 789"
    print(f"\nparsing: {text}")
    d = parser.parse_args("123 456 789".split())
except SystemExit as e: pass

# now try with wrong types
try:
    text = "123 456.999"
    print(f"\nparsing: {text}")
    d = parser.parse_args(text.split())
except argparse.ArgumentError as ae:
    print(f"***** {ae}")

# now try a help message with -h
try:
    text = "-h"
    print(f"\nparsing: {text}")
    d = parser.parse_args(text.split())
except SystemExit as e: pass

# now try a help message with --help
try:
    text = "--help 123 456"
    print(f"\nparsing: {text}")
    d = parser.parse_args(text.split())
except SystemExit as e: pass



