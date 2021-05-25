import argparse
from argparse import Namespace

# This example shows how to supply optional arguments (e.g. -v or --verbose)
# The store_true option (in this case for verbose) means:
#     if --verbose is present in the command line (it has no associated value) set verbose = True
#     but if --version is missing automatically create a default value of False, i.e. set verbose = False

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

print(args.__dict__)
if args.verbose:
    print("This example examines optional arguments")
else:
    print("optional args")
