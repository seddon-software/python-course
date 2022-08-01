'''
Optional Arguments
==================

This example shows how to supply optional arguments (e.g. -v or --verbose)

The store_true option (in this case for verbose) means:
    if --verbose is present in the command line (it has no associated value) set verbose = True
    but if --version is missing automatically create a default value of False, i.e. set verbose = False

'''
import argparse
from argparse import Namespace

# The parser expects two parameters, both of type int and an optional parameter -v (or --verbose)
parser = argparse.ArgumentParser(epilog="... and that was the help message", exit_on_error=False)
parser.add_argument("first",  type=int, help="First number")
parser.add_argument("second", type=int, help="Second number")
parser.add_argument("-v", "--verbose", action="store_true")

# try without optional arg
text = "123 456"
print(f"\nparsing: {text}")
d = parser.parse_args(text.split())
print(d.__dict__)

# try with optional arg
text = "123 -v 456"
print(f"\nparsing: {text}")
d = parser.parse_args(text.split())
print(d.__dict__)

