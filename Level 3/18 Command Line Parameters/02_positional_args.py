import argparse

# This example shows how to pass positional parameters and get detailed usage message on error
parser = argparse.ArgumentParser(description='The Adder', epilog="And that's how you add")
parser.add_argument("first",  type=int, help="First number")
parser.add_argument("second", type=int, help="Second number")
args = parser.parse_args()
print((args.first + args.second))
print(args.__dict__)

